<a name="tqdm.std"></a>
# tqdm.std

Customisable progressbar decorator for iterators.
Includes a default (x)range iterator printing to stderr.

Usage:
  >>> from tqdm import trange[, tqdm]
  >>> for i in trange(10): `same` as: for i in tqdm(xrange(10))
  ...     ...

<a name="tqdm.std.tqdm"></a>
## tqdm Objects

```python
class tqdm(Comparable)
```

Decorate an iterable object, returning an iterator which acts exactly
like the original iterable, but prints a dynamically updating
progressbar every time a value is requested.

<a name="tqdm.std.tqdm.format_sizeof"></a>
#### format\_sizeof

```python
 | @staticmethod
 | format_sizeof(num, suffix='', divisor=1000)
```

Formats a number (greater than unity) with SI Order of Magnitude
prefixes.

Parameters
----------
num  : float
    Number ( >= 1) to format.
suffix  : str, optional
    Post-postfix [default: ''].
divisor  : float, optional
    Divisor between prefixes [default: 1000].

Returns
-------
out  : str
    Number with Order of Magnitude SI unit postfix.

<a name="tqdm.std.tqdm.format_interval"></a>
#### format\_interval

```python
 | @staticmethod
 | format_interval(t)
```

Formats a number of seconds as a clock time, [H:]MM:SS

Parameters
----------
t  : int
    Number of seconds.

Returns
-------
out  : str
    [H:]MM:SS

<a name="tqdm.std.tqdm.format_num"></a>
#### format\_num

```python
 | @staticmethod
 | format_num(n)
```

Intelligent scientific notation (.3g).

Parameters
----------
n  : int or float or Numeric
    A Number.

Returns
-------
out  : str
    Formatted number.

<a name="tqdm.std.tqdm.ema"></a>
#### ema

```python
 | @staticmethod
 | ema(x, mu=None, alpha=0.3)
```

Exponential moving average: smoothing to give progressively lower
weights to older values.

Parameters
----------
x  : float
    New value to include in EMA.
mu  : float, optional
    Previous EMA value.
alpha  : float, optional
    Smoothing factor in range [0, 1], [default: 0.3].
    Increase to give more weight to recent values.
    Ranges from 0 (yields mu) to 1 (yields x).

<a name="tqdm.std.tqdm.status_printer"></a>
#### status\_printer

```python
 | @staticmethod
 | status_printer(file)
```

Manage the printing and in-place updating of a line of characters.
Note that if the string is longer than a line, then in-place
updating may not work (it will print a new line at each refresh).

<a name="tqdm.std.tqdm.format_meter"></a>
#### format\_meter

```python
 | @staticmethod
 | format_meter(n, total, elapsed, ncols=None, prefix='', ascii=False, unit='it', unit_scale=False, rate=None, bar_format=None, postfix=None, unit_divisor=1000, **extra_kwargs)
```

Return a string-based progress bar given some parameters

Parameters
----------
n  : int or float
Number of finished iterations.
total  : int or float
The expected total number of iterations. If meaningless (None),
only basic progress statistics are displayed (no ETA).
elapsed  : float
Number of seconds passed since start.
ncols  : int, optional
The width of the entire output message. If specified,
dynamically resizes `{bar}` to stay within this bound
[default: None]. If `0`, will not print any bar (only stats).
The fallback is `{bar:10}`.
prefix  : str, optional
Prefix message (included in total width) [default: ''].
Use as {desc} in bar_format string.
ascii  : bool, optional or str, optional
If not set, use unicode (smooth blocks) to fill the meter
[default: False]. The fallback is to use ASCII characters
" 123456789#".
unit  : str, optional
The iteration unit [default: 'it'].
unit_scale  : bool or int or float, optional
If 1 or True, the number of iterations will be printed with an
appropriate SI metric prefix (k = 10^3, M = 10^6, etc.)
[default: False]. If any other non-zero number, will scale
`total` and `n`.
rate  : float, optional
Manual override for iteration rate.
If [default: None], uses n/elapsed.
bar_format  : str, optional
Specify a custom bar string formatting. May impact performance.
[default: '{l_bar}{bar}{r_bar}'], where
l_bar='{desc}: {percentage:3.0f}%|' and
r_bar='| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, '
'{rate_fmt}{postfix}]'
Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt,
percentage, elapsed, elapsed_s, ncols, nrows, desc, unit,
rate, rate_fmt, rate_noinv, rate_noinv_fmt,
rate_inv, rate_inv_fmt, postfix, unit_divisor,
remaining, remaining_s.
Note that a trailing ": " is automatically removed after {desc}
if the latter is empty.
postfix  : *, optional
Similar to `prefix`, but placed at the end
(e.g. for additional stats).
Note: postfix is usually a string (not a dict) for this method,
and will if possible be set to postfix = ', ' + postfix.
However other types are supported (`382`).
unit_divisor  : float, optional
[default: 1000], ignored unless `unit_scale` is True.

