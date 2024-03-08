# decentralised social media based on git

Take a repo like this one and generate HTML pages from it, with a CI
job that first preprocesses the files then runs Jekyll or similar to
generate the output.

The first commit hash of README.md becomes the blog's ID.

## connecting and commenting

Have a branch that's your "comment root". It

Have a branch for each other blog that you're commenting on, forked
from their comment root. Have a file that lists remotes and branches that you're pulling from. At rebuild
time it clones/pulls those and builds them into the pagess.

If someone wants to comment on your blog then they just send you a pull
request adding themselves to your list of comment repos. If you merge
it then they are added as remotes next rebuild. Pull each remote and use
it when generating comments.

Now you can generate not only your blog but anyone else's too! The
outputs can be anywhere, the method used to do the first pull request
is injected into the page by the repo owner. Git web platforms can
generally show the posts.

Org to org links should also be possible, creating a discussion platform
that doesn't belong to any one company.

## rules and stuff

* Rate limits
* Size limits
* Content mime type limits
* Removing specific posts
* Censorship with content
* Banning users without deleting their old posts
* Showing previous edits
* Dropping remotes that are troublesome
* Shallow or deep copying other repos.

## performance stuff

* Incremental updates
* Dependency resolver for comments on comments you haven't got yet
* Prefer https remotes so we can use HEAD requests to decide whether
  they are good.

## decentralisation

* Support IPFS git repo links.
* GitHub, gitlab, email, pubsub JavaScript templates for starting pull
  requests.

## investigation

Q: How can we mark a branch as not being a fork of the master branch? We
   don't want accidental pull requests all over the place.

A: No way to do this. Create an intentional merge conflict in a file that
   bollocks the user for trying to merge it.

Q: How could we run edits in a browser?

A: Not sure yet, there's a wasm git client but it needs a CORS-busting
   git web server which limits its usefulness.
