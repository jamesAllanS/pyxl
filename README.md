# seshm

Seshm is a simple script for Linux which runs a series of commands in sequence and waits until each app is open until launching the next.
Useful for cases such as starting all required apps/procs before attempting to load a saved Jack audio connections.

### Dependencies

* Requires python 3.7
* Requires xdotool
```
sudo apt install xdotool
```

### Usage examples

```
./seshm.py SAVEDSESSION.txt
```
or
```
./seshm.py SAVEDSESSION.csv
```
where SAVEDSESSION is the name of your saved session file, which should be a plain text file with each line being the command to run exactly as it appears on the command line.
So the following commands will open caja in an 800 x 800 window and vs code with the file titled file.txt.
```
code /path/to/your/file.txt
caja -g '800x800'
```

## Known issues

* many, see issues for details and feel free to report in new ones