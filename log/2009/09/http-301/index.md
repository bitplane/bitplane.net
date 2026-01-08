# This [e107] page has moved permanently [to gallery2]

If you do a Google search for some of my really old code, like my
[Python T9 Dictionary](/dev/python/t9) or
[XBMC IRC MP3 downloader](/dev/python/xbmc/irc), you’ll notice that my pagerank
has been carried over to SVN and the
[gallery](https://web.archive.org/web/20091207064353/http://gallery.bitplane.net/).
This is because Google and other search engines take note of HTTP 301 response
codes and update their links accordingly.

When I migrated from e107 to WordPress and Gallery2, I replaced download.php with a redirect script which redirects to the gallery, svn or file dumps. The script looks like this:

```php
<?php
// lots excluded
$table['4']='http://svn.bitplane.net/misc/trunk/py/py9/readme.txt';
$address = 'http://bitplane.net/';
 
foreach ($_GET as $i => $value)
{
  $index = explode('_', $i);
  if ( isset($index[1]) && isset( $table[ $index[1] ]) )
  {
    $address = $table[ $index[1] ];
  }
}
 
// send 301 (permanent redirect)
header("HTTP/1.1 301 Moved Permanently");
header("Location: " . $address );
?>
<html><head></head><body>
This file has permanently moved <a href="<? echo $address; ?>">here</a>
</body></html>
```

So when you try to view PY9, you’re redirected to the new location. There’s no
excuse for 404 errors when you move your site around, if you care about keeping
the web up-to-date then please use a redirect script!
