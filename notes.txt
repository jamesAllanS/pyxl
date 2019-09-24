# Notes for xdotool etc
./home/james/MEGA/codeRef/mypython/print_stream.py | xdotool search --class code 
xdotool search --onlyvisible --class geany windowfocus --sync type --delay 250 'how to get a file here?'
xdotool search --onlyvisible --class geany getwindowgeometry --shell
xdotool search --onlyvisible --pid `pidof geany` # may not work, needs try.

## Get PID:

```bash

my-app &
echo $!

# Save PID in variable:

my-app &
export APP_PID=$!

# Save all instances PID in text file:

my-app &
echo $! >>/tmp/my-app.pid

# Save output, errors and PID in separated files:

my-app >/tmp/my-app.log 2>/tmp/my-app.error.log &
echo $! >>/tmp/my-app.pid

echo "my-app PID's: $(cat /tmp/my-app.pid)"
```