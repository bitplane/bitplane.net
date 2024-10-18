# ONBUILD COPY . /var/www/pwned/

All good titles should contain context. This one goes the extra mile and
broadcasts it too!

If you didn't have enough good reasons to never build and push from your
local repo, here's another:

A Dockerfile's `ONBUILD` lines are executed when building containers that depend
on it.

This means a rogue Docker image isn't just a runtime risk to all of its
downstream dependencies, it can ransack *your* build dir while you're building
it, adding files that aren't in your `.dockerignore` to the image that you then
publish, and it can serve them back to the attacker.

That sort of deliberate attack is quite unlikely, but it opens the avenue to
accidental leaks too.  Unless you're sure you've ignored everything important,
building locally could expose your .env files, .git/config, core dumps, log
files, and that customers.dat~ file you were messing with too.

🌈⭐