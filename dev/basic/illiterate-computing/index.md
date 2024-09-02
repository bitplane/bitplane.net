# INKEY$ and his 8 legs

The Speccy's crude operating system was a BASIC command line interpreter
complimented by a simple line editor, booted into in about a second when the
machine was switched on. Well, to be more accurate, when you plugged it in, as
extravagant luxuries like an on/off switch had no place in Sinclair's quest for
affordable home computing.

Budget home computers of the 80s outsourced their peripherals to existing
consumer electronics. Connecting to the family TV with a coax cable was cheaper
than buying an expensive digital monitor, and games played into the MIC port
from a radio cassette player's headphone socket.

The main reason to buy a home computer was to play games, but the reason people
made computers was to bring the glory of computing to the home. So, gaming was
both a killer app and secondary function, and this conflict meant that in order
to load a game you'd need to instruct the thing to actually do the loading.

This meant running the `LOAD` keyword from the machine's CLI, and like the rest
of the ZX Spectrum's budget quirks, it was different and famously awkward. Short
on space and long on ideas, the boffins at Nine Tiles decided that their BASIC
interpreter could do without a lexical parser so assigned all their possible
functions to their extended character set, characters 0xA5 to 0xFF being entire
words rather than a symbol. To input them, the text cursor switched between
modes depending on context, a flashing `K` for keyword input, an `L` for letters
and so on. The budget rubber keyboard had all the commands printed on it, so to
load a game you'd find and tap the key with the word `LOAD` on it:

![keyboard](zx-buttons.webp)

If you didn't spot it, `LOAD` was *conveniently* located on the J key. But that
wasn't enough to load a game, nope, you also had to pass the name of the program
to load. Not that anyone actually used this name filter, as that'd mean sitting
there for 4 minutes listening to some other program's memory dump; I like to
think it was a psyop by Steve Vickers to teach programming by stealth. It
probably wasn't, but it certainly worked that way.

If, like everyone, you didn't know or care about the name of the program then
you entered an empty string, a pair of empty double quotes. These, even more
conveniently than `LOAD`, were input by holding down the aptly named
`SYMBOL SHIFT` key squishing the P key down twice. Then you pressed `ENTER` and
clunked down the play mechanism on your cassette player. If the tape
wasn't too worn or too stretched and hadn't got too hot or too damp, it wasn't
wound too tight, and wasn't an 8th generation copy borne of a chain of people's
mums' Hi-Speed Dubbing dual cassette deck radio players, and impatient kids
didn't shock the tape heads by jumping about the room or squabbling too roughly
then your game would be ready to play in 3-4 minutes, which felt like a whole
day.

This ritual was performed each time you loaded one of the many (excellent)
games, but the flashing cursor and looming 4 minute eternity invited kids to
play with the other keys. If you pressed the P key it typed `PRINT`, and if you
put some letters between the quotes after it then it'd whatever you wrote to the
screen (in CAPS, because the CAPS SHIFT key was for exotic and alien
lower-case). If you wanted some real fun, you could put a number before the
keyword and it'd get saved to one of the 9,999 available line numbers rather
than being executed. Then you'd run them in line-order with the R key, or
`GOTO` one of them with the G key. So we did.

```basic
10 PRINT "HELLO"
20 GOTO 10
```

That's how I became an illiterate programmer. I couldn't spell `LOAD` or `CLEAR`
on my own at the age of 6, even `BEEP` was spelled strangely, but it made music
if you gave it some numbers.

If you wanted to take a key from the keyboard without waiting for someone to
`ENTER` it, so you could move `▄█▄` around the bottom of the screen then you'd
use the `INKEY$` keyword to save it to a variable, or a "little box"; input key,
dollar meaning it returns a string. If you're 6 years old, don't know what
"input" means and call your keys "buttons" then `INKEY$` conjures up images of a
friendly octopus with his arms all over your buttons catching the ones you
press. Well, legs actually, because only humans have arms.

And that's how I became a programmer, it's how a lot of kids became one. Sir
Clive earned his knighthood ten times over by creating a generation of
programmers who were learning to read and write, and we went on to
[transform the world](https://youtu.be/IagZIM9MtLo). To me, and me alone it
seems, `INKEY$` is a friendly cartoon octopus living on 4 inches of
thin card with SEE INLAY FOR DETAILS written along one side. Ah.. memories!
