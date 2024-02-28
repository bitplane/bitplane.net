# Irrlicht TAR Loader

[source](https://sourceforge.net/p/irrlicht/code/HEAD/tree/trunk/source/Irrlicht/CTarReader.cpp)

IFileSystem changes:

* Added TAR archive loader.
* Renamed the following functions-
  `IFileArchive::getArchiveType` to `getType`
  `IFileSystem::registerFileArchive` to `addFileArchive`
  `IFileSystem::unregisterFileArchive` to `removeFileArchive`
  `IFileArchive::openFile` to `createAndOpenFile`
* New enum, `E_FILE_ARCHIVE_TYPE`. `getType` on `IArchiveLoader` and
  `IFileArchive` now both return this.
* `IFileSystem::addFileArchive` takes a parameter to specify the archive type
  rather always using the file extension. `IFileSystem::addZipFileArchive`,
  `addFolderFileArchive` and `addPakFileArchive` now use this but these
  functions are now marked as deprecated. Users should now use `addFileArchive`
  instead.
