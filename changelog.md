> <center>A (finally) major update for EasySaxo Alpha</center>

# <center>Changelog (Version 1.08, Aug 22th)</center>

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

sxf