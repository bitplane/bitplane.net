Make docker containers smaller by having exhaustive test coverage,
then removing every file that wasn't accessed during tests.

## Easy mode

* Copy all files into a new filesystem
* Reset their access times to epoch.
* Spin up image as root with atime enabled
* Run all tests from another filesystem
* Shut it down
* Remove all files that haven't been accessed.

## Hard mode

* Strace from the init daemon, or use a kernel debug trace?
* Record all files accessed, seek positions and data returned by read()
* Map them all out and combine them.
* Combine overlaps
* Recreate the filesystem with just the regions of files that were read.
* Shrink and compress the image

## God mode

Instead of just looking at file reads, look at where it goes in ram.
If it gets discarded or overwritten without being used then mark it
as useless and remove it.

Look at all library calls and if they return the same thing each time
then replace the library with a stub.

Fuzz your main inputs, cache the call stack by caller, params and
response. If responses are always smaller than the code, cache it.

This would require tests that cause exceptions in every possible way,
and a coverage tool that is far deeper than standard, and 100% coverage.

## God king emperor mode

So you have a bunch of services that are RAM heavy, they run across
a number of machines. Stick a gateway on the front with MQ architecture.

Use ordinary test cases to shrink the images as in Hard Mode and use
them for.the bulk of your services, but keep an unmolested one around
too, frozen ready to resume.

If you get a crash:

* Post a message with the request saying it's a bad one
* Spin up a real container process the request
* Throw the input request into the test case bucket and run the shrink
  process again.
* Redeploy. Rinse and repeat.

If it means you can run 10x the services with only an occasional risk to
response times then it might even be a sane idea?!
