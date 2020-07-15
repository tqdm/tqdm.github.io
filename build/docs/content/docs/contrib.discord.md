<a name="tqdm.contrib.discord"></a>
# tqdm.contrib.discord

Sends updates to a Discord bot.

<a name="tqdm.contrib.discord.tqdm_discord"></a>
## tqdm\_discord Objects

```python
class tqdm_discord(tqdm_auto)
```

Standard `tqdm.auto.tqdm` but also sends updates to a Discord Bot.
May take a few seconds to create (`__init__`).

- create a discord bot (not public, no requirement of OAuth2 code
  grant, only send message permissions) & invite it to a channel:
  https://discordpy.readthedocs.io/en/latest/discord.html
- copy the bot `{token}` & `{channel_id}` and paste below

>>> from tqdm.contrib.discord import tqdm, trange
>>> for i in tqdm(iterable, token='{token}', channel_id='{channel_id}'):
...     ...

<a name="tqdm.contrib.discord.tqdm_discord.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(*args, **kwargs)
```

Parameters
----------
token  : str, required. Discord token
    [default: ${TQDM_DISCORD_TOKEN}].
channel_id  : int, required. Discord channel ID
    [default: ${TQDM_DISCORD_CHANNEL_ID}].
mininterval  : float, optional.
  Minimum of [default: 1.5] to avoid rate limit.

See `tqdm.auto.tqdm.__init__` for other parameters.

<a name="tqdm.contrib.discord.tqdm_discord.__new__"></a>
#### \_\_new\_\_

```python
 | __new__(cls, *args, **kwargs)
```

Workaround for mixed-class same-stream nested progressbars.
See [`509`](https://github.com/tqdm/tqdm/issues/509)

