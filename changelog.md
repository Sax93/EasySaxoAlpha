> <center>A mostly minor update for ES Alpha 1.08-2</center>

# <center>Changelog (Version 1.082, Aug 25th)</center>

<details>
<summary>ES Alpha 1.08 base changelog</summary>

## <center>1. Added new commands: `web` and `dirsz`.</center>
Two new commands were just added to EasySaxo:

`web` command allows to interact with a **website** through its _URL_ (usually `https://insertedurl.com`) and through its _method_ (`GET`, `POST` and so).
> Syntax: `web <url> [method] [payload (only if method)]`

`dirsz` command is the main fix to `filesz` command, allowing to get byte-formatted size of a **directory** based on the directory path. Allows **`.`** as current directory.
> Syntax: `dirsz <non-file directory/path>`

## <center>2. Added flag to system-shell command: `-silent`.</center>
Since **1.02 Version**, EasySaxo is able to use *system shell* commands along with its own commands, and with the lastest updates, processes started by EasySaxo are now logged with their *return code*, which in errors, can get _really_ long.

This new `-silent` flag mutes the log in case of error/exception, only showing the output od the process.

> Syntax: `<systerminal_cmd> -silent -s` / `<systerminal_cmd> -silent`\
> Note: This addition will not work with processes ran with `fileopn`.

## <center>3. Updated app *minimum and recommended requirements*.</center>
During *file and resource usage inspection*, it was decided to update the required software/hardware features to run the app. 

<details>
<summary>Here is a quick peek:</summary>

> **Minimum Requirements:**
>> **RAM**: `256 megabytes` of free memory.\
>> **CPU**: `Single-Core 1.5 GHz` (x86-64 CPU).\
>> **Storage**: `200 megabytes` of free storage space.\

> **Recommended Requirements:**\
>> **RAM**: `1024 megabytes (1 gigabyte)` of free memory.\
>> **CPU**: `Dual-Core 2.0 GHz` (x86-64/ARM64 CPU).\
>> **Storage**: `400 megabytes` of free storage space.\

> Both `OS` and `Python Runtime Version` stay the same.
</details>

## <center>4. App optimization by *debloating* (`pyproject.toml`)</center>
After checking dependencies defined in `pyproject.toml`, more than **6 dependencies** were removed.\
The reason behind was, _besides `deptry` reasons_, to debloat **Virtual Environment** and not bloating the folder with another `150 megabytes` of unused libraries. 

<details>
<summary>Removed dependencies (missing sub-libraries):</summary>

> - cputil
> - scikit-learn
> - nvidia-ml-py
> - wmi
> - wintmp
> - pypiwin32
</details>

<details>
<summary>Added dependencies (missing sub-libraries):</summary>

> - BeautifulSoup4
> - Requests
> - URLlib
</details>

## <center>5. `KeyboardInterrupt` constant patching.</center>
To my surprise, a great chunk of the app was not supported over `KeyboardInterrupt`, and crashed the app early; **while loading**.\
This half-patch uses `sys` to prevent `KeyboardInterrupt` to crash the entire app while it is still _loading its settings and commands_.
</details>

<details>
<summary>ES Alpha 1.081 changelog</summary>

## <center>6. Added *country flags* as doodles for command `banner render <doodle>`.
As a tiny add-up to the version, the first additional feature is a set of *8 doodled country flags* in the `render` attribute inside `banner` command.

<details>
<summary>Added country flags (with alias):</summary>

- Britain (UK)
- Chile
- Deutschland (Germany)
- Japan
- Mexico
- Switzerland (Switz)
- United States (USA)
- Venezuela
</details>

Since *doodles* only range a max of **3 lines**, some flags may look really weird, so sorry about that ;(
</details>

## <center>7. Modified **path display** set subcommand and `cd` command.
As a better way at "acknowledging" the current path/directory, both *`pathdisplay` set subcommand* and `cd` command were lightly modified.

- The directory path will now be shown above the user command input as a *dim text*, leaving the user a guide of where they are located.\
    - When located in the app *root folder* (by default '`\src\easysaxo`'), the path will be displayed as "`~easysaxo`" to shorten the full path.\
    - If the user enters a subfolder inside the root (e. g. '`\src\easysaxo\esmodules\`'), the path will be displayed as "`~easysaxo\esmodules`".
    - To see the full path of where the *root folder* is located, use `cd` command.
- The `cd` command received a minor modification linked to the *path display* update; will refer to paths in *root folder* as "`~easysaxo\path`". Though, the entry stays the same (`cd path`).

## <center>8. Added **build date** as *app metadata*.
ES Alpha 1.082 adds a new metadata to the app, which displays the earliest *modification date* of any listed ES Alpha file as the **build date**. It is meant to work as a date route for code modification, useful for patchs and updates.

## <center>9. Updated **Built-in Changelog** display.
In the app, the way the integrated changelog (`changelog`) displayed was just modified, taking the shape of a *resizable squared box* instead of a *raw scroll*.

sxf