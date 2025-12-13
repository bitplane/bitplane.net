# 🖌️ Procedural Texture Toolkit

* [🐱 github](https://github.com/bitplane/proctex)

Procedural textures save storage space by saving the instructions of how to
create a texture rather than the raw texture data itself. Using this method you
can create hundreds of megabytes of textures from just a couple of kilobytes of
data.

Of course, this comes at a cost. Firstly the textures can't just be dumped into
memory - they take a long time to load because they must be created before being
used. Secondly you have to use a special editor that looks and acts nothing like
Photoshop or GIMP, and your artists need to learn how to use it.

This isn't supposed to compete with demoscene procedural texture tools like
.werkkzeug, as Irrlicht takes up about half a megabyte of space anyway.

## Using the Generator

Link all the files in `/generator/` and create an instance of
`CProceduralTextureGenerator`. You can then load texture and project files
created by the editor.

To load a texture from a project simply use:

```cpp
driver->getTexture("project.proctex#texturename");
```

The first time a project file is accessed like this every texture from the
project will be added to the texture cache, which may take some time.

Procedural textures only work with the hardware drivers at present, so you can't
use them in software mode (yet).

## Credits

* ATI RenderMonkey - lots of useful shaders
* .theprodukkt - inspiration
