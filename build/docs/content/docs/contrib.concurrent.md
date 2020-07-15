<a name="tqdm.contrib.concurrent"></a>
# tqdm.contrib.concurrent

Thin wrappers around `concurrent.futures`.

<a name="tqdm.contrib.concurrent.thread_map"></a>
#### thread\_map

```python
thread_map(fn, *iterables, **tqdm_kwargs)
```

Equivalent of `list(map(fn, *iterables))`
driven by `concurrent.futures.ThreadPoolExecutor`.

Parameters
----------
tqdm_class : optional
    `tqdm` class to use for bars [default: tqdm.auto.tqdm].
max_workers : int, optional
    Maximum number of workers to spawn; passed to
    `concurrent.futures.ThreadPoolExecutor.__init__`.
    [default: max(32, cpu_count() + 4)].

<a name="tqdm.contrib.concurrent.process_map"></a>
#### process\_map

```python
process_map(fn, *iterables, **tqdm_kwargs)
```

Equivalent of `list(map(fn, *iterables))`
driven by `concurrent.futures.ProcessPoolExecutor`.

Parameters
----------
tqdm_class  : optional
    `tqdm` class to use for bars [default: tqdm.auto.tqdm].
max_workers : int, optional
    Maximum number of workers to spawn; passed to
    `concurrent.futures.ProcessPoolExecutor.__init__`.
    [default: min(32, cpu_count() + 4)].
chunksize : int, optional
    Size of chunks sent to worker processes; passed to
    `concurrent.futures.ProcessPoolExecutor.map`. [default: 1].

