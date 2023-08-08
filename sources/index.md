<img align="right" src="https://tqdm.github.io/img/logo-trans.gif" />

# tqdm

[![PyPI-Versions](https://img.shields.io/pypi/pyversions/tqdm.svg?logo=python&logoColor=white)](https://pypi.org/project/tqdm)
[![PyPI-Status](https://img.shields.io/pypi/v/tqdm.svg?logo=PyPI&logoColor=white)](https://tqdm.github.io/releases)
[![Conda-Forge-Status](https://img.shields.io/conda/v/conda-forge/tqdm.svg?label=conda-forge&logo=conda-forge)](https://anaconda.org/conda-forge/tqdm)
<br/>
[![Docker](https://img.shields.io/badge/docker-pull-blue.svg?logo=docker&logoColor=white)](https://hub.docker.com/r/tqdm/tqdm)
[![Snapcraft](https://img.shields.io/badge/snap-install-82BEA0.svg?logo=snapcraft)](https://snapcraft.io/tqdm)
[![binder-demo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tqdm/tqdm/master?filepath=DEMO.ipynb)

[![Build-Status](https://img.shields.io/github/actions/workflow/status/tqdm/tqdm/test.yml?branch=master&label=tqdm&logo=GitHub)](https://github.com/tqdm/tqdm/actions/workflows/test.yml)
[![Coverage-Status](https://img.shields.io/coveralls/github/tqdm/tqdm/master?logo=coveralls)](https://coveralls.io/github/tqdm/tqdm)
[![Branch-Coverage-Status](https://codecov.io/gh/tqdm/tqdm/branch/master/graph/badge.svg)](https://codecov.io/gh/tqdm/tqdm)
[![Codacy-Grade](https://api.codacy.com/project/badge/Grade/3f965571598f44549c7818f29cdcf177)](https://www.codacy.com/app/tqdm/tqdm/dashboard)
<br/>
[![PyPI-Downloads](https://img.shields.io/pypi/dm/tqdm.svg?label=pypi%20downloads&logo=python&logoColor=white)](https://pepy.tech/project/tqdm)
[![Libraries-Rank](https://img.shields.io/librariesio/sourcerank/pypi/tqdm.svg?logo=koding&logoColor=white)](https://libraries.io/pypi/tqdm)
[![Repology](https://repology.org/badge/tiny-repos/python:tqdm.svg)](https://repology.org/project/python:tqdm/versions)
[![awesome-python](https://awesome.re/mentioned-badge.svg)](https://github.com/vinta/awesome-python)
[![README-Hits](https://caspersci.uk.to/cgi-bin/hits.cgi?q=tqdm&style=social&r=https://github.com/tqdm/tqdm&l=https://tqdm.github.io/img/favicon.png&f=https://tqdm.github.io/img/logo.gif)](https://caspersci.uk.to/cgi-bin/hits.cgi?q=tqdm&a=plot&r=https://github.com/tqdm/tqdm&l=https://tqdm.github.io/img/favicon.png&f=https://tqdm.github.io/img/logo.gif&style=social)
---

`tqdm` means "progress" in Arabic (*taqadum*, تقدّم) and is an
abbreviation for "I love you so much" in Spanish (*te quiero demasiado*).

Instantly make your loops show a smart progress meter - just wrap any
iterable with `tqdm(iterable)`, and you're done!

```python
from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
```

`76%|████████████████████████████         | 7568/10000 [00:33<00:10, 229.00it/s]`

`trange(N)` can be also used as a convenient shortcut for `tqdm(range(N))`.

![Screenshot](https://tqdm.github.io/img/tqdm.gif)

[![Video](https://tqdm.github.io/img/video.jpg)](/video) [![Slides](https://tqdm.github.io/img/slides.jpg
)](/PyData2019/slides.html) [![Merch](https://tqdm.github.io/img/merch.jpg)](/merch)

It can also be executed as a module with pipes:

```{.sh hl_lines="2 3 6"}
$ seq 9999999 | tqdm --bytes | wc -l
75.2MB [00:00, 217MB/s]
9999999
$ 7z a -bd -r backup.7z docs/ | grep Compressing | \
    tqdm --total $(find docs/ -type f | wc -l) --unit files >> backup.log
100%|███████████████████████████████▉| 8014/8014 [01:37<00:00, 82.29files/s]
```

Overhead is low -- about 60ns per iteration (80ns with `tqdm_gui`), and
is unit tested against performance regression. By comparison, the
well-established
[ProgressBar](https://github.com/niltonvolpato/python-progressbar) has
an 800ns/iter overhead.

In addition to its low overhead, `tqdm` uses smart algorithms to predict
the remaining time and to skip unnecessary iteration displays, which
allows for a negligible overhead in most cases.

`tqdm` works on any platform (Linux, Windows, Mac, FreeBSD, NetBSD,
Solaris/SunOS), in any console or in a GUI, and is also friendly with
IPython/Jupyter notebooks.

`tqdm` does not require any dependencies (not even `curses`!), just
Python and an environment supporting `carriage return \r` and
`line feed \n` control characters.

[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.595120-blue.svg)](https://doi.org/10.5281/zenodo.595120)
[![LICENCE](https://img.shields.io/pypi/l/tqdm.svg)](https://raw.githubusercontent.com/tqdm/tqdm/master/LICENCE)
[![OpenHub-Status](https://www.openhub.net/p/tqdm/widgets/project_thin_badge?format=gif)](https://www.openhub.net/p/tqdm?ref=Thin+badge)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3264/badge)](https://bestpractices.coreinfrastructure.org/projects/3264)
