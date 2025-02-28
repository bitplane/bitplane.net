# 🤖 Generic AI hacking workflow

I've been using a few different models while doing coding work, and over xmas
I finalized a workflow that works with them all, excluding copilot which only
works in an editor. So far this technique works well with:

1. The consultancy's internal model
2. The client's multiple internal models, and external ones
3. ChatGPT, using my account.
4. ollama, running locally or on a rented machine on vast.ai over ssh (-X)
5. claude
6. grock
7. groq
8. gemini

So I've added aliases for `c`, `v` and `git-dump`, to my `~/.bashrc` and/or
`~/.zshrc` files:

```bash
if command -v pbcopy &>/dev/null; then
    alias c="pbcopy"
    alias v="pbpaste"
elif [ "$XDG_SESSION_TYPE" = "wayland" ] && command -v wl-copy &>/dev/null; then
    alias c="wl-copy"
    alias v="wl-paste"
elif command -v xsel &>/dev/null; then
    alias c="xsel --clipboard --input"
    alias v="xsel --clipboard --output"
elif command -v clip.exe &>/dev/null; then
    alias c="clip.exe"
    alias v="powershell.exe Get-Clipboard"
fi


# commit hash of an empty git repo
EMPTY_TREE=$(echo -n 'tree 0\0' | sha1sum | cut -f 1 -d ' ')

alias git-dump="git diff $EMPTY_TREE --"
```

Then when I want to start a conversation about a project or subset of it, I can
run `git-dump | c` and paste it in from the clipboard. Like:

```text
Hey chatbot, here's where we're up to. Summary and next steps please:

<ctrl+v>
```

Then it gets all the files as a single patch, but doesn't have the full commit
history which will blow the context window or give too much comprognitive load;
it works with reasonably strong models.

The most powerful thing about this, is that adding instructions for an AI agent
to the project's `README.md` will cause it to focus on the next tasks rather
than noise that's less relevant.

If it's a large project or I want to focus on just a small area I can filter by
a dir, like `git-dump . | c`, add filters to exclude binary files or large text
files like so: `git-dump . ':!*.cast'`.

And when the model gives some output, I can `v > file` to write the changes, and
if I make my own changes and feed them back in, just `cat file | c` to share my
own edits.

And of course it works with other things like `git-dump | wc -l`, with `grep`,
or `v | pastebinit` and so on.

Given how fast this space is moving, it might not remain the best way to do
things for very long. But for the moment, it works pretty well for me.


