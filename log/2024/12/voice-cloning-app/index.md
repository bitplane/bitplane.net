# 🦜 voice-cloning-app

[Last year](/log/2023/09/voice-cloning) I was using [Voice-Cloning-App](https://github.com/voice-cloning-app/Voice-Cloning-App)
to create Tacotron 2 models, and archived a working copy using Docker, as it
was dying of bitrot. This is the case with many Python machine learning
projects, which seem to have a limited shelf life due to the pace of
development, hardware and driver dependencies, and the size of the models are
too big to stick in a git repo (without incurring charges at least).

Well now I've got a bigger disk and Linux running on my laptop, I decided to
do some more cloning. Turns out that the creator, [Ben](https://benaandrew.github.io/)
has archived the project. With newer models like RVC and Bark being all the
rage, most of the community have moved on. But I personally like Tacotron2 as
it actually works with my accent, and the cloning app is really easy to use.

So I messaged him and asked if he'd unarchive it and transition to a GitHub org,
he can keep ownership and I'll do some maintenance and invite contributors to
join as and when they resurface.

And he agreed 🎉, so now I've inherited a Discord server and a project with 1.4k
stars, which seems like an awful lot of responsibility.

A few things that need(ed) fixing:

* Mozilla sacked their DeepSpeech team, so their STT doesn't work with recent
  Python versions. But we have Whisper at least, which is hosted on Hugging
  Face (more on this in a future post). I've removed the DeepSpeech deps for
  the moment, and will replace it with Whisper soonish™. Thankfully it uses
  Silero for STT by default.
* Nvidia's pre-trained models were on Google Drive, and whoever has the keys
  mustn't have a Google account there anymore. So I archived them on
  archive.org [here](https://archive.org/download/tacotron2-statedict)
* HiFi-GAN suffered a similar fate, but Jungil Kong restored access when I
  requested it. But I archived it [here](https://archive.org/details/voice-cloning-app-hifigan)
* The project's CI has been broken for ages, so that'll need to be moved from
  circle to GitHub actions.
* The model sharing hub has been defunct for ages. I think I can revive it
  using the Internet Archive as a back-end; they have an S3-like storage API
* The tutorial videos are dead, one of them was taken down. The rest have been
  archived [here](https://archive.org/details/voice-cloning-app-yt-backup).

So once I get CI working again and make the thing run with data from the
Internet Archive, I'll do a new release, and think about how it can be extended
with some of the ideas that I've been working on for decentralizing this sort
of thing.

For the moment, the Docker nvidia version is gonna be the most up-to-date as
it's the one I'm using myself.


