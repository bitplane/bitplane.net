# Fix WayBack machine zips

Way back when, there was an Internet Archive issue where zip files that were
downloaded were missing a single byte off the end. This made them impossible
to open in WinZip/WinRAR.

So this little C tool just adds a byte on the end. If I remember correctly
that's what it does anyway.

[download](fix_wayback_zips.zip)
