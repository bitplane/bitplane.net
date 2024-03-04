# mIRC Script

A cynical take on mIRC's early 2000s glory days might be all about the warez,
the trojans and the drama, and that'd be largely correct. We had blatent
disregard for copyright law, completely vulnerable unfirewalled systems
connected directly to the internet by dial-up modem, and kids being dicks
to each other. Though another framing would be the empowerment of personal
automation in a social network that valued privacy, robustness and comradery;
popularity contests and bitter disputes aside.

Back in those days I used to run an eBook server on DalNet, `bitplane` was the
name of my alt account and bot. It ran a custom script that featured automatic
syncing of files between other servers, persistent queues and requeueing of
failed user-downloads, automatic leeching from peers and rivals, chat between
connected users, channel operator automation that rivaled the best eggies, a
search engine, the ability to browse and download files inside ZIP and RAR
archives, automatic file renaming and sorting, plus a ton of long forgotten
features, added as and when needed by myself or others.

Unfortunately that was lost in a hard drive crash, and all that remains of
bitplane is this handle. Another thing lost includes a suite of aggressive
antivirus scripts that hacked back into exploited users, removed the trojans
and left a note on their desktop to be more careful with downloads - we saw
the botnet spam as a personal insult.

Somehow this was all written in mIRC script, which looks simple on its face
but is actually an incredibly robust procedural language in the style of TCL
that served as my first introduction to event-driven programming, TCP sockets
and hash tables.

The only thing I have that I wrote back then was this fserver leech script,
which logs on to shell-style file servers, issues commands to change
directories and re-enqueues downloads, to leech entire directories of files -
which is what you want if you're downloading albums or directories full of
text files. Of course modern Windows detects this as a trojan, which it
isn't.

So here it is, one for the archives:

* [leechfserver015a.zip](leechfserver015a.zip)

