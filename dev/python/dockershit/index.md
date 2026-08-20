# docker sh -it

```txt
BUILDING DOCKERIFLES OVER AND OVER AGAIN WITH NO FEEDBACK AT ALL IS LIKE WEARING
THREE CONDOMS I'M TOO OLD FOR THIS SHIT I NEED TO TOUCH IT AND FEEL WHAT'S GOING
ON IN THERE OR I'LL LOSE INTEREST WHY CAN'T WE JUST CONNECT AND GET FEEDBACK AND
A RHYTHM GOING INSTEAD OF ALL THIS STOPPING AND STARTING IT'S REALLY OFF-PUTTING
AND NOT GOOD FOR ANYONE WHY NOT CONNECT TO THE CONTAINER THEN TYPE YOUR COMMANDS
IN AND WHEN THEY WORK THEY GET ADDED TO THE dOCKERFILE AND IF THEY DON'T THEY GO
IN AS COMMENTS OR SOMETHING AND IN THE BACKGROUND IT'S REBUILDING YOUR IMAGE AND
RECONNECTING READY FOR THE NEXT COMMAND OH AND HAVE IT WORK WITH THINGS LIKE add
AND copy AND STUFF THEN WHEN YOU'VE ACTUALLY GOT SOMETHING THAT WORKS YOU CAN GO
AND EDIT IT INTO SOMETHING THAT LOOKS MORE LIKE AN ACTUAL dOCKERFILE RATHER THAN
TRYING TO DO EVERYTHING UP-FRONT BEFORE YOU EVEN KNOW IF IT'S GONNA WORK INSTEAD
OF COMMUNICATING BY TELEGRAM MAYBE I SHOULD INSTALL DOCKERSHIT AND USE THAT YEAH
ITS PRETTY EASH YOU JUST TYPE `uvx dockershit` APPARENTLY AND IT'LL BE READY FOR
USE IN UNDER A SECOND AND WILL MOSTLY WORK BUT MIGHT BE BUGGY BECAUSE ITS NEWISH
AND THE DEVELOPER WROTE IT IN ANGER AND DOESN'T SEEM TO TAKE IT SERIOUSLY BUT IT
IS WORTH A TRY BECAUSE IF YOU WASTE TIME HERE AT LEAST IT IS WASTED DIFFERENTLY.
```

## Usage

Quickest way is run it in `uv` (either `pip install uv` or follow
[their instructions](https://github.com/astral-sh/uv)). Or use
`pip install dockershit` or `pipx dockershit`. It's on pypi.

### ⚠️ IT EDITS DOCKERFILES SO USE SOURCE CONTROL ⚠️

By default it'll create or append to a `Dockerfile` in your pwd. Each proposed
instruction is tested as a transaction: if it breaks the build, the previous
file is restored byte-for-byte before the failed instruction is added as a
comment. Don't say you weren't warned.

```bash
uvx dockershit ubuntu:latest
```

It uses Podman when available, falling back to Docker. Choose one explicitly
with `--engine podman` or `--engine docker`.

* 🔢 type some commands, then `exit` or `quit`
* 👀 look in your pwd for a `Dockerfile`, notice the `RUN` lines - they're the
  commands that worked (zero exit code)
* 💣 commands that failed or made no changes are commented out
* 🔃 arrow keys and ctrl+r work, history is in `Dockerfile.history`
* ⬅️ commands starting with a space don't get added to the file, but they do go to
  the .history file
* 💬 comments e.g. `# wtf delete the above` go to the `Dockerfile` unless they
  start with a space i.e. ` # subscribe and like, like and subscribe`
* ➕ `ADD`, `COPY` and other docker shit get added too, and the image is rebuilt
  between each command
* #️⃣ if a command fails, you'll get a commented out line instead
* 🚶 `cd` changes your `WORKDIR`, and `WORKDIR` changes your `cd`
* 🐛 use `--debug` if you want to see it rebuilding
* 💥 if an instruction breaks the build, it restores the previous `Dockerfile`
* 🚫 your Dockerfile and its history are excluded from the context
* 🪈 you can use it with pipe like `cat whatever | dockershit`
* 💩 yeah it runs everything twice, which is an embarrassment - in future I'll make
  it just run in docker, but pull requests are welcome

# License

WTFPL with one additional clause:

1. Don't blame me!

# Links

* [🏠 home](https://bitplane.net/dev/python/dockershit)
* [🐍 pypi](https://pypi.org/project/dockershit)
* [🐱 github](https://github.com/bitplane/dockershit)
* [📖 pydoc](https://bitplane.net/dev/python/dockershit/pydoc)

## TODO

* restructure input so it's a nice UI
  * use textual?
* remove double `WORKDIR` entries by combining them
* deal with `ENV` and `ARG` - passing them in on the command line.
* add `DS` commands or whatever it ends up being called
  * use `argparse`
  * `edit`, to edit the current file (in git editor?)
  * `squash`, combine run steps with `&& \`
