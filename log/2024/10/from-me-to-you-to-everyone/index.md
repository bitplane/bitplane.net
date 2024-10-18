# ONBUILD COPY . /var/www/pwned/

Titles should contain context, this one goes the extra mile and broadcasts it
too!

Careful where your images are `FROM`, you might end up serving your .env files,
.git/config, core dumps, log files, that customers.dat~ file you were messing
with.

Unless you're sure your `.dockerignore` is absolute perfection, you might want
to make a habit of never building and pushing from your local repo, just to be
safe.
