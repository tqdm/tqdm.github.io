![Logo](https://raw.githubusercontent.com/tqdm/tqdm/master/images/logo.gif)

tqdm
====

[![PyPI-Status](https://img.shields.io/pypi/v/tqdm.svg)](https://pypi.python.org/pypi/tqdm) [![PyPI-Versions](https://img.shields.io/pypi/pyversions/tqdm.svg)](https://pypi.python.org/pypi/tqdm) [![Conda-Forge-Status](https://anaconda.org/conda-forge/tqdm/badges/version.svg)](https://anaconda.org/conda-forge/tqdm)

[![Build-Status](https://travis-ci.org/tqdm/tqdm.svg?branch=master)](https://travis-ci.org/tqdm/tqdm) [![Coverage-Status](https://coveralls.io/repos/tqdm/tqdm/badge.svg?branch=master)](https://coveralls.io/github/tqdm/tqdm) [![Branch-Coverage-Status](https://codecov.io/gh/tqdm/tqdm/branch/master/graph/badge.svg)](https://codecov.io/gh/tqdm/tqdm) [![Codacy-Grade](https://api.codacy.com/project/badge/Grade/3f965571598f44549c7818f29cdcf177)](https://www.codacy.com/app/tqdm/tqdm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tqdm/tqdm&amp;utm_campaign=Badge_Grade)

[![DOI-URI](https://zenodo.org/badge/21637/tqdm/tqdm.svg)](https://zenodo.org/badge/latestdoi/21637/tqdm/tqdm) [![LICENCE](https://img.shields.io/pypi/l/tqdm.svg)](https://raw.githubusercontent.com/tqdm/tqdm/master/LICENCE) [![OpenHub-Status](https://www.openhub.net/p/tqdm/widgets/project_thin_badge?format=gif)](https://www.openhub.net/p/tqdm?ref=Thin+badge)

`tqdm` means "progress" in Arabic (taqadum, تقدّم) and an abbreviation for "I love you so much" in Spanish (te quiero demasiado).

Instantly make your loops show a smart progress meter - just wrap any iterable with `tqdm(iterable)`, and you're done!

``` sourceCode
from tqdm import tqdm
for i in tqdm(range(10000)):
    ...
```

`76%|████████████████████████████         | 7568/10000 [00:33<00:10, 229.00it/s]`

`trange(N)` can be also used as a convenient shortcut for `tqdm(xrange(N))`.

![Screenshot](https://raw.githubusercontent.com/tqdm/tqdm/master/images/tqdm.gif)  
REPL: [ptpython](https://github.com/jonathanslenders/ptpython)

It can also be executed as a module with pipes:

``` sourceCode
$ seq 9999999 | tqdm --unit_scale | wc -l
10.0Mit [00:02, 3.58Mit/s]
9999999
$ 7z a -bd -r backup.7z docs/ | grep Compressing | \
    tqdm --total $(find docs/ -type f | wc -l) --unit files >> backup.log
100%|███████████████████████████████▉| 8014/8014 [01:37<00:00, 82.29files/s]
```

Overhead is low -- about 60ns per iteration (80ns with `tqdm_gui`), and is unit tested against performance regression. By comparison, the well-established [ProgressBar](https://github.com/niltonvolpato/python-progressbar) has an 800ns/iter overhead.

In addition to its low overhead, `tqdm` uses smart algorithms to predict the remaining time and to skip unnecessary iteration displays, which allows for a negligible overhead in most cases.

`tqdm` works on any platform (Linux, Windows, Mac, FreeBSD, NetBSD, Solaris/SunOS), in any console or in a GUI, and is also friendly with IPython/Jupyter notebooks.

`tqdm` does not require any dependencies (not even `curses`!), just Python and an environment supporting `carriage return \r` and `line feed \n` control characters.
