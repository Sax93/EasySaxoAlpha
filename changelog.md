# <center>Changelog (Version 1.11.02, Sep 15th)</center>

## <center>1. Added new commands *(a lot)*</center>

### 1. `Restart` command: Restarts the computer after a defined time in seconds *(omit seconds for instant reset; flag `cancel` to cancel operation if scheduled)*

- Syntax: `restart [seconds; {cancel}]`

### 2. `Sleep` command: Puts the computer to sleep immediately (a. k. a. *suspended state*)

- Syntax: `sleep`

### 3. `Lock` command: Locks the computer session immediately

- Syntax: `lock`

### 4. `TempFlush` command: Clears *(most of)* the files in the `\\Temp` directory of the system

- Syntax: `tempflush`

### 5. `DNSFlush` command: Clears the cache of the DNS resolver in the system

- Syntax: `dnsflush`

### 6. `App` command: Uses app manager commands

- Syntax: `app (command)`
- Subcommands: `app ({restart}, {unins}, {log ({mute}, {unmute}, {codes})}, {state})`
>
> - `Restart` > Restarts the app in the same terminal.
> - `Unins` > Sets up the app uninstaller (earlier known as base command `unins`)
> - `Log` > Manages a new app logger:
>>
>> - `Mute/Unmute`: Mutes or unmutes the App logger, which throws exception messages that warn the user about mismatches in the prompt as well as other information.
>> - `Codes`: Shows the log code of the App logger.
>>
> - `State` > Shows the app statistics according to the App manager.

## <center>2. Extended functionality for `Shutdown` and `Tree` commands.</center>

### `Shutdown`
Using the `shutdown` command plainly will instantly turn your computer off, or if you enter a `seconds` argument, it will do the same after the entered amount of seconds.

This update adds a new argument; `Cancel` (or `Abort`). This cancels the active shutdown countdown, therefore *cancelling the shutdown operation*.

Syntax: `shutdown cancel`

### `Tree`

A new argument was added for command `Tree`. The tree build *maximum depth* is now customizable.

`> tree`                    -> Renders tree of the current directory, maximum depth as 4 (will not render content deeper than four folders).
`> tree [path]`             -> Renders tree of the entered path, maximum depth of 4. (`.` points at the current path)
`> tree [path] [maxdepth]`  -> Renders tree of the entered path, maximum depth of the entered number. *(If not a number or a negative value, defaults to 4)*

> Note: Combining deep root paths (like drive roots) with a large max-depth can severely impact performance.

## <center>3. Added [*path assurance **disclaimers***](#-path-assurance-disclaimers) for path-resolving operations.</center>

Every command that calls the **Path resolver** function is now evaluated with a set of disclaimers, meant to *advice the user for mismatches in the result of such called command*.

Example:

- User enters > `dirsz C:`, which calls the Path resolver.
- The resolver looks for any possible paths, aiming at which seems the most precise.
- The resolver returns the path, which may or may not be the referred path.

Path issues are something that EasySaxo struggles to manage perfectly, so a close solution is to add *path assurance disclaimers*.

Example:

- User enters > `dirsz C:`, which calls the Path resolver.
- The resolver looks for any possible paths, aiming at which seems the most precise.
- The resolver returns the path along with a dimmed disclaimer, variable according to case.

While it certainly does not aims at the intended path, it lets the user know that the resolver had some minor issues while parsing the path.
> Note: During tests, some of these mentioned disclaimers were removed due to resolving their specific errors.

## <center>4. `Unins` moved from being base command.</center>

As mentioned before, the `Unins` command is no longer a base command, and it has to be called from `App` command as a subcommand.

## <center>5. Updated **app metadata**.</center>

With the introduction of the `App` command, the app metadata has been seen noticeably updated.

Callable with `app state` prompt, the updated information includes:

- App name, version and build date.
- Developer *(and with luck, future ones)*
- Session time (time since the app was opened)
- Logger state (either **muted** or **unmuted**)
- Memory usage (usually around 50-90MB)
- CPU usage

## <center>6. Restructured *code base* in main files.</center>

The logic in the code of soome app files has been modified slightly, with the goal of optimizing the app priority operations as well as to fill fallbacks.

## <center>7. Updated *logos*.</center>

EasySaxo and SXF logos have been updated in `builtinrender.py`. In order to reflect the major updates in the app since the very first versions of the app, the app logo had changed its design.

