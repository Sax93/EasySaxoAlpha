"""Math Holder for EasySaxo"""

import ast
import random

from rich import print

from ..config import easysaxo
from .lister import MathList as Mt


class MathFunc:
    """Mathematic expressions and equations handler + MathSet handler."""
    @staticmethod
    def help_attribute(attr: str):
        attr = attr.strip()
        attr_l = attr.lower()
        if attr in Mt.MATHSET_HELP:
            print(f"[green]=== MathSet Help: {attr} ===[/green]")
            print(f"[yellow]{Mt.MATHSET_HELP[attr]}[/yellow]")
        elif (attr in Mt.mathset and attr not in Mt._reserved) or (attr_l in Mt.mathset and attr_l not in Mt._reserved):
            print(f"'[cyan]{attr or attr_l}[/cyan]' (user variable) = [green]{Mt.mathset[attr or attr_l]}[/green]")
        else:
            easysaxo.k_log("")
            print(f"[red]No MathSet documentation found for '{attr}'.[/red]")

    @staticmethod
    def _eval_ast_node(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)): return node.value
            raise ValueError("Only numeric constants allowed.")

        elif hasattr(ast, "Num") and isinstance(node, ast.Num): return node.n

        elif isinstance(node, ast.Name):
            if node.id in Mt.mathset:
                val = Mt.mathset[node.id]
                if callable(val): raise ValueError(f"'{node.id}' is a function, not a constant or variable.")
                return val
            raise ValueError(f"Undefined variable '{node.id}'")
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type in Mt._allowed_operators: return Mt._allowed_operators[op_type](MathFunc._eval_ast_node(node.operand))
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")

        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in Mt._allowed_operators: return Mt._allowed_operators[op_type](MathFunc._eval_ast_node(node.left), MathFunc._eval_ast_node(node.right))
            raise ValueError(f"Unsupported binary operator: {op_type.__name__}")

        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in Mt.mathset and callable(Mt.mathset[func_name]):
                    args = [MathFunc._eval_ast_node(arg) for arg in node.args]
                    return Mt.mathset[func_name](*args)
                raise ValueError(f"Unknown function '{func_name}'")
            raise ValueError("Complex function calls not supported.")

        else: raise ValueError(f"Unsupported syntax expression: {type(node).__name__}")

    @staticmethod
    def evaluate(expression: str):
        try:
            open_count = expression.count('(')
            close_count = expression.count(')')
            if open_count > close_count: expression += ')' * (open_count - close_count)

            parsed_ast = ast.parse(expression, mode='eval').body
            print(f"Result: [green]{MathFunc._eval_ast_node(parsed_ast)}[/green]")

        except SyntaxError as e:
            # e.offset points to the character position of the syntax error
            offset = e.offset or 1
            pointer_pos = min(offset - 1, len(expression)) 
            
            print(f"[red]Syntax Error:[/red] {e.msg}")
            print(f"  {expression}")
            print(f"  [red]{' ' * pointer_pos}^[/red]")

        except (ValueError, ZeroDivisionError) as e:
            easysaxo.k_log("6")
            print(f"[red]Evaluation Error:[/red] {e}")
        except TypeError as e: 
            easysaxo.k_log("6")
            print(f"[red]Type Error:[/red] {e}")
        except KeyboardInterrupt: 
            easysaxo.k_log("11")
            print("\n[yellow]Evaluation interrupted.[/yellow]")

    @staticmethod
    def getmath(): print(Mt.math_funcslist)

    @staticmethod
    def rtool(start: int | None = None, end: int | None = None):
        try:
            if start is not None and end is not None: num = random.randint(min(start, end), max(start, end))
            elif start is not None: num = random.randint(1, start)
            else: num = random.randint(1, 10000)
            print(f"Random number: [green]{num}[/green]")
        except (ValueError, TypeError, KeyboardInterrupt) as e: 
            easysaxo.k_log("6" if not isinstance(e, KeyboardInterrupt) else "11")
            print(f"[red]Error generating random number: {e}[/red]")

    @staticmethod
    def set_var(var_name: str, value: float):
        try:
            Mt.mathset[var_name] = float(value)
            print(f"Variable [cyan]{var_name}[/cyan] assigned value [green]{float(value)}[/green].")
        except ValueError:
            easysaxo.k_log("6")
            print("[red]Invalid numeric value provided.[/red]")

    @staticmethod
    def del_var(var_name: str):
        if var_name in Mt._reserved:
            easysaxo.k_log("m1")
            print(f"[red]Cannot delete built-in constant/function '{var_name}'.[/red]")
        elif var_name in Mt.mathset:
            del Mt.mathset[var_name]
            print(f"Variable [green]{var_name}[/green] deleted.")
        else: 
            easysaxo.k_log("m2")
            print(f"[red]Variable '{var_name}' not found.[/red]")

    @staticmethod
    def getvar(var_name: str):
        if var_name in Mt.mathset and var_name not in Mt._reserved: print(f"[cyan]{var_name}[/cyan] = [green]{Mt.mathset[var_name]}[/green]")
        elif var_name in Mt._reserved: print(f"[yellow]'{var_name}' is a built-in function/constant.[/yellow]")
        else: 
            easysaxo.k_log("m2")
            print(f"[red]Variable '{var_name}' not found.[/red]")

    @staticmethod
    def list_vars():
        user_vars = {k: v for k, v in Mt.mathset.items() if k not in Mt._reserved}
        if user_vars:
            print("\n[cyan]== USER VARIABLES ==[/cyan]\n")
            for k, v in user_vars.items(): print(f"[cyan]{k:<15}[/cyan]: [green]{v}[/green]")
        else: print("[yellow]No custom variables saved yet.[/yellow]")