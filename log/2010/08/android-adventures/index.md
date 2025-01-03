# 📱 Adventures in Android

Since getting myself a Google Nexus One I've decided to do a bit of Android
development. My first impressions with the platform weren’t really that
good, but I’m beginning to get the hang of it now.

My main problem is that Java is a horribly verbose and restrictive language.
To do the simplest things you need to implement at least three interfaces and
extend a couple of abstract classes (after reading the documentation for each
of them and their alternatives of course). Something which could be written in
Python in three lines of code and two minutes takes fifty lines and twenty
minutes in Java. Perhaps that’s just me, maybe I’ve been spoiled by dynamic
languages and expect to be able to do things a hundred different ways by just
typing whatever comes to mind, rather than carefully considering the available
options and planning every step of my app. In my short journey through Java
development I've suffered a lot of pain because I make assumptions and choose a
design pattern which is incompatible some point later down the line, so I end up
refactoring everything ten times before I even get a working prototype. I'm
slowly learning not to fly by the seat of my pants (even if it is the most fun
way to fly) and perhaps that’s a good thing.

My other gripe is the UI editor and XML format, their steep learning curve makes
the design stage a huge time sink. I’ve now spent a fair bit of time banging my
head off my keyboard while attempting to make the simplest of interface, which
still don’t look like they do on paper, but I think I’m getting the hang of it.

Anyhow, so far I’ve managed to knock out 3 applications which are available in
the Android marketplace:

## Anonypic

This little app just adds an extra option to your share menu, and will upload an
image to bayimg.com, the anonymous image sharing service by the creators of The
Pirate Bay. Images have their EXIF data removed, so you can share images without
leaving a trail of metadata leading back to your phone.

## Rainwatch

Rainwatch is an alternative viewer for the BBC’s Maps Presenter, the Flash
application available on their weather site. It’s far from complete but is good
enough to predict the weather, so I’m quite happy with it (as are my 1500 active
users)

## MC Mail

MC Mail, or Missed Call Mailer is a little app which sends you an email when
you get a missed call. The back-end is written in PHP and MySQL, the front-end
is mostly just a service which monitors your call log. Useful if you're a
hospital or call centre worker who has access to email but can’t use a phone in
work, or if you always forget your phone. It usually only works while the phone
is in silent mode.

## Next steps?

I'll make a couple more apps and maybe a game, then learn the Native Development
Kit and port Irrlicht using Christian’s OpenGL ES driver. I haven’t done any
Irrlicht code in ages, so that's certainly on the agenda.