Returns
-------
out  : Formatted meter and stats, ready to display.

<a name="tqdm.std.tqdm.write"></a>
#### write

```python
 | @classmethod
 | write(cls, s, file=None, end="\n", nolock=False)
```

Print a message via tqdm (without overlap with bars).

<a name="tqdm.std.tqdm.external_write_mode"></a>
#### external\_write\_mode

```python
 | @classmethod
 | @contextmanager
 | external_write_mode(cls, file=None, nolock=False)
```

Disable tqdm within context and refresh tqdm when exits.
Useful when writing to standard output stream

<a name="tqdm.std.tqdm.set_lock"></a>
#### set\_lock

```python
 | @classmethod
 | set_lock(cls, lock)
```

Set the global lock.

<a name="tqdm.std.tqdm.get_lock"></a>
#### get\_lock

```python
 | @classmethod
 | get_lock(cls)
```

Get the global lock. Construct it if it does not exist.

<a name="tqdm.std.tqdm.pandas"></a>
#### pandas

```python
 | @classmethod
 | pandas(tclass, *targs, **tkwargs)
```

Registers the given `tqdm` class with
    pandas.core.
    ( frame.DataFrame
    | series.Series
    | groupby.(generic.)DataFrameGroupBy
    | groupby.(generic.)SeriesGroupBy
    ).progress_apply

A new instance will be create every time `progress_apply` is called,
and each instance will automatically close() upon completion.

Parameters
----------
targs, tkwargs  : arguments for the tqdm instance

Examples
--------
>>> import pandas as pd
>>> import numpy as np
>>> from tqdm import tqdm
>>> from tqdm.gui import tqdm as tqdm_gui
>>>
>>> df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
>>> tqdm.pandas(ncols=50)  # can use tqdm_gui, optional kwargs, etc
>>> # Now you can use `progress_apply` instead of `apply`
>>> df.groupby(0).progress_apply(lambda x: x**2)

References
----------
https://stackoverflow.com/questions/18603270/
progress-indicator-during-pandas-operations-python

<a name="tqdm.std.tqdm.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(iterable=None, desc=None, total=None, leave=True, file=None, ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None, ascii=None, disable=False, unit='it', unit_scale=False, dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0, position=None, postfix=None, unit_divisor=1000, write_bytes=None, lock_args=None, nrows=None, gui=False, **kwargs)
```

Parameters
----------
iterable  : iterable, optional
    Iterable to decorate with a progressbar.
    Leave blank to manually manage the updates.
desc  : str, optional
    Prefix for the progressbar.
total  : int or float, optional
    The number of expected iterations. If unspecified,
    len(iterable) is used if possible. If float("inf") or as a last
    resort, only basic progress statistics are displayed
    (no ETA, no progressbar).
    If `gui` is True and this parameter needs subsequent updating,
    specify an initial arbitrary large positive number,
    e.g. 9e9.
leave  : bool, optional
    If [default: True], keeps all traces of the progressbar
    upon termination of iteration.
    If `None`, will leave only if `position` is `0`.
file  : `io.TextIOWrapper` or `io.StringIO`, optional
    Specifies where to output the progress messages
    (default: sys.stderr). Uses `file.write(str)` and `file.flush()`
    methods.  For encoding, see `write_bytes`.
ncols  : int, optional
    The width of the entire output message. If specified,
    dynamically resizes the progressbar to stay within this bound.
    If unspecified, attempts to use environment width. The
    fallback is a meter width of 10 and no limit for the counter and
    statistics. If 0, will not print any meter (only stats).
mininterval  : float, optional
    Minimum progress display update interval [default: 0.1] seconds.
maxinterval  : float, optional
    Maximum progress display update interval [default: 10] seconds.
    Automatically adjusts `miniters` to correspond to `mininterval`
    after long display update lag. Only works if `dynamic_miniters`
    or monitor thread is enabled.
miniters  : int or float, optional
    Minimum progress display update interval, in iterations.
    If 0 and `dynamic_miniters`, will automatically adjust to equal
    `mininterval` (more CPU efficient, good for tight loops).
    If > 0, will skip display of specified number of iterations.
    Tweak this and `mininterval` to get very efficient loops.
    If your progress is erratic with both fast and slow iterations
    (network, skipping items, etc) you should set miniters=1.
ascii  : bool or str, optional
    If unspecified or False, use unicode (smooth blocks) to fill
    the meter. The fallback is to use ASCII characters " 123456789#".
disable  : bool, optional
    Whether to disable the entire progressbar wrapper
    [default: False]. If set to None, disable on non-TTY.
unit  : str, optional
    String that will be used to define the unit of each iteration
    [default: it].
unit_scale  : bool or int or float, optional
    If 1 or True, the number of iterations will be reduced/scaled
    automatically and a metric prefix following the
    International System of Units standard will be added
    (kilo, mega, etc.) [default: False]. If any other non-zero
    number, will scale `total` and `n`.
dynamic_ncols  : bool, optional
    If set, constantly alters `ncols` and `nrows` to the
    environment (allowing for window resizes) [default: False].
smoothing  : float, optional
    Exponential moving average smoothing factor for speed estimates
    (ignored in GUI mode). Ranges from 0 (average speed) to 1
    (current/instantaneous speed) [default: 0.3].
bar_format  : str, optional
    Specify a custom bar string formatting. May impact performance.
    [default: '{l_bar}{bar}{r_bar}'], where
    l_bar='{desc}: {percentage:3.0f}%|' and
    r_bar='| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, '
      '{rate_fmt}{postfix}]'
    Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt,
      percentage, elapsed, elapsed_s, ncols, nrows, desc, unit,
      rate, rate_fmt, rate_noinv, rate_noinv_fmt,
      rate_inv, rate_inv_fmt, postfix, unit_divisor,
      remaining, remaining_s.
    Note that a trailing ": " is automatically removed after {desc}
    if the latter is empty.
initial  : int or float, optional
    The initial counter value. Useful when restarting a progress
    bar [default: 0]. If using float, consider specifying `{n:.3f}`
    or similar in `bar_format`, or specifying `unit_scale`.
position  : int, optional
    Specify the line offset to print this bar (starting from 0)
    Automatic if unspecified.
    Useful to manage multiple bars at once (eg, from threads).
postfix  : dict or *, optional
    Specify additional stats to display at the end of the bar.
    Calls `set_postfix(**postfix)` if possible (dict).
unit_divisor  : float, optional
    [default: 1000], ignored unless `unit_scale` is True.
write_bytes  : bool, optional
    If (default: None) and `file` is unspecified,
    bytes will be written in Python 2. If `True` will also write
    bytes. In all other cases will default to unicode.
lock_args  : tuple, optional
    Passed to `refresh` for intermediate output
    (initialisation, iterating, and updating).
nrows  : int, optional
    The screen height. If specified, hides nested bars outside this
    bound. If unspecified, attempts to use environment height.
    The fallback is 20.
gui  : bool, optional
    WARNING: internal parameter - do not use.
    Use tqdm.gui.tqdm(...) instead. If set, will attempt to use
    matplotlib animations for a graphical output [default: False].

Returns
-------
out  : decorated iterator.

<a name="tqdm.std.tqdm.__iter__"></a>
#### \_\_iter\_\_

```python
 | __iter__()
