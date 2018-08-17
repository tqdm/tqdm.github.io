# tqdm documentation

Requires [pydoc-markdown](https://github.com/NiklasRosenstein/pydoc-markdown).
Assumes the following directory structure:

- tqdm: https://github.com/tqdm/tqdm.git
    - docs: https://github.com/tqdm/tqdm.github.io.git
    - wiki: https://github.com/tqdm/tqdm.wiki.git

```bash
tqdm/docs$ make serve
tqdm/docs$ make build  # generates static site in _build/site
```
