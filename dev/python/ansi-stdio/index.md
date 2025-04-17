# 🖼️ ansi stdio

Terminal text composition and animation library.

```sh
$ uvx ansi_stdio
```

## Tools

* `ansi-quantize` - terminal filter to help you strip out log dump noise from
  asciinema recordings. Currently doesn't do a very good job of it, due to
  not having char-level diffs.
* `ansi-fonts` - lists available monospace fonts on the system.

## Design

The thing is a scene graph made of Actor nodes. Each node has a clock and when
rendered, can redirect calls. Haven't decided how child relationships and
recursion will work yet, so keeping this open. Probably won't call them actors
either.

Clocks are chained timers that can be paused and implement time however they
like. `clock.wall` gives you the system time. `Clock.time` gives the current
time etc.

Buffers are sparse grids of `rich` characters. They track their own size and
can be merged (`+=` and `+`), queried/set (slice notation) and copied.

### Object design

So far we have:

* 🔢 Versioned - objects that are versioned have a version number that gets
  updated when they are changed.
* 📦 Box - a 2d box, used for bounding things.
* ⏲️ Clock - the workhorse of animation.

Still not figured out:

* 💾 Saved - a serializable class.
* 🎞️ The main actor class - is it a View?
* How buffers, views and time work together with caching.
* Should "Animation" be a buffer?

## Overall plan

* Build a custom video format with keyframes and delta frames/buffers. This can
  act as a cache and a rendering format. The encoder can then be used to
  capture terminal graphics from various sources, including text files,
  programs or other loaders.
* Build serialization into the core objects via a generic mixin. The
  construction parameters will be attribute names by convention, so they can
  always be (de)serialized.
* Once the foundations are laid, build in structure for working with a vast
  library of effects, sources and so on, and filtering it effectively. So we
  don't end up constrained, with everything dumped in a directory, and can
  compose the different things in various ways.
* Make a plugin system for all these things.
* Build a basic UI that works with this, somewhere between Kdenlive and OBS
  Studio.
* Go to town building components that are useful. Idea being to use code
  generation within the confines of a decent structure, so using AI to add
  to it doesn't end up like a Glastonbury Festival toilet.

## Next Steps

* Finish the Saved class, figure out how it relates to Versioned.
* Figure out animation buffers, how they map to buffers, accumulate and can
  be rendered.
* Implement a recorder using the above.
* Figure out how to convert ANSI text into animations when it has no timing
  info (callbacks that look for cursor movements and/or screen resets).
* Start work on the UI
