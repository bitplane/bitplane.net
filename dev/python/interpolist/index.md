# InterpoList

InterpoList is a list class for Python which interpolates between missing
values. It’s useful for graphing, where you use it like this:

```python
>>> a = InterpoList()
>>> a[0]   = 0
>>> a[100] = 200
>>> a[200] = 0
>>> a[50]
100.0
>>> a[125]
150.0
```

See the [original post](/log/2009/12/interpolist) for more info. You can get
the module [here](https://github.com/bitplane/typepie)
