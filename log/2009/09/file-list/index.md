# PHP file list using mod_rewrite

I've noticed that most of the traffic to this site is actually people visiting
my permanent and temporary file dumps, which until today were literally a bunch
of files dumped in a folder. DreamHost don't keep my logs for over 30 days and
I'd like to incorporate my file dumps into my Piwik stats, so I made a nice
fancy file list in PHP. It has nice looking icons courtesy of famfamfam, though
may move to stdicon in the future.

Some caveats:

The file list currently tracks directory views (via the template) but not yet
file downloads, as that requires a Piwik plugin that isn't final so I haven't
installed it, adding it should be trivial though.

As requests are passed through PHP using mod_rewrite it will result in long
running scripts on your server, which may upset your shared web hosting provider.

Scripts are not yet excluded by rewrite rules! You won't want to keep other
scripts containing sensitive information in dirs under the path.

Access to files and folders beginning with “.” will be blocked.

It only works on Unices, not Windows servers as they don't have the `file`
command to get the MIME type.

You'll obviously need an Apache installation with mod_rewrite.

To install it, just copy index.php, .htaccess and .filelist/ to the directory
where you store your files. You can get the script (without icons) 
[here](/dev/php/file-list)