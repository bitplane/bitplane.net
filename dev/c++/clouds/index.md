# Clouds

The cloud node was my first attempt at writing an Irrlicht ISceneNode, it was
also my first real attempt at writing my own C++ classes too, I hadn’t RTFM at
the time either so the code is a bit sloppy, but the effect is still good.

![clouds](cloudsnew.jpg)

The idea is that clouds are made of millions of particles, far more than you
could ever draw at once on a low end machine. I decided to make a cloud node
which draws only the bare minimum of quads and recursively adds additional
levels of detail as you approach it, kind of like a fractal. It does have a
maximum depth level which is usually set to a sensible value.

The code for CCloudSceneNode is available from
[IrrExt’s SVN repository](http://irrext.svn.sourceforge.net/viewvc/irrext/trunk/extensions/scene/ISceneNode/CloudSceneNode/)