## <center>8. Fixed errors in commands: `FileWrt`, `FileRd`, *sub* `Unins`</center>

An issue was found with the `FileWrt` and `FileRd` command, which raised an `UnicodeDecodeError`.

- Cause: Using the command with a file whose encoding is not `UTF-8` (like an image or an audio file) raises an invalid byte start error, and because the resolver does not check the encoding of the called file, the `UnicodeDecodeError` sneaks in through and crashes the application.

- Solution: The error handler in both commands now catches this exception, disclaiming the `Invalid file or directory` message instead.

By other hand, subcommand `Unins` showed a small issue that did not fully delete the app files.

- Cause: The uninstaller only scanned files in `~easysaxo` instead of the full folder.

- Solution: Resolve two directories up to point at the `EasySaxoAlpha-main` folder and delete.

## <center>9. Added flags in `DirLocation`: </center>
> Since all of the next flags point at `C:\\Users\\User`, the parent path will be called as `~`
- `-<dwn`: Points at `~\\Downloads`.
- `-<docs`: Points at `~\\Documents`.
- `-<imgs`: Points at `~\\Pictures`.
- `-<aud`: Points at `~\\Music`.
- `-<vid`: Points at `~\\Videos`.

## <center>10. Added [**Encoding Evaluator**](#-encoding-bom-evaluator).

In EasySaxo Alpha 1.11.02 when using either `FileRd` or `FileWrt` commands, you may notice a message above the content, that says:

### `Encoding: UTF-8`

This indicates the positive outcome of a new feature added in both of these commands; the *Encoding Evaluator*.

## <center>11. *(Minor add)* Updated *force shell* flags.

If the prompt starts with `>`, it will act as the *EasySaxo command flag* (`-e`)
If the prompt starts with `$`, it will act as the *System shell command flag* (`-s`)

## <center>12. Updated *path resolving* functionality.

Path resolving was (once again) updated to fix command path location. It is now organized like this:

1. No directory -> `.`, or `cwd` by default.
2. Absolute path
3. *Candidates* (`cwd`, `-<root\\` or `-<es\\`)
4. Creator (boolean)
5. Fallback (`.\\path`)


# <center>Additional data (Details about new features)</center>

Index:
-
* [App logger](#-app-logger)
* [Encoding (BOM) evaluatotr](#-encoding-bom-evaluator)
* [Path Assurance disclaimers](#-path-assurance-disclaimers)

## > App Logger

This logger can be mostly seen in error messages, invalid inputs or values, fallbacks or when closing the app.
It will be **muted** by default, and you can activate it using this prompt: > `app log unmute`

Once the logger is unmuted, every error will be assigned with a certain number, the *log code*.

To look at the log code, use this prompt: `app log codes`

If an error occurs, the logger will display a message stating:

### `[EasySaxo] |> (Code: X) An error occured.`

> Where `X` is a character (`X` or `xX`) and `An error occured` is the error message.

To mute it, use this prompt: `app log mute`

## > Encoding (BOM) evaluator

Because of the `FileRd` and `FileWrt` commands, an Encoding Evaluator was added. It will check if the byte order mark (BOM) is either UTF-8 or UTF-16. Else will stop the command execution.

- `UTF-8` / `UTF-16` : The file is ready for reading and writing.
- `UTF-32` : EasySaxo does not support reading or writing files with this encoding.
- `None` / `Error` : Though not displayed, this raises a disclaim: "**File `[path]` could not be read**".
- `Directory` : Though not displayed, this raises a disclaim: "**Path `[path]` is a directory, not a file**".

## > Path Assurance disclaimers

The path assurance disclaimers, as earlier said, are meant to inform the user about possible mistakes during the path analysis, which could lead to an unfound file, a wrong path or a name error while resolve.

The common disclaimers are:

- `Make sure the path is written correctly.` : Indicates that the resolver found a path that does not exactly match the actual directory name. It warns that the resolver parsed the input and returned a different one, despite usually not meaning a full path change. It shows up when the path is not found or the path had to be parsed several times.

- `'/d' in this command is automated, you do not need to type it!` : Despite not being a possible error disclaimer, this message informs that changing drive paths do not need to use the `/d` flag in the terminal.

Feel free to report any issue with the software.

sxf
