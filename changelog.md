> <center>A major update for ES Alpha 1.10</center>

# <center>Changelog (Version 1.10.00, Sep 7th)</center>

## <center>1. Added new command flags for *path related commands*
EasySaxo Alpha 1.10 base first comes up with ***Directory Locator*** flags that point to absolute paths, no matter where the user is located at.

1. Flag `-<root`: Points directly at the root directory of EasySaxo.
>> Usage: `cd -<root` (changes to X:/.../src/easysaxo)

2. Flag `-<es`: Points directly at ESModules directory.
>> Usage: `ls -<es` (lists as `~easysaxo/esmodules`)

3. Flag `-<fc`: Points directly at FileCreation directory in ESModules.
>> Usage: `dirsz -<fc` (displays the size of `~easysaxo/esmodules/filecreation`)

4. Flag `-<drv`: Points at the drive root; also known as: C:\\, D:\\, F:\\ and so on.
>> Usage: `cd -<drv` (changes to `C:\` or the root of the path drive.)
>> As well: `cd -<drv F:` (changes to `F:\`)

sxf