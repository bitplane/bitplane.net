# Irrlicht 1.5.1 Released

Yesterday we released [Irrlicht 1.5.1](https://irrlicht.sf.net/). This will be
the last 1.5.x release, development is now focused on 1.6 which will move to its
own branch over the next week or so and become stable.

Changes in 1.5.1:

```
- Make sure a missing font does not corrupt the skin.
- Fix getAngle in vector2d as suggested by xray.
  This has only a minor impact on s32 vectors.
- bugfix: CGUIFont::getCharacterFromPos regards now kerning
  (found by Arras)
- Add support for range fog in some OpenGL versions.
- Fix for shadow volume removal, submitted by vitek.
- Avoid using X11 autorepeat to deal with broken X11
  versions.
- Speculars are properly exported into mtl files now,
  instead of corrupting them.
- Binary type loading in attributes fixed.
- bugfix: Use make_lower throughout for spritebank filenames
  (found and patched by Ion Dune)
- STL loader fixed: Right-handedness corrected, normals and
  bboxes are correctly added now.
- bugfix: CUnZipReader::openFile no longer returns true for
  empty files. Corresponding test added.
- Big endian issues in .x loader fixed.
- HSLColor methods repaired.
- copyToScaling fixed.
- Fixed problem with highlighting menus when mouse was
  outside sub-menu area.
- bugfix (2796207): menu acted (wrongly) on left-click down
  instead of left-click up.
- bswap16 fallback macro fixed
- getBaseName fixed to work correct with dots in filenames.
- static method isDriverSupported allows for simple
  check of available drivers.
- Some defines added to check for the Irrlicht version of
  the library.
- Make sure all renderstates are properly initialized
- Wrong size for main depth buffer fixed.
- Fix 3ds shininess to the allowed range.
- Fix loading of Collada files from irrEdit 1.2
- Remove texture pointers after texture clear.
- WindowsCE pathnames fixed.
- Some virtuals are now overridden as expected.
- Incomplete FBOs are properly signalled now
- Update to libpng 1.2.35, fixed issues on 64bit machines
  with system's libpng.
- Fixed wrong grab/drop in setOverrideFont
- Added draw2dRectOutline
- rectf and recti added.
- Fix ALPHA_CHANNEL_REF to a fixed check for alpha==127 as
  expected.
- Fixed OSX device bug where screen size was not set in
  fullscreen mode.
- cursor setVisible changed to be called less often.
- OpenGL version calculation fixed.
- OSX device now supports shift and ctrl keys.
- Fixed ambient light issues in burningsvideo.
- device reset for d3d fixed when using VBOs.
- Fix dimension2d +=
- MD2 mesh loader: Now uses much less memory,
  reduced number of allocations when loading meshes.
- OpenGL render state (texture wrongly cached) fixed.
- Fixed animator removal.
- Changed collision checks for children of invisible
  elements to also be ignored (as they're actually
  invisible due to inheritance).
- Fix terrain to use 32bit only when necessary, make
  terrain use hw buffers. Heightmap loading and height
  calculation fixed. Visibility and LOD calculations updated.
- Some mem leaks fixed
- FPS camera resets the cursor better
```
