<a name="tqdm.gui"></a>
# tqdm.gui

GUI progressbar decorator for iterators.
Includes a default (x)range iterator printing to stderr.

Usage:
  >>> from tqdm.gui import trange[, tqdm]
  >>> for i in trange(10): `same` as: for i in tqdm(xrange(10))
  ...     ...

<a name="tqdm.gui.tqdm_gui"></a>
## tqdm\_gui Objects

```python
class tqdm_gui(std_tqdm)
```

Experimental GUI version of tqdm!

