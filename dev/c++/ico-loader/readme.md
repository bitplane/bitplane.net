# .ico and .cur loader

Loads Windows icons and cursors in a cross-platform way for Irrlicht
Engine graphics apps/games.

Download: [CIcoLoader.zip](CIcoLoader.zip)

Source online:

[link](https://sourceforge.net/p/irrext/code/HEAD/tree/trunk/extensions/io/IArchiveLoader/ICO/)

## Docs

```txt
-----------------------------------------------------------------
           Irrlicht .ICO & .CUR archive loader v1.0
                    (c) Gaz Davidson 2009
-----------------------------------------------------------------
1. Introduction
-----------------------------------------------------------------

This is an ICO/CUR file loader, implemented as an archive loader 
for the Irrlicht Engine 1.6 and above. 

After adding this loader to the filesystem you can add a Windows
icon (*.ico) or cursor (*.cur) to the filesystem like opening a
zip file. This will add a list of TGA and PNG files to the VFS.

The file names are in the format: "%s.%d.%d.%s", name, i, ext
where: 
  name is the name of the archive
  i is the index of the icon
  ext is the file extension (either TGA or PNG)

The TGA files are converted from BMP/ICO format with a separate
alpha channel, you need the TGA writer, plus the BMP and PNG 
loaders to be able to read icons in all ICO files.

-----------------------------------------------------------------
2. Example
-----------------------------------------------------------------

/*
  Windows users:
    Copy the directory to Irrlicht's examples dir, double click 
    the VC9 project file, compile and run.

  Linux users:
    The makefile assumes Irrlicht 1.6 is installed as a shared 
    object. To do this, cd to Irrlicht's source dir and type:
    
    make clean
    make sharedlib
    sudo make install

    Then return to this directory and type make.
*/

// create an instance of the loader 
io::CArchiveLoaderICO* icoLoader = 
  new io::CArchiveLoaderICO(fs, driver);

// add it to the filesystem
fs->addArchiveLoader(icoLoader);

// we created it with new, so we must drop it.
icoLoader->drop();

// now we can add an .ICO archive to the filesystem
fs->addFileArchive("bitplane.ico");

// and load an icon from it
video::ITexture* tex = driver->getTexture("bitplane.ico.2.tga");

-----------------------------------------------------------------
3. Credits
-----------------------------------------------------------------

Written by Gaz Davidson (gaz@bitplane.net)

Thanks to Wikipedia's page on icons for documenting the file
format.

Thanks to GIMP's icon loader plugin source code, which was used
as a reference rather than copied, as I didn't want to adhere to
the GPL. Thanks to the guys in #GIMP for pointing me in the right
direction.

Thanks to www.axialis.com, where I stole SamplePNG.ico from. You
don't have permission to use this icon!

And of course thanks to the rest of the Irrlicht dev team, this
code sits on top of Irrlicht.

-----------------------------------------------------------------
4. License
-----------------------------------------------------------------

Copyright (c) 2009 Gaz Davidson

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
```
