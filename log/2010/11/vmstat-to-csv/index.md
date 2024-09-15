# Import vmstat logs into LoadRunner

Here’s a little script to format vmstat’s output into something you can import
into LoadRunner’s analysis tool:

```python
import sys, time

sys.stdout.write("Date,Time,"
                 "Proc Run,Proc sleep,"
                 "Mem swap use,Mem free,Mem buffered,Mem Cache,"
                 "Swap in,Swap out,Blocks in,Blocks out,"
                 "Interrupts,Context switches,"
                 "CPU %User,CPU %System,CPU %Idle,CPU %Wait,CPU %Stolen\n")

for line in iter(sys.stdin.readline, ""):
    if line[0] != 'p' and line[0:2] != ' r':
        t = time.strftime("%d/%m/%Y,%H:%M:%S", time.localtime(time.time()))
        line = ' '.join(line.split())
        line = line.replace(" ", ",")
        sys.stdout.write("%s,%s\n" % (t, line))
        sys.stdout.flush()
```

(Thanks to [fabrizoM](https://stackoverflow.com/q/4187785/146642) for the help!)

Run it from a shell script like so:

```bash
#!/bin/bash
vmstat 5 | python vmstat2csv.py >> servername-vmstat.log
```

Then start the job from the shell, press CTRL+Z and `nohup` it (so it doesn’
die if you disconnect) and tail it (so you can keep an eye on it) like so:

```shell
[1]+  Stopped                 ./log.sh
[gaz@box ~]$ bg
[1]+ ./log.sh &amp;
[gaz@box ~]$ disown
[gaz@box ~]$ tail -f servername-vmstat.log
Date,Time,Proc Run,Proc sleep,Mem swap use,Mem free,Mem buffered,Mem Cache,Swap in,Swap out,Blocks in,Blocks out,Interrupts,Context switches,CPU %User,CPU %System,CPU %Idle,CPU %Wait,CPU %Stolen
23/11/2010,12:59:47,1,0,0,1266452,465576,2074012,0,0,2,15,0,36,0,0,99,0,0
23/11/2010,13:00:11,0,0,0,1264460,465584,2074024,0,0,0,168,581,577,1,1,94,4,0
```
