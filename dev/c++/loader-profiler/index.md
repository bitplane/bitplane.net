# Loader profiler for Irrlicht

To use it, just create an instance of it and call attach(), it will be added
as a mesh, image, scene and archive loader that intercepts all load calls,
passes them to the correct loader while timing them, then outputs the result.

If nothing else, it's a good example of how to override a built-in loader
with your own :)

```c++
// Irrlicht loader profiler by gaz@bitplane.net
// requires Irrlicht 1.8 or above.


#include "IImageLoader.h"
#include "IMeshLoader.h"
#include "ISceneLoader.h"
#include "IFileArchive.h"
#include "path.h"

namespace irr 
{

// When added to Irrlicht as an external loader or writer, this class claims intercepts all calls 
// and puts timings around them.
class LoaderProfiler : public virtual video::IImageLoader, scene::IMeshLoader, scene::ISceneLoader, io::IArchiveLoader
{
	public: 

	LoaderProfiler(IrrlichtDevice* device=0) : Device(device)
	{
	}

	void attach() 
	{
		// register the interceptor.
		if (Device)
		{
			Device->getVideoDriver()->addExternalImageLoader(this);
			Device->getSceneManager()->addExternalMeshLoader(this);
			Device->getSceneManager()->addExternalSceneLoader(this);
			Device->getFileSystem()->addArchiveLoader(this);
		}
	}

	//! Used by all the loaders except archives, where this method is badly named.
	virtual bool isALoadableFileExtension(const io::path& filename) const 
	{
		// since we have no idea what it is we're loading, we have to check all loaders/writers.
		// since C++ sucks, we have to write this crap out many times.

		scene::ISceneManager* smgr  = Device->getSceneManager();
		video::IVideoDriver*  video = Device->getVideoDriver();

		s32 i;

		// image loaders
		i = video->getImageLoaderCount()-1;
		for (;i>=0; --i)
			if (video->getImageLoader(i) != this && 
			    video->getImageLoader(i)->isALoadableFileExtension(filename))
				return true;

		// mesh loaders
		i = smgr->getMeshLoaderCount()-1;
		for (;i>=0; --i)
			if (smgr->getMeshLoader(i) != this && 
			    smgr->getMeshLoader(i)->isALoadableFileExtension(filename))
				return true;

		// scene loaders
		i = smgr->getSceneLoaderCount()-1;
		for (;i>=0; --i)
			if (smgr->getSceneLoader(i) != this && 
			    smgr->getSceneLoader(i)->isALoadableFileExtension(filename))
				return true;

		// no match
		return false;
	}

	//! badly named! need to fix this at some point
	virtual bool isALoadableFileFormat(const io::path& filename) const 
	{
		io::IFileSystem* fs = Device->getFileSystem();
		// archive loaders
		s32 i = fs->getArchiveLoaderCount()-1;
		for (;i>=0; --i)
			if (fs->getArchiveLoader(i) != this && 
			    fs->getArchiveLoader(i)->isALoadableFileFormat(filename))
				return true;

		return false;
	}

	virtual bool isALoadableFileFormat(io::E_FILE_ARCHIVE_TYPE t) const
	{
		io::IFileSystem* fs = Device->getFileSystem();
		// archive loaders
		s32 i = fs->getArchiveLoaderCount()-1;
		for (;i>=0; --i)
			if (fs->getArchiveLoader(i) != this && 
			    fs->getArchiveLoader(i)->isALoadableFileFormat(t))
				return true;

		return false;
	}

	//! Used by all but mesh loaders
	virtual bool isALoadableFileFormat(io::IReadFile* file) const
	{
		// again, C++ sucks.

		scene::ISceneManager* smgr  = Device->getSceneManager();
		video::IVideoDriver*  video = Device->getVideoDriver();
		io::IFileSystem*      fs    = Device->getFileSystem();

		s32 i;

		// image loaders
		i = video->getImageLoaderCount()-1;
		for (;i>=0; --i)
			if (video->getImageLoader(i) != this && 
			    video->getImageLoader(i)->isALoadableFileFormat(file))
				return true;

		// scene loaders
		i = smgr->getSceneLoaderCount()-1;
		for (;i>=0; --i)
			if (smgr->getSceneLoader(i) != this && 
			    smgr->getSceneLoader(i)->isALoadableFileFormat(file))
				return true;

		// archive loaders
		i = fs->getArchiveLoaderCount()-1;
		for (;i>=0; --i)
			if (fs->getArchiveLoader(i) != this && 
			    fs->getArchiveLoader(i)->isALoadableFileFormat(file))
				return true;

		// no match
		return false;
	}


	//! Load an image, time it.
	virtual video::IImage* loadImage(io::IReadFile* file) const 
	{
		video::IImage* ret = 0;

		video::IVideoDriver* video = Device->getVideoDriver();

		u32 readTime=0;

		// find the correct loader
		for (s32 i=video->getImageLoaderCount()-1; !ret && i >= 0; --i)
			if (video->getImageLoader(i) != this &&
			    video->getImageLoader(i)->isALoadableFileFormat(file))
			{
				// attempt to open
				u32 readStart = Device->getTimer()->getRealTime();
				ret = video->getImageLoader(i)->loadImage(file);
				readTime = Device->getTimer()->getRealTime() - readStart;
			}

		if (ret)
			log(readTime, file->getFileName());
		
		return ret;
	}

	//! Load a mesh, time it
	virtual scene::IAnimatedMesh* createMesh(io::IReadFile* file)
	{
		scene::IAnimatedMesh* ret = 0;

		scene::ISceneManager* smgr = Device->getSceneManager();

		u32 readTime=0;

		// find the correct loader
		for (s32 i=smgr->getMeshLoaderCount()-1; !ret && i >= 0; --i)
			if (smgr->getMeshLoader(i) != this &&
			    smgr->getMeshLoader(i)->isALoadableFileExtension(file->getFileName()))
			{
				// attempt to open
				u32 readStart = Device->getTimer()->getRealTime();
				ret = smgr->getMeshLoader(i)->createMesh(file);
				readTime = Device->getTimer()->getRealTime() - readStart;
			}

		if (ret)
			log(readTime, file->getFileName());
		
		return ret;
	}

	//! Load a scene, time it
	virtual bool loadScene(io::IReadFile* file, scene::ISceneUserDataSerializer* userDataSerializer=0,
	                       scene::ISceneNode* rootNode=0) 
	{
		bool ret = false;

		scene::ISceneManager* smgr = Device->getSceneManager();

		u32 readTime=0;

		// find the correct loader
		for (s32 i=smgr->getSceneLoaderCount()-1; !ret && i >= 0; --i)
			if (smgr->getSceneLoader(i) != this &&
			    smgr->getSceneLoader(i)->isALoadableFileFormat(file))
			{
				// attempt to open
				u32 readStart = Device->getTimer()->getRealTime();
				ret = smgr->getSceneLoader(i)->loadScene(file, userDataSerializer, rootNode);
				readTime = Device->getTimer()->getRealTime() - readStart;
			}

		if (ret)
			log(readTime, file->getFileName());
		
		return ret;
	}


	//! Mounting an archive from file name
	virtual io::IFileArchive* createArchive(const io::path& filename, bool ignoreCase, bool ignorePaths) const
	{
		io::IReadFile* f = Device->getFileSystem()->createAndOpenFile(filename);

		io::IFileArchive* ret = createArchive(f, ignoreCase, ignorePaths);

		f->drop();
		
		return ret;
	}

	//! Mount an archive, time it.
	virtual io::IFileArchive* createArchive(io::IReadFile* file, bool ignoreCase, bool ignorePaths) const
	{
		io::IFileArchive* ret = 0;

		io::IFileSystem* fs = Device->getFileSystem();

		u32 start=Device->getTimer()->getRealTime(), readTime=0, totalTime=0;

		// find the correct loader
		for (s32 i=fs->getArchiveLoaderCount()-1; !ret && i >= 0; --i)
			if (fs->getArchiveLoader(i) != this &&
			    fs->getArchiveLoader(i)->isALoadableFileFormat(file))
			{
				// attempt to open
				u32 readStart = Device->getTimer()->getRealTime();
				ret = fs->getArchiveLoader(i)->createArchive(file, ignoreCase, ignorePaths);
				readTime = Device->getTimer()->getRealTime() - readStart;
			}

		totalTime = Device->getTimer()->getRealTime() - start;

		if (ret)
			log(readTime, totalTime, file->getFileName());
		
		return ret;
	}

private:
	IrrlichtDevice* Device;

	void log(u32 readTime, core::stringc filename) const
	{
		core::stringc msg = "LoaderProfiler: took ";
		msg += readTime;
		msg += "ms to load '";
		msg += filename + "'";

		Device->getLogger()->log(msg.c_str());
	}

};

}
```
