# Docker Pipeline Cache

## why?

* Bandwidth is often cheaper than CPU - for the planet at least.
* You've got lots of it on a server in a datacenter. CPU is the
  same though.
* A randomly allocated build server always has to run your shitty
  setup steps as part of the build. So you need to hit the same
  box. But often you don't, so you have to run the steps.

## how?

* Pull the last known good image from a container registry
* Add a subset of the server's rootfs to a Dockerfile (lol), build it.
* copy the cwd somewhere else, add it as the cwd. Build it again.
* Add the command you want to cache to the Dockerfile as a run step, build it.
* Copy changed files back out over the filesystem, and ADD them in the next step
* Repeat for all cached steps
* At the end of the run, push the image to the registry

## and?

And your build times got shorter. Hopefully.
