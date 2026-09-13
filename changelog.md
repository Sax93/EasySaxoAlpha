> <center>ES Alpha 1.11.xx version.</center>

# <center>Changelog (Version 1.11.00, Sep 12th)</center>

## <center>1. Added new commands *(a lot)*</center>

### 1. `Restart` command: Restarts the computer after a defined time in seconds *(omit seconds for instant reset; flag `cancel` to cancel operation if scheduled)*.
- Syntax: `restart [seconds; {cancel}]`

### 2. `Sleep` command: Puts the computer to sleep immediately (a. k. a. *suspended state*)
- Syntax: `sleep`

### 3. `Lock` command: Locks the computer session immediately.
- Syntax: `lock`

### 4. `TempFlush` command: Clears *(most of)* the files in the `\\Temp` directory of the system.
- Syntax: `tempflush`

### 5. `DNSFlush` command: Clears the cache of the DNS resolver in the system.
- Syntax: `dnsflush`

### 6. `App` command: Uses app manager commands.
- Syntax: `app (command)`
- Subcommands: `app ({restart}, {unins}, {log ({mute}, {unmute}, {codes})}, {state})`
> - `Restart` > Restarts the app in the same terminal.
> - `Unins` > Sets up the app uninstaller (earlier known as base command `unins`)
> - `Log` > Manages a new app logger:
>> - `Mute/Unmute`: Mutes or unmutes the App logger, which throws exception messages that warn the user about mismatches in the prompt as well as other information.
>> - `Codes`: Shows the log code of the App logger.
> - `State` > Shows the app statistics according to the App manager.

## <center>2. Extended functionality for `Shutdown` command.</center>

Using the `shutdown` command plainly will instantly turn your computer off, or if you enter a `seconds` argument, it will do the same after the entered amount of seconds.

This update adds a new argument; `Cancel` (or `Abort`). This cancels the active shutdown countdown, therefore *cancelling the shutdown operation*.

Syntax: `shutdown cancel`

## <center>3. Added *path assurance **disclaimers*** for path-resolving operations.</center>

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

# <center>Additional data (Details about new features)</center>

## > App Logger

This logger can be mostly seen in error messages, invalid inputs or values, fallbacks or when closing the app.
It will be **muted** by default, and you can activate it using this prompt: > `app log unmute`

Once the logger is unmuted, every error will be assigned with a certain number, the *log code*.

To look at the log code, use this prompt: `app log codes`

If an error occurs, the logger will display a message stating:
### `[EasySaxo] |> (Code: X) An error occured.`
> Where `X` is a character (`X` or `xX`) and `An error occured` is the error message.

To mute it, use this prompt: `app log mute`

## > Path Assurance disclaimers

The path assurance disclaimers, as earlier said, are meant to inform the user about possible mistakes during the path analysis, which could lead to an unfound file, a wrong path or a name error while resolve.

The common disclaimers are:
- `If this directory is incorrect, try this path instead:` : Indicates issues when typing a drive root without slash (`C:`). The resolver parses it as `C:\\`, but the disclaimer remains to warn if it ever confuses the drive with another path.

- `Make sure the path is written correctly.` : Indicates that the resolver found a path that does not exactly match the actual directory name. It warns that the resolver parsed the input and returned a different one, despite usually not meaning a full path change. It shows up when the path is not found or the path had to be parsed several times.

- `'/d' in this command is automated, you do not need to type it!` : Despite not being a possible error disclaimer, this message informs that changing drive paths do not need to use the `/d` flag in the terminal.

Feel free to report any issue with the software.

sxf