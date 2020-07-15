<a name="tqdm.std"></a>
# tqdm.std

Customisable progressbar decorator for iterators.
Includes a default (x)range iterator printing to stderr.

Usage:
  >>> from tqdm import trange[, tqdm]
  >>> for i in trange(10): `same` as: for i in tqdm(xrange(10))
  ...     ...

<a name="tqdm.std.TqdmWarning"></a>
## TqdmWarning Objects

```python
class TqdmWarning(Warning)
```

base class for all tqdm warnings.

Used for non-external-code-breaking errors, such as garbled printing.

<a name="tqdm.std.TqdmExperimentalWarning"></a>
## TqdmExperimentalWarning Objects

```python
class TqdmExperimentalWarning(TqdmWarning,  FutureWarning)
```

beta feature, unstable API and behaviour

<a name="tqdm.std.TqdmMonitorWarning"></a>
## TqdmMonitorWarning Objects

```python
class TqdmMonitorWarning(TqdmWarning,  RuntimeWarning)
```

tqdm monitor errors which do not affect external functionality

<a name="tqdm.std.TqdmDefaultWriteLock"></a>
## TqdmDefaultWriteLock Objects

```python
class TqdmDefaultWriteLock(object)
```

Provide a default write lock for thread and multiprocessing safety.
Works only on platforms supporting `fork` (so Windows is excluded).
You must initialise a `tqdm` or `TqdmDefaultWriteLock` instance
before forking in order for the write lock to work.
On Windows, you need to supply the lock from the parent to the children as
an argument to joblib or the parallelism lib you use.

