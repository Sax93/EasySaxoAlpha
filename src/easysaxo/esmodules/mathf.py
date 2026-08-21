"""Math Holder for EasySaxo"""

# `mathf.py` ONLY FOR MATH FUNCTIONS COMMAND DEFINING
# math shii and stuff ig

import ast
import random

from colorama import Fore, Style

from .lister import MathList as Mt


class MathFunc:
    @staticmethod
    def help_attribute(attr: str):
        attr = attr.strip()
        attr_l = attr.lower()
        if attr in Mt.MATHSET_HELP:
            print(f"{Fore.GREEN}=== MathSet Help: {attr} ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Mt.MATHSET_HELP[attr]}{Style.RESET_ALL}")
        elif (attr in Mt.mathset and attr not in Mt._reserved) or (attr_l in Mt.mathset and attr_l not in Mt._reserved):
            print(f"'{Fore.CYAN}{attr or attr_l}{Style.RESET_ALL}' (user variable) = {Fore.GREEN}{Mt.mathset[attr or attr_l]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No MathSet documentation found for '{attr}'.{Style.RESET_ALL}")

    @staticmethod
    def _eval_ast_node(node):
        # WARNING: van rossum be frowning at ts
        
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
            if op_type in Mt._allowed_operators:
                return Mt._allowed_operators[op_type](MathFunc._eval_ast_node(node.operand))
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")

        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in Mt._allowed_operators:
                return Mt._allowed_operators[op_type](MathFunc._eval_ast_node(node.left), MathFunc._eval_ast_node(node.right))
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
            if open_count > close_count:
                expression += ')' * (open_count - close_count)

            parsed_ast = ast.parse(expression, mode='eval').body
            print(f"Result: {Fore.GREEN}{MathFunc._eval_ast_node(parsed_ast)}{Style.RESET_ALL}")
        except (ValueError, ZeroDivisionError, TypeError) as e:
            print(f"{Fore.RED}Error evaluating expression: {e}{Style.RESET_ALL}")
        except SyntaxError as e:
            print(f"{Fore.RED}Invalid syntax in expression: {e}{Style.RESET_ALL}")

    @staticmethod
    def getmath(): print(Mt.math_funcslist)

    @staticmethod
    def rtool(start: int | None = None, end: int | None = None):
        try:
            if start is not None and end is not None: num = random.randint(min(start, end), max(start, end))
            elif start is not None: num = random.randint(1, start)
            else: num = random.randint(1, 1000)
            print(f"Random number: {Fore.GREEN}{num}{Style.RESET_ALL}")
        except (ValueError, TypeError, KeyboardInterrupt) as e:
            print(f"{Fore.RED}Error generating random number: {e}{Style.RESET_ALL}")

    @staticmethod
    def set_var(var_name: str, value: float):
        try:
            Mt.mathset[var_name] = float(value)
            print(f"Variable {Fore.CYAN}{var_name}{Style.RESET_ALL} assigned value {Fore.GREEN}{float(value)}{Style.RESET_ALL}.")
        except ValueError: print(f"{Fore.RED}Invalid numeric value provided.{Style.RESET_ALL}")

    @staticmethod
    def del_var(var_name: str):
        if var_name in Mt._reserved:
            print(f"{Fore.RED}Cannot delete built-in constant/function '{var_name}'.{Style.RESET_ALL}")
        elif var_name in Mt.mathset:
            del Mt.mathset[var_name]
            print(f"Variable {Fore.GREEN}{var_name}{Style.RESET_ALL} deleted.")
        else: print(f"{Fore.RED}Variable '{var_name}' not found.{Style.RESET_ALL}")

    @staticmethod
    def getvar(var_name: str):
        if var_name in Mt.mathset and var_name not in Mt._reserved:
            print(f"{Fore.CYAN}{var_name}{Style.RESET_ALL} = {Fore.GREEN}{Mt.mathset[var_name]}{Style.RESET_ALL}")
        elif var_name in Mt._reserved:
            print(f"{Fore.YELLOW}'{var_name}' is a built-in function/constant.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Variable '{var_name}' not found.{Style.RESET_ALL}")

    @staticmethod
    def list_vars():
        user_vars = {k: v for k, v in Mt.mathset.items() if k not in Mt._reserved}
        if user_vars:
            print(f"\n{Fore.BLUE}== USER VARIABLES =={Style.RESET_ALL}\n")
            for k, v in user_vars.items(): print(f"{Fore.CYAN}{k:<15}{Style.RESET_ALL}: {Fore.GREEN}{v}{Style.RESET_ALL}")
        else: print(f"{Fore.YELLOW}No custom variables saved yet.{Style.RESET_ALL}")

# love math tho