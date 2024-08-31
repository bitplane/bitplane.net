# Idea: UAC evil twin escalation

(Just an idea, I don't have time/inclination to actually do a proof of concept.)

Say you're an evil script or binary that has managed to run as a user, and you
want to elevate yourself.

1. `new_app` = Process list contains a new, unknown elevated application.
2. `screen_off` = Check the screen off timeout and compare with idle time.
3. `no_fg = GetForegroundWindow == NULL`
4. `screensaver = SystemParametersInfo(SPI_GETSCREENSAVERRUNNING ...`
5. If `new_app` and `no_fg`, but not `screen_off` or `screensaver`:
   1. Load the binary and extract metadata.
   2. Create a new binary in temp with the same name, but your own behaviour.
   3. Give it a couple of seconds, and request elevation for your own app.
6. If not elevated, GOTO 1

So the user gets a double UAC request and accepts it.

If it works, it works because it hides among the stream of frustration and nags
that define the Windows user experience; a hypodermic needle in a matted, second
hand haystack.
