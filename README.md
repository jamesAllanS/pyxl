# pyxl

pyxl is a simple script for Linux which launches a series of x applications (GUI apps) in sequence and waits until each app is open until launching the next.
Useful for cases such as starting all required apps/procs before attempting to load saved Jack audio connections.

### Dependencies

* Requires python 3.7
* Requires xdotool
```
sudo apt install xdotool
```

### Usage examples

```
./pyxl.py SAVEDSESSION.txt
```
or
```
./pyxl.py SAVEDSESSION.csv
```
where SAVEDSESSION is the name of your saved session file, which should be a plain text file with each line being the command to run exactly as it appears on the command line.
So the following commands will open caja in an 800 x 800 window and vs code with the file titled file.txt.
```
caja -g '800x800'
code /path/to/your/file.txt
```

## Known issues

* many, see issues for details and feel free to report in new ones
