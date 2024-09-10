
# Yet another Glastonbury ticket fiasco

Once again we have tickets for Glastonbury Festival, and once again there’s
well-founded accusations of foul play as technical festivalgoers barged through
SeeTickets’s queues to the booking pages, and once again I’m not complaining.

Why did it suck, and how did everyone get around it?

Knowing that their IIS 7.5 servers (both of them) couldn’t hold up under the
load of 2 million people hitting F5 every few seconds, See did a “clever” thing
with their DNS servers and set them to periodically return a 192.168 address for
their booking page. This IP address gets saved on the user’s DNS resolver cache
and effectively bans that computer from contacting the booking page until the
DNS time-to-live has expired; you’re attempting to contact a machine on your own
local network and no matter how furiously you hit refresh you aren’t causing See
any damage. While you’re requesting a connection to a non-existent
192.168.202.201/202 the real servers at 194.168.202.201/202 (sneaky eh?) are not
collapsing under the load. Crude, but effective.

There were complaints in 2010 that the system wasn’t fair, people who got in
once could go back and register more people. The lucky winners with the right
address in their cache could gorge themselves on orders until all the tickets
ran out, larger groups who were more likely to have a winner got tickets while
the smaller groups lost out. This also meant that if your company’s corporate
proxy servers won the DNS lottery then everyone in your company could get a
ticket. Like every year, much butthurt was caused by this unfair selection
process.

This year See took the infinitely wise decision to “fix” this by decreasing
their DNS TTL to 60 seconds. So to get a ticket legitimately you’d have to
either complete the entire three-stage booking process in under 60 seconds, or
win the DNS lottery several times in a row. Good luck with that, humans!

Those in the know just edited their hosts file to point
glastonbury.seetickets.com to the correct IP, and as soon as
[eFestivals announced this to the world](https://twitter.com/eFestivals/status/254860841168560129)
’201 slowed to a crawl as thousands of queue-bargers found their way over the
barriers and bought around 60,000 tickets in under 20 minutes. Once again,
[it sold out in record time](https://twitter.com/GlastoFest/status/254879887381385216/photo/1).

Can’t wait to see what they come up with for the resale!
