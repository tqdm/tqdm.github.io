<a name="tqdm.contrib"></a>
# tqdm.contrib

Thin wrappers around common functions.

Subpackages contain potentially unstable extensions.

<a name="tqdm.contrib.tenumerate"></a>
#### tenumerate

```python
tenumerate(iterable, start=0, total=None, tqdm_class=tqdm_auto, **tqdm_kwargs)
```

Equivalent of `numpy.ndenumerate` or builtin `enumerate`.

Parameters
----------
tqdm_class  : [default: tqdm.auto.tqdm].

