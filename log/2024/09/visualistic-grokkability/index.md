# \[idea\] Eyeballing training runs

Seems to me, as a bit of a noob and an outsider, that a pretty big issue in
machine learning is the lack of decent visualisations.

Training a decent model is more art than science, it involves a lot of gut feel
about the data, features, model architecture and so on - it's an exercise in
cookery rather than engineering. But the language we use to describe it is about
science rather than art, there's no smelling or tasting the model as it bubbles
on the hob.

So we end up with exhaustive, brute-force metrics that are infeasible, or weak
ones with bad names. We sit watching the training loss by default and not much
else, or at least I do. And everyone has their own models and their own data,
so their problems and learnings aren't really shareable.

## Visualistic Grokkability

What if we made a GitHub project with code to deterministically create bad
models, saving checkpoints at each epoch, as a dataset that can be used to
create new visualisation methods?

This seems like a pretty simple project to build, it'd take the bare minimum
example code and a bunch of examples of how to totally mess up!

No promises on any code, so I'll park this here for now.