```

Backward-compatibility to use: for x in tqdm(iterable)

<a name="tqdm.std.tqdm.update"></a>
#### update

```python
 | update(n=1)
```

Manually update the progress bar, useful for streams
such as reading files.
E.g.:
>>> t = tqdm(total=filesize) # Initialise
>>> for current_buffer in stream:
...    ...
...    t.update(len(current_buffer))
>>> t.close()
The last line is highly recommended, but possibly not necessary if
`t.update()` will be called in such a way that `filesize` will be
exactly reached and printed.

Parameters
----------
n  : int or float, optional
    Increment to add to the internal counter of iterations
    [default: 1]. If using float, consider specifying `{n:.3f}`
    or similar in `bar_format`, or specifying `unit_scale`.

<a name="tqdm.std.tqdm.close"></a>
#### close

```python
 | close()
```

Cleanup and (if leave=False) close the progressbar.

<a name="tqdm.std.tqdm.clear"></a>
#### clear

```python
 | clear(nolock=False)
```

Clear current bar display.

<a name="tqdm.std.tqdm.refresh"></a>
#### refresh

```python
 | refresh(nolock=False, lock_args=None)
```

Force refresh the display of this bar.

Parameters
----------
nolock  : bool, optional
    If `True`, does not lock.
    If [default: `False`]: calls `acquire()` on internal lock.
lock_args  : tuple, optional
    Passed to internal lock's `acquire()`.
    If specified, will only `display()` if `acquire()` returns `True`.

<a name="tqdm.std.tqdm.unpause"></a>
#### unpause

```python
 | unpause()
```

Restart tqdm timer from last print time.

<a name="tqdm.std.tqdm.reset"></a>
#### reset

```python
 | reset(total=None)
```

Resets to 0 iterations for repeated use.

Consider combining with `leave=True`.

Parameters
----------
total  : int or float, optional. Total to use for the new bar.

<a name="tqdm.std.tqdm.set_description"></a>
#### set\_description

```python
 | set_description(desc=None, refresh=True)
```

Set/modify description of the progress bar.

Parameters
----------
desc  : str, optional
refresh  : bool, optional
    Forces refresh [default: True].

<a name="tqdm.std.tqdm.set_description_str"></a>
#### set\_description\_str

```python
 | set_description_str(desc=None, refresh=True)
```

Set/modify description without ': ' appended.

<a name="tqdm.std.tqdm.set_postfix"></a>
#### set\_postfix

```python
 | set_postfix(ordered_dict=None, refresh=True, **kwargs)
```

Set/modify postfix (additional stats)
with automatic formatting based on datatype.

Parameters
----------
ordered_dict  : dict or OrderedDict, optional
refresh  : bool, optional
    Forces refresh [default: True].
kwargs  : dict, optional

<a name="tqdm.std.tqdm.set_postfix_str"></a>
#### set\_postfix\_str

```python
 | set_postfix_str(s='', refresh=True)
```

Postfix without dictionary expansion, similar to prefix handling.

<a name="tqdm.std.tqdm.format_dict"></a>
#### format\_dict

```python
 | @property
 | format_dict()
```

Public API for read-only member access.

<a name="tqdm.std.tqdm.display"></a>
#### display

```python
 | display(msg=None, pos=None)
```

Use `self.sp` to display `msg` in the specified `pos`.

Consider overloading this function when inheriting to use e.g.:
`self.some_frontend(**self.format_dict)` instead of `self.sp`.

Parameters
----------
msg  : str, optional. What to display (default: `repr(self)`).
pos  : int, optional. Position to `moveto`
  (default: `abs(self.pos)`).

<a name="tqdm.std.tqdm.wrapattr"></a>
#### wrapattr

```python
 | @classmethod
 | @contextmanager
 | wrapattr(tclass, stream, method, total=None, bytes=True, **tkwargs)
```

stream  : file-like object.
method  : str, "read" or "write". The result of `read()` and
    the first argument of `write()` should have a `len()`.

>>> with tqdm.wrapattr(file_obj, "read", total=file_obj.size) as fobj:
...     while True:
...         chunk = fobj.read(chunk_size)
...         if not chunk:
...             break

