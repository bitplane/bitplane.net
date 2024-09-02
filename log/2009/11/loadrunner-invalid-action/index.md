# LoadRunner Controller – Invalid Action Window

LoadRunner 9.5′s VUGen sometimes gets its undergarments in a twist and messes up
the actions in one of its INI files. You don’t notice this until you get the
dreaded “Invalid Action” error message while running a test, which appears once
for each virtual user and prevents other users from loading.

Thankfully, [Sameh Abdelhamid](https://web.archive.org/web/20161020072117/http://mishmashmoo.com/blog/?p=12)
found and documented a proper fix for this problem:

> Find a file called default.usp and edit it in your favorite text editor. I use
> ScITE which comes with ruby. You will notice a parameter called [Profile
> Actions].
>
> That will list your actions. If you cross check this with the actions in your
> script you will notice that in my example, I only have 3 actions, whereas, the
> default.ups has 4.

Which is great, but no good for me *right now() as it started happening half way
into a test which I can’t cancel. If like me, you need that horrible, dirty,
reactive solution *right now*, here’s a little VB Script to send a Y key to the
messagebox every time it appears.

```vb
Dim Wsh
Set Wsh = Wscript.CreateObject("Wscript.Shell")
 
While True
  If Wsh.AppActivate("Invalid Action") Then
    Wsh.SendKeys "y"
    WScript.echo "go away!"
  End if
 
  WScript.Sleep 1000
Wend
```
