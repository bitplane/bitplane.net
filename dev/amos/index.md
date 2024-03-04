# AMOS BASIC

AMOS was the Amiga port of STOS, a BASIC for the Atari ST written in assembly
language by François Lionet. Not just a procedural programming language, but a 
batteries-included IDE that supported the emerging multimedia pipelines of the
day - Deluxe Paint as a pixel painter and animation tool, and the array of
audio editors and trackers, and later on even supported 3D graphics created by
the likes of Imagine 3D.

![AMOS - The Creator](AMOS.png)

Back in 1993 I'd saved up my paper round wages, pooled birthday and Christmas
money, sold my ZX Spectrum and got my hands on an Amiga 500+ and a portable
colour TV. My high school years were defined not just by playing pirated games
shared by the one guy in school who's dad had BBS access, but by creating them
in AMOS and sharing them too. Not that anyone wanted to play them - they were
shit.

## Ramblings about multimedia

The 90s were a beautiful time for multimedia. Moving from a time where hard
drives were an expensive luxury, low bandwidth cassette tape and low capacity
floppy disks ruled the day. Then the CD-ROM came along with 800 times as much
space, we went from an era of extreme resource constraints to one of egregious
bloat and wastefulness. 

In the good old days graphics and audio weren't just created, they were
engineered. You'd carefully craft the palette as well as paint the pixels,
knowing that 16 colours looked naff, 64 were painfully slow, and 32 needed some
tricks to make things fast enough. You could swap the colours out in realtime
very quickly - abuse duplicate colours and swap them out for animation effects
as the electron beam scanned down each line. Compression mattered, bytes were
counted, sizes aligned to hardware widths, you had to keep ahead of the scan
line when filling the graphics card's output memory or you'd get tearing, lest
take the speed and RAM hit of double-buffering. Apparently the reason BMP files
are upside down is because a subtraction operation took less cycles than an
addition.

Audio was similar, chip tune was standard. You couldn't just record into a mic
at 11khz mono and get 30 seconds of audio on a floppy disk; you want a couple
of tunes in your game. So instruments would be crafted by breaking them up into
start, loop, end, and pitch shifted on the fly by banging the metal, interleaved
to fake more than 2 channels, and the snare drum would take up more space than
everything else combined.

Then the CD came along and the public were wowed by the voice acting and full
motion video, while we looked on in utter disgust.

## Some projects

I don't think I can switch my old A1200 on anymore, so some of this may be lost
to time. And older stuff from before I had a hard drive might be on rotten
floppy disks. They means I can pretend that they were all finished and polished,
which they mostly weren't.

* Mega Battler - an AD&D style text-based fighting tool, with character classes
  and different weapons. You'd basically set it up and it'd tell you what was
  going on, randomly selecting nouns and verbs to add texture to what was
  essentially just a bunch of dice rolls and calculations.
* Viking Tester - John, Graeme (and I think Craig for a bit) were members of
  [Regia Anglorum](https://regia.org/), a mediaeval reenactment society where
  we cosplayed as viking peasants. We made our own authentic, ill-fitting
  tunics and trousers from itchy woolen blankets, "Cornish Pastie" shoes out of
  leather, and spent every other weekend beating the shit out of each other
  with blunted spears and scramseaxes. Occasionally we'd do public displays and
  had to memorize basic Old Norse words to do with battle, this educational
  tool was an effort by John and I to memorize as much of it as we could. In
  hindsight, the only thing I remember is phalanx-esque march of "TROTHA... OI!"
* QAB - A Galaga type game with a sprite-swapping twist that we don't talk
  about in this day and age for fear of being cancelled on grounds of homophobia
  and crassness. We were kids though, it was funny at the time.
* Thrusts - A 3 player game that just wasn't fast enough to be the Gravity Force
  2 that we wanted it to be. Matt and Jay Benson made the sprites I think.
* Eggit - A Dizzy-remake starring an old friend, Stephen Edgar (R.I.P.). In a
  similarly tragic vein, we also made a single level of a game "Nuts, Andrew
  Hazelnuts", starring self-confessed nut-case Andrew Hazeldon, who also died
  in a car crash in early adulthood.
* Matchstick Man - Crap graphics, single player, made entirely by me. But it's
  a game that I actually finished and it worked. I was really proud of it at
  the time.
* NSLE - The Benson Bros got their hands on a digital camera that took those
  mini VHS tapes, while Browney had a digitizer that, if used with a VHS player
  with enough heads to pause it without streaks, could actually capture stills
  from the video. So we made a Lethal Enforcers clone over the course of a
  couple of weekends. Black and white of course. And Jay took his shoes off
  between parts of the rolling animation and we didn't realise until after
  filming, had to draw it back on in DPaint.
* Circular GUI elements - I remember being introduced to Pythagoras's Theorem
  in an early algebra test, and realising it could be used to make circular
  collision detection. So I memorized the formula and used it to make a bunch
  of procedures that could be used to create circular buttons. Kinda weird
  and nerdy memorizing a maths test rather than things for a maths test, but
  guilty as charged.
* The Ultimate Adventure - A remake of my ZX Spectrum text adventure, done in
  the style of The Secret of Monkey Island. Never finished it because, while
  all the code was there, actually creating content requires a pipeline and
  artists and is extremely hard work. And that's not the fun bit if you're a
  programmer.
* Scrawler - Jimmy White's Whirlwind Snooker had this cool effect where it
  drew letters on the screen as if someone was drawing them by hand. So I
  made a tool that would record and play them back.
