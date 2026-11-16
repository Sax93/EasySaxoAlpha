# <center>Changelog (Version 1.12.0, Nov 14th)</center>

## <center>1. Added new commands</center>

### `move`

The `move` command works for moving files to a specified directory.

> Its syntax is the command followed by the files, lastly the destination.
> To group files, use parentheses and separate each filename by commas.

> Syntax: `move [file] [dir]`; `move ([file1], [file2]) [dir]`

## <center>2. Fixed errors in commands: *`timer`*</center>

Errors in this command crashed the application abruptly when inserting *invalid times or specific messages*. This bug was patched.

## <center>3. Added new path flag: *`-<inst`*</center>

The `-<inst` path flag (short for *Installation*) points just above the `/src` directory, where all application files, including virtual environments,
core files, data and cache, are stored.

## <center>4. Added new subcommand for command `app`: *`update`*.</center>

The `app` command received a new particular subcommand.

The `app update` prompt executes the next sequence:

- Fetch current app version.
- Via internet, check the GitHub repository for EasySaxo Alpha.
- Fetch GitHub EasySaxo version.
- Compare numbers.
- Inform if the user should update the app or not.

In case the GitHub-fetched version is lower or equal, the app will not ask and not update.\
Otherwise, it will ask the user to update. If yes, it will install and replace the files.

## <center>5. Optimized **app files**.</center>

Certain features of earlier versions were removed to improve performance.
- Easter eggs
- Trailing spaces in code
- Sleep deprivation

## <center>6. Removed dependencies: **Colorama**</center>

The *colorama* library was removed and replaced with Rich coloring, meant to remove storage usage.

## <center>7. Removed autocompletion.</center>

Autocompletion of earlier versions was removed along with Colorama coloring.


Feel free to report any issue with the software.

sxf
