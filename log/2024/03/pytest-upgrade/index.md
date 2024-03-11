# Upgrading deps automagically

Just a thought - haven't tried it:

```bash

deps=.requirements.verified
pip freeze > $deps

packages=$(pip review | cut -d '=' -f 1)

for package in $packages; do
    pip install --upgrade $package && \
        make test && \
        pip freeze > $deps || \
        pip install -r $deps
done

mv $deps requirements.txt
```

