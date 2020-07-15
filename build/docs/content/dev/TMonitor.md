<a name="tqdm._monitor"></a>
# tqdm.\_monitor

<a name="tqdm._monitor.TMonitor"></a>
## TMonitor Objects

```python
class TMonitor(Thread)
```

Monitoring thread for tqdm bars.
Monitors if tqdm bars are taking too much time to display
and readjusts miniters automatically if necessary.

Parameters
----------
tqdm_cls  : class
    tqdm class to use (can be core tqdm or a submodule).
sleep_interval  : fload
    Time to sleep between monitoring checks.

