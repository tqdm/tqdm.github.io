<a name="tqdm.notebook"></a>
# tqdm.notebook

IPython/Jupyter Notebook progressbar decorator for iterators.
Includes a default (x)range iterator printing to stderr.

Usage:
  >>> from tqdm.notebook import trange[, tqdm]
  >>> for i in trange(10): `same` as: for i in tqdm(xrange(10))
  ...     ...

<a name="tqdm.notebook.tqdm_notebook"></a>
## tqdm\_notebook Objects

```python
class tqdm_notebook(std_tqdm)
```

Experimental IPython/Jupyter Notebook widget using tqdm!

<a name="tqdm.notebook.tqdm_notebook.status_printer"></a>
#### status\_printer

```python
 | @staticmethod
 | status_printer(_, total=None, desc=None, ncols=None)
```

Manage the printing of an IPython/Jupyter Notebook progress bar widget.

<a name="tqdm.notebook.tqdm_notebook.reset"></a>
#### reset

```python
 | reset(total=None)
```

Resets to 0 iterations for repeated use.

Consider combining with `leave=True`.

Parameters
----------
total  : int or float, optional. Total to use for the new bar.

