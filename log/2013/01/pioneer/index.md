# xorshitter

Over Christmas in 2012 I was playing with Pioneer, a space simulator based on
Frontier: Elite II, which I was a huge fan of on the Amiga. The game, written
in C++, was running pretty slow, and a bit of testing revealed they were using
a secure random number generator. So I ripped out the code and replaced it with
an xorshift generator, 17 times faster than the existing implementation:

* [merge request](https://github.com/pioneerspacesim/pioneer/pull/1893)

And all was good. For a while. Then weird bugs started to show up. It turns out
that xorshift generators are blazingly fast but they tend to get stuck on 0
inputs, and in a game made of procedural content where where everything relies
on the state of the RNG, you hit that a lot more frequently than you ought to.

I was pretty proud of myself at the time, but looking back at it the change was
high risk, needed a hell of a lot more tests and input from someone with real
expertise in that area, rather than a lay-hacker with a hard-on for performance
gains.

Oh well, you live and learn. Or you live at least.

