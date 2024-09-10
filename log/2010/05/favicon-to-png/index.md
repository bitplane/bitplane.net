# Automatic favicon to PNG script

Ever want to add a link to a site with the favourites icon in the page along
with the link? I did, so I made this cool little toy:

![ico](bitplane.net.png) http://favicon.bitplane.net/

The site looks like nothing more than a directory filled with icons in PNG
format, but it actually uses an Apache directive to make sure that every file
served is sent back with the image/png mimetype, and the HTTP 404 error page
points to a script:

```text
ErrorDocument 404 /.downloader/404.php
ForceType image/png
```

404.php page actually downloads the favicon from a remote site and converts it
to PNG format.

I’ve removed the out-of-date code from here, you can get the latest code over on
[GitHub](https://github.com/bitplane/)
