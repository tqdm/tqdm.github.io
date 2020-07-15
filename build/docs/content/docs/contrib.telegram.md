<a name="tqdm.contrib.telegram"></a>
# tqdm.contrib.telegram

Sends updates to a Telegram bot.

<a name="tqdm.contrib.telegram.tqdm_telegram"></a>
## tqdm\_telegram Objects

```python
class tqdm_telegram(tqdm_auto)
```

Standard `tqdm.auto.tqdm` but also sends updates to a Telegram Bot.
May take a few seconds to create (`__init__`).

- create a bot https://core.telegram.org/bots#6-botfather
- copy its `{token}`
- add the bot to a chat and send it a message such as `/start`
- go to https://api.telegram.org/bot`{token}`/getUpdates to find out
  the `{chat_id}`
- paste the `{token}` & `{chat_id}` below

>>> from tqdm.contrib.telegram import tqdm, trange
>>> for i in tqdm(iterable, token='{token}', chat_id='{chat_id}'):
...     ...

<a name="tqdm.contrib.telegram.tqdm_telegram.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(*args, **kwargs)
```

Parameters
----------
token  : str, required. Telegram token
    [default: ${TQDM_TELEGRAM_TOKEN}].
chat_id  : str, required. Telegram chat ID
    [default: ${TQDM_TELEGRAM_CHAT_ID}].

See `tqdm.auto.tqdm.__init__` for other parameters.

<a name="tqdm.contrib.telegram.tqdm_telegram.__new__"></a>
#### \_\_new\_\_

```python
 | __new__(cls, *args, **kwargs)
```

Workaround for mixed-class same-stream nested progressbars.
See [`509`](https://github.com/tqdm/tqdm/issues/509)

