> <center>A major update for ES Alpha 1.09</center>

# <center>Changelog (Version 1.09, Sep 5th)</center>

## <center>1. Added new command: `Unzip`

Function for this new command (*firstly meant for a new feature added to `Web` command*), `Unzip` command extracts the contents of a **specified ZIP file**.

Its syntax is pretty easy, being used basically with: `unzip <path/file>.zip`

Although, if the user wants to extract the ZIP file in a specified folder, the command adopts this syntax: `unzip <path/file>.zip <folder>`

## <center>2. Fixed *ES flag format* appliable in system shell commands: **`-<`**.

Since EasySaxo Alpha 1.082 and earlier stripped every word starting with simply `-`, many errors happened with *flagged commands* (e. g. `python -m pip install --upgrade pip`).

This update changes the *flag format* for future flags. For example:

### Instead of this: `<command> -silent -s`,\
### Now works like this: `<command> -<silent -s`\
This way, the terminal will not confuse the ES flags with the system flags. 

> Note: This modification does not affect the **force-command-execution** flags: `-s`, `-e`.

## <center>3. Fixed *commands* from uncaught exceptions: **`regex`, `dirsz`, `dirdel`**.

### 1. `Regex` command
> `Regex` command showed up uncaught exceptions when calling the command like this:\
> \> `regex 0 C:\ -f`\
> **Issue**: This syntax for the command raised an `OSError`, a `PermissionError` and an `IsADirectoryError`, which meant a ***serious issue*** for the command.\
> **Fix**: Added error handlers for prompts like this in the command.

### 2. `DirSz` command
> `DirSz` command, rather than a potentially harmful error, showed up a *path display inconvenience* for a prompt like this:\
>`dirsz ..`
> **Issue**: The path `.`, `..` and sequences using these path tools was output as simply: `.` or `..`, making it confusing at sight by *the lack of full path display*.\
> **Fix**: The filepath is processed as the referred path, so: [(`C:/`), (`..`) or (`.`)] paths are resolved as [(`C:\`), (`Full\Path\ReferredByDots`) and (`Full\Path\ReferredByDots\cwd`)].\
> More than a quick fix, this modification works as a *global parser* for the path (only in this command).

### 3. `DirDel` command

> `DirDel` command earlier worked with `os.rmdir` method, meaning it only worked with *empty directories*.\
> **Issue**: If by any reason, the directory had *one single byte* of information in it, it would ***crash the entire program***.\
> **Fix**: Simply replaced `os.rmdir` method with `shutil.rmtree` method, so the user can also delete directories with files in them.
>> Do not use this with important folders.

## <center>4. Updated *command functionality* for commands: **`FileRd`, `Web`**.

### 1. `FileRd` command

> **Command main function**: Display in the terminal the content of a script or file by *taking the filepath and getting its lines of text*, thus returning them to a `print()` function.\
> **Update**: Now the command will check if the file in the filepath is a `.py` script, using `pygments` library to lit up the **Python syntax**. In other words, coloring the texts if the file is a Python script.

### 2. `Web` command

> **Command main function**: Via internet, get information out of a *referred URL* and returning the content to the terminal screen.\
> **Update**: Ability to download files via a `-d` flag right after the URL.
>> **Syntax**:\
>> `web <https://url.dom/section-1> -d` *(downloads first available file)*\
>> `web <https://url.dom/section-1> -d <cool_file>` *(downloads specific file)*\
> *This function supports GitHub related links, allowing EasySaxo to download repositories, files from repositories and much more.*

## <center> 5. Changed *app name display*

The *app name and app version display* is now moved from the start screen to the terminal window name.

## <center> 6. Changed *error handler display*

For some commands, their *error handler* is now slightly modified to identify the issue more precisely.

sxf