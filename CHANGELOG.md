> Idle update for EasySaxo Alpha

# Changelog (Version 1.07, Aug 21th)

## 1. Removed `runloc` command.
After some function comparison, command `cd` has a shorter and simpler way to display the current location.
It is decided to remove the command `runloc` due to **repeated function** with other command.

## 2. Fixed `KeyboardInterrupt` issue in unsupported command process.
`KeyboardInterrupt` (`Ctrl` + `C`) turned out to be a great inconvenience to commands whose processes were heavy or long when actioned, crashing the app instantly.
Even after fixes applied in 1.061 version, some commands are still affected by this issue, and this fix focused in such problem.

## 3. Rewritten `_resolve_path` and `check` command.
An incredibly overseen error occured when trying to use `check` command while *being in a different path than `easysaxo`*.
This error led to a restructuring fix in `dirloct.py`, adding new settings that allow `check` command to be used indifferently of the path the user is in.

## 4. Sorting added in **Command List** display
`help` command list display is now sorted in colors and spaces, depending on whether the command operates *in, out or in between* the program.

## 5. File extension color scheme expanded (+25 file extensions)
When using `tree` command, files will get a **certain color** based on its *extension*.
This upgrade adds personalized color to even more files.

## 6. *Secret function* extension.
The lastest *secret function* has been updated and supports more words.

sxf
