# JPerfmeter crashes while starting

I’ve been us [JPerfmeter](https://jperfmeter.sourceforge.net/) in work to keep
an eye on Linux system counters served up over rstatd.

However, it has one very annoying bug:

If one of your servers goes offline, or it somehow lets you add a server which
doesn’t exist JPerfmeter will crash and refuse to start again. The setting is
saved somewhere on disk. Where? Google didn’t know (hence this blog post).

Half an hour of messing around in Procmon going through reams of logs and I find
the settings in %userprofile%\JPerfmeter, just where you’d expect them to be.
facepalm.jpg
