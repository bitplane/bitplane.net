# C++

C++ gets a lot of flack, and there's good reasons for it. But despite its
dispatch, dreaded diamond and SOLIDesque flaws, it was popular enough to have
decent debugging tools for a lot of its life, making it as useful as it is
dangerous.

I got into C++ by writing games for Nikolaus Gebhardt's Irrlicht Engine, an open
source 3D library for the fixed-function graphics pipeline that abstracts the
rendering back-end and operating system away, making it perfect for cross
platform, device agnostic games programming.

So most of my C++ work is stuff done for Irrlicht, which I was on the dev team
for several years - until I gave up on the idea of writing games and moved on to
more boring, real things.

## Not Irrlicht

* 🌇 [webp support for mediainfo](webp)
* 🚀 [Pioneer](log/2013/01/pioneer)

## Games

Some games, none of any note.

* 👾 [irrvaders](irrvaders) -
  A space invaders game with a cylindrical coordinate system.
* 🚀 [jetpac](jetpac) -
  A remake of JetPac.
* 🔥 [jump or burn](jumporburn) -
  Ridiculously crap game made for a gaming contest.
* 💥 [mines](mines) -
  Minesweeper game.

### Unifinished

* 👽 [UFO game](ufo-game) -
  A game that Graeme and I wanted to make, in the style of Star Fox 64.
* ✝ [Monotheism](monotheism) -
  A game I wanted to make, but, got distracted making other things.

## Irrlicht Scene Nodes

Things that make your world pretty

* 🧑‍🔧 [axial-billboards](axial-billboards) -
  Axis aligned billboards, like Mariokart on the SNES.
* 📦 [batching-mesh](batching-mesh) -
  A mesh that batches its children, so you can use fewer render calls.
* ⚡ [beam-scene-node](beam-scene-node) -
* A screen-aligned beam effect. Basically a rod with a billboard on each end.
* ☁️ [clouds](clouds) -
  Clouds with recursive levels of detail.
* ☘️ [grass](grass) -
  A grass patch scene node, used in a few popular games.
* 🕵️ [impostors](impostors) -
  Distant items become billboards, making enormous scenes possible.
* 🪴 [plantlod](plantlod) -
  A quad tree to render loads of stuff, loaded from disk and culled depending
  on distance.
* 🌍 [spheremap renderer](spheremap-renderer) -
  Render the scene into a spheremap, for use in lighting effects.
* 🖼️ [skybox renderer](skybox) -
  Render your scene into a sky box. Same as above, but for performance reasons.
* 🫠 [mesh deformation](deform) - 
  Example of deforming 3D meshes.

## Tools

* 👍 [3d mesh thumbnailer](thumbnailer) -
  A Gnome thumbnailer for 3D mesh file formats.
* 🔡 [font generator](font-generator) -
  The cross platform Irrlicht font generator.
* 🖊️ [GUI Editor](gui) -
  The GUI editor for Irrlicht.

## Irrlicht Loaders and Internals

* 🔠 [figlet driver](figlet-driver) -
  Loading figlet fonts on the console device, or wherever.
* 🤖 [console device](console-device) -
  Created as a null device, became an ASCII device for software drivers
* 🖼️ [ico-loader](ico-loader) -
  Load Windows icon and cursor files in your Irrlicht app.
* 📉 [loader profiler](loader-profiler) -
  Profile the various loaders for the Irrlicht Engine.
* 💾 [ply loader](ply-loader) -
  A loader for Stanford Polygon with blistering performance due to ugly hacks.
* 🪟 [rsrc-loader](rsrc-loader) -
  Load resources from Windows DLL and EXE files.
