<a name="tqdm.keras"></a>
# tqdm.keras

<a name="tqdm.keras.TqdmCallback"></a>
## TqdmCallback Objects

```python
class TqdmCallback(keras.callbacks.Callback)
```

`keras` callback for epoch and batch progress

<a name="tqdm.keras.TqdmCallback.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(epochs=None, data_size=None, batch_size=None, verbose=1, tqdm_class=tqdm_auto)
```

Parameters
----------
epochs  : int, optional
data_size  : int, optional
    Number of training pairs.
batch_size  : int, optional
    Number of training pairs per batch.
verbose  : int
    0: epoch, 1: batch (transient), 2: batch. [default: 1].
    Will be set to `0` unless both `data_size` and `batch_size`
    are given.
tqdm_class : optional
    `tqdm` class to use for bars [default: `tqdm.auto.tqdm`].

