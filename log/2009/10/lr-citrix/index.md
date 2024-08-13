# Stripping snapshot files from LoadRunner Citrix scripts

After several re-records of a Citrix script in LoadRunner, thousands of PNG
snapshot files build up in the data dir. Over time they can build up to make
your script eat up over a hundred megabytes of disk space, which is a little
excessive given that the useful parts are only a few megs in total.

These snapshots are used to make the script tree-view useful, so you can’t
delete all of them in case you need a reference image when inserting a new sync,
keypress or some other event. So, I squirted out this little VB script which
will remove unused stuff from the data directory, I’m sharing it with the
Internet because I’m nice like that.

You can download it
[here](/dev/vb/loadrunner-citrix/strip_loadrunner_citrix_script.vbs).

To run it, just copy to the dir which contains your scripts (back them up first,
I offer no warranty or compensation in case things go wrong) and click it. Be
prepared to wait a long time, enumerating forty thousand bitmaps will always
take some time.

When archiving your scripts you might also want to delete any results data,
which also costs a few megs
