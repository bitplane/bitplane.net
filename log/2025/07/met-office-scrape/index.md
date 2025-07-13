# ⛅ Met Office Scrape

While writing my article about [Truth](/~/doc/thoughts/lens/truth), I found
myself researching the exact weather on Sean Connery's birthday, and ended up
deep in the Met Office's library looking for an image to illustrate the text.

It turns out that when they say it's "the hottest summer since records began",
the records they're talking about are those of the UK Met Office (not to be
confused with the Royal Meteorological Society), which has been collecting
official data for the UK government since the 1850s. Poking around in the
archives, I realised that the library wasn't archived on archive.org, due in
part to the hosting choices. Access is possible over the web but bulk downloads
require an API key, so it isn't accessible in an open and permissionless way.

So I set about fixing that.

3 months later, during the third heatwave of 2025, I'm happy to say that the
Met Office library is finally
[hosted on archive.org](https://archive.org/details/@gareth_davidson/lists/2/uk-met-office-library).

## Code

The library itself is about 1.5TB of data, containing PDFs 20x larger than is
reasonable. It also contained hundreds of thousands of files. I managed to
shave almost a terrabyte off that.

To download the data, I wrote
[this custom scraper](https://github.com/bitplane/met-office-scrape).

Once that was done, I built some scripts for my
[rip](https://github.com/bitplane/rip) project, one to extract PDFs that are
made of huge TIFF files, recompress to webm and `tar` them - making them 20x
smaller. I ran this on [vast.ai](https://vast.ai) over a weekend, which is
the source of most of the space saving.

Another script bundles huge dirs into tar files, so it's easy to upload and
process. Both of these scripts can be found in rip's `./scrip` dir (not a typo).
It is, of course, WTFPL licensed like everything but the data.

The side project caused MediaInfo to get webm support, which in turn caused
EXIF to be split out, data was shared, philosophy written, uploaders honed, and
keeping the rip project alive led to a generic FUSE mounting system (`qemount`),
an embeddable 9p server, and a user-space
[block device cache](/dev/python/blkcache) built and tested.

I'll write about `rip` itself and these tools once I've finished battle testing
it, have added scrapers and DVD/CD repair without manual intervention, and a
nice TUI that isn't just tmux with 6 panels open. 

Currently though, the data is live and the job seems complete. Hopefully I didn't
damage too much during the experiment! Go have a look, the data is ours now :)
