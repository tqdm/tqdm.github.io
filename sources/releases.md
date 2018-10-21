# [tqdm/tqdm](https://github.com/tqdm/tqdm) Releases

## [v4.28.1](https://github.com/tqdm/tqdm/releases/tag/v4.28.1) <small><small>(2018-10-21)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.28.1/tqdm-4.28.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.28.1/tqdm-4.28.1-py2.py3-none-any.whl.asc)


- fix `--manpath` file not found
- expose `main():argv`
- add unit tests
- release framework tidy
  + update .`gitattributes`
  + remove deprecated `make`/`dist` options

## [v4.28.0](https://github.com/tqdm/tqdm/releases/tag/v4.28.0) <small><small>(2018-10-20)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.28.0/tqdm-4.28.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.28.0/tqdm-4.28.0-py2.py3-none-any.whl.asc)


- remove installation of man pages by default ([#460], [#628])
- CLI:add `--manpath` option ([#629])
- documentation additions and fixes

[#460]: https://github.com/tqdm/tqdm/issues/460
[#628]: https://github.com/tqdm/tqdm/issues/628
[#629]: https://github.com/tqdm/tqdm/issues/629

## [v4.27.0](https://github.com/tqdm/tqdm/releases/tag/v4.27.0) <small><small>(2018-10-15)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.27.0/tqdm-4.27.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.27.0/tqdm-4.27.0-py2.py3-none-any.whl.asc)


- fix `str.isnumeric` [#605]
- fix `WeakSet` `KeyError` [#548], [#553], [#596] -> [#607]
- stop `tqdm_notebook` description truncation [#582] -> [#599]
- include `unit_scale` for `rate` [#608]
- add `auto` -> nowarning `autonotebook`
- add better postfix numeric formatting [#621]
- minor refactoring [#609] -> [#616]
- update documentation
- add unit tests
- fix py26 CI

[#605]: https://github.com/tqdm/tqdm/issues/605
[#548]: https://github.com/tqdm/tqdm/issues/548
[#553]: https://github.com/tqdm/tqdm/issues/553
[#596]: https://github.com/tqdm/tqdm/issues/596
[#607]: https://github.com/tqdm/tqdm/issues/607
[#582]: https://github.com/tqdm/tqdm/issues/582
[#599]: https://github.com/tqdm/tqdm/issues/599
[#608]: https://github.com/tqdm/tqdm/issues/608
[#621]: https://github.com/tqdm/tqdm/issues/621
[#609]: https://github.com/tqdm/tqdm/issues/609
[#616]: https://github.com/tqdm/tqdm/issues/616

## [v4.26.0](https://github.com/tqdm/tqdm/releases/tag/v4.26.0) <small><small>(2018-09-11)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.26.0/tqdm-4.26.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.26.0/tqdm-4.26.0-py2.py3-none-any.whl.asc)


- fix `smoothing` ([#566] -> [#601])
- `pandas` updates
    + address the `FutureWarning` in `pandas`, drop `pandas` test in py34, add in py37 ([#603])
    + support `pandas` `axis='index' or 'columns'` ([#570])
- minor documentation updates ([#597], [#600], [#606])
    + developer notes

[#566]: https://github.com/tqdm/tqdm/issues/566
[#601]: https://github.com/tqdm/tqdm/issues/601
[#603]: https://github.com/tqdm/tqdm/issues/603
[#570]: https://github.com/tqdm/tqdm/issues/570
[#597]: https://github.com/tqdm/tqdm/issues/597
[#600]: https://github.com/tqdm/tqdm/issues/600
[#606]: https://github.com/tqdm/tqdm/issues/606

## [v4.25.0](https://github.com/tqdm/tqdm/releases/tag/v4.25.0) <small><small>(2018-08-20)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.25.0/tqdm-4.25.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.25.0/tqdm-4.25.0-py2.py3-none-any.whl.asc)


- stop monitor on shutdown ([#571], [#572])
- fix `find_packages()` for submodules ([#593])
    + properly add `autonotebook` ([#586], 1cf3393)
- ignore ANSI escape codes in the bar length calculation ([#450], [#591] -> [#592])
- update documentation ([#243])

[#571]: https://github.com/tqdm/tqdm/issues/571
[#572]: https://github.com/tqdm/tqdm/issues/572
[#593]: https://github.com/tqdm/tqdm/issues/593
[#586]: https://github.com/tqdm/tqdm/issues/586
[#450]: https://github.com/tqdm/tqdm/issues/450
[#591]: https://github.com/tqdm/tqdm/issues/591
[#592]: https://github.com/tqdm/tqdm/issues/592
[#243]: https://github.com/tqdm/tqdm/issues/243

## [v4.24.0](https://github.com/tqdm/tqdm/releases/tag/v4.24.0) <small><small>(2018-07-26)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.24.0/tqdm-4.24.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.24.0/tqdm-4.24.0-py2.py3-none-any.whl.asc)


- `autonotebook` submodule for automatic selection of notebook/CLI bar ([#443], [#508])
    + update/add `pandas()` example documentation ([#474])
- `NameError:IntProgress` changed to a more helpful `ImportError` ([#187], [#451], [#558])
- support `bool()` cast when `disable=True` ([#574])
- fix `format_sizeof` hundreds rounding ([#579] -> [#581])
- ensure URLs in documentation are secure (`https`)

[#443]: https://github.com/tqdm/tqdm/issues/443
[#508]: https://github.com/tqdm/tqdm/issues/508
[#474]: https://github.com/tqdm/tqdm/issues/474
[#187]: https://github.com/tqdm/tqdm/issues/187
[#451]: https://github.com/tqdm/tqdm/issues/451
[#558]: https://github.com/tqdm/tqdm/issues/558
[#574]: https://github.com/tqdm/tqdm/issues/574
[#579]: https://github.com/tqdm/tqdm/issues/579
[#581]: https://github.com/tqdm/tqdm/issues/581

## [v4.23.4](https://github.com/tqdm/tqdm/releases/tag/v4.23.4) <small><small>(2018-05-22)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.23.4/tqdm-4.23.4-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.23.4/tqdm-4.23.4-py2.py3-none-any.whl.asc)


- Support pandas 0.23.0 `core.groupby` module layout ([#555] -> [#554])
- Add python_requires to help pip ([#557])
- minor maintenance updates
  + CI updates: drop travis py33 due to `tox` ([tox-dev/tox#648])
  + minor code tidy

[#555]: https://github.com/tqdm/tqdm/issues/555
[#554]: https://github.com/tqdm/tqdm/issues/554
[#557]: https://github.com/tqdm/tqdm/issues/557
[#648]: https://github.com/tqdm/tqdm/issues/648
[tox-dev/tox#648]: https://github.com/tox-dev/tox/issues/648

## [v4.23.3](https://github.com/tqdm/tqdm/releases/tag/v4.23.3) <small><small>(2018-05-22)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.23.3/tqdm-4.23.3-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.23.3/tqdm-4.23.3-py2.py3-none-any.whl.asc)


- suppress 10 second warning (refix [#323])

[#323]: https://github.com/tqdm/tqdm/issues/323

## [v4.23.2](https://github.com/tqdm/tqdm/releases/tag/v4.23.2) <small><small>(2018-05-02)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.23.2/tqdm-4.23.2-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.23.2/tqdm-4.23.2-py2.py3-none-any.whl.asc)


- minor import syntax fix [#496]
- re-fix nested overlaps [#477]
- update documentation and examples
- code tidy and abstraction

[#496]: https://github.com/tqdm/tqdm/issues/496
[#477]: https://github.com/tqdm/tqdm/issues/477

## [v4.23.1](https://github.com/tqdm/tqdm/releases/tag/v4.23.1) <small><small>(2018-04-25)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.23.1/tqdm-4.23.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.23.1/tqdm-4.23.1-py2.py3-none-any.whl.asc)


- fix `AttributeError`s ([#546])
    + `pos`  on initialisation ([#323], [#510] -> [#544])
    + `fp` on `write()` ([#383])
- fix py34 CI
- update documentation

[#546]: https://github.com/tqdm/tqdm/issues/546
[#323]: https://github.com/tqdm/tqdm/issues/323
[#510]: https://github.com/tqdm/tqdm/issues/510
[#544]: https://github.com/tqdm/tqdm/issues/544
[#383]: https://github.com/tqdm/tqdm/issues/383

## [v4.23.0](https://github.com/tqdm/tqdm/releases/tag/v4.23.0) <small><small>(2018-04-15)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.23.0/tqdm-4.23.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.23.0/tqdm-4.23.0-py2.py3-none-any.whl.asc)


- Fix `disable=True` where`iterable` has no `len()` and is not `None`  ([#539])
- Add `ncols` to specify `tqdm_notebook` bar width ([#276] -> [#292])
- allow custom `pandas` `total` ([#364] -> [#535])
- Add `progress_apply` for `pandas.(Series|DataFrame).(rolling|expanding)` ([#530] -> [#537])
- unit tests, pep8 tidy
- `postfix` non-`dict` documentation note

[#539]: https://github.com/tqdm/tqdm/issues/539
[#276]: https://github.com/tqdm/tqdm/issues/276
[#292]: https://github.com/tqdm/tqdm/issues/292
[#364]: https://github.com/tqdm/tqdm/issues/364
[#535]: https://github.com/tqdm/tqdm/issues/535
[#530]: https://github.com/tqdm/tqdm/issues/530
[#537]: https://github.com/tqdm/tqdm/issues/537

## [v4.22.0](https://github.com/tqdm/tqdm/releases/tag/v4.22.0) <small><small>(2018-04-11)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.22.0/tqdm-4.22.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.22.0/tqdm-4.22.0-py2.py3-none-any.whl.asc)


- allow direct non-string assignment to `postfix` member (lists, dicts, etc) ([#382] -> [#534])
- documentation updates
- unit tests

[#382]: https://github.com/tqdm/tqdm/issues/382
[#534]: https://github.com/tqdm/tqdm/issues/534

## [v4.21.0](https://github.com/tqdm/tqdm/releases/tag/v4.21.0) <small><small>(2018-04-08)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.21.0/tqdm-4.21.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.21.0/tqdm-4.21.0-py2.py3-none-any.whl.asc)


- fix [#532] `write()` with manual `position`
  + more robust free position finding
- add `TqdmWarning` base class
- fix GUI `__del__()`
  + add `TqdmExperimentalWarning`
- add, tidy & fix unit tests
- documentation
  + wiki release notes
  + update contributors
  + fix `7zx` example

[#532]: https://github.com/tqdm/tqdm/issues/532

## [v4.20.0](https://github.com/tqdm/tqdm/releases/tag/v4.20.0) <small><small>(2018-04-03)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.20.0/tqdm-4.20.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.20.0/tqdm-4.20.0-py2.py3-none-any.whl.asc)


- `pandas` wrapper: remove `*args` and add better `total` handling ([#244], [#299], [#322], [#366] -> [#524])
- document windows unicode know issues ([#454])
- suppress `RuntimeError: Set changed size during iteration` -> `TqdmSynchronisationWarning` ([#481])

[#244]: https://github.com/tqdm/tqdm/issues/244
[#299]: https://github.com/tqdm/tqdm/issues/299
[#322]: https://github.com/tqdm/tqdm/issues/322
[#366]: https://github.com/tqdm/tqdm/issues/366
[#524]: https://github.com/tqdm/tqdm/issues/524
[#454]: https://github.com/tqdm/tqdm/issues/454
[#481]: https://github.com/tqdm/tqdm/issues/481

## [v4.19.9](https://github.com/tqdm/tqdm/releases/tag/v4.19.9) <small><small>(2018-03-27)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.9/tqdm-4.19.9-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.9/tqdm-4.19.9-py2.py3-none-any.whl.asc)


- fix monitor thread termination and update tests ([#527])

[#527]: https://github.com/tqdm/tqdm/issues/527

## [v4.19.8](https://github.com/tqdm/tqdm/releases/tag/v4.19.8) <small><small>(2018-03-27)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.8/tqdm-4.19.8-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.8/tqdm-4.19.8-py2.py3-none-any.whl.asc)


- fix monitoring thread issues
  + avoid uninitialised instance manipulation ([#493])
  + fix thread starting `RuntimeError` ([#522] -> [#523])
- these release notes ([#529])

[#493]: https://github.com/tqdm/tqdm/issues/493
[#522]: https://github.com/tqdm/tqdm/issues/522
[#523]: https://github.com/tqdm/tqdm/issues/523
[#529]: https://github.com/tqdm/tqdm/issues/529

## [v4.19.6](https://github.com/tqdm/tqdm/releases/tag/v4.19.6) <small><small>(2018-02-27)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.6/tqdm-4.19.6-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.6/tqdm-4.19.6-py2.py3-none-any.whl.asc)


- CLI improvements
    + `--bytes` implies `--unit B --unit_scale --unit_divisor 1024` ([#503])
    + allow hyphens in CLI arguments ([#511])
- synchronisation: fix for `sem_open` on `aarch64` ([#513])
- framework update
    + CI/tests, year 2018, py37, badges, documentation

[#503]: https://github.com/tqdm/tqdm/issues/503
[#511]: https://github.com/tqdm/tqdm/issues/511
[#513]: https://github.com/tqdm/tqdm/issues/513

## [v4.19.5](https://github.com/tqdm/tqdm/releases/tag/v4.19.5) <small><small>(2017-12-10)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.5/tqdm-4.19.5-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.5/tqdm-4.19.5-py2.py3-none-any.whl.asc)


- multiprocess/lock fixes ([#457])
- `set_description` in notebook ([#345] -> [#475])
- minor tidy ([#476])
- documentation updates

[#457]: https://github.com/tqdm/tqdm/issues/457
[#345]: https://github.com/tqdm/tqdm/issues/345
[#475]: https://github.com/tqdm/tqdm/issues/475
[#476]: https://github.com/tqdm/tqdm/issues/476

## [v4.19.4](https://github.com/tqdm/tqdm/releases/tag/v4.19.4) <small><small>(2017-10-15)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.4/tqdm-4.19.4-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.4/tqdm-4.19.4-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.19.4/tqdm-4.19.4.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.4/tqdm-4.19.4.tar.gz.asc)


- fix `Lock:NotImplementedError` on certain systems ([#466] -> [#468])
- use recursive locks ([#469] -> [#468])
    - fix deadlocks
- tidy ([#448])
- `flush()` on `moveto()` ([#398] -> [#399], [#420], [#467])
- update tests and benchmarks

[#466]: https://github.com/tqdm/tqdm/issues/466
[#468]: https://github.com/tqdm/tqdm/issues/468
[#469]: https://github.com/tqdm/tqdm/issues/469
[#468]: https://github.com/tqdm/tqdm/issues/468
[#448]: https://github.com/tqdm/tqdm/issues/448
[#398]: https://github.com/tqdm/tqdm/issues/398
[#399]: https://github.com/tqdm/tqdm/issues/399
[#420]: https://github.com/tqdm/tqdm/issues/420
[#467]: https://github.com/tqdm/tqdm/issues/467

## [v4.19.2](https://github.com/tqdm/tqdm/releases/tag/v4.19.2) <small><small>(2017-10-08)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.2/tqdm-4.19.2-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.2/tqdm-4.19.2-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.19.2/tqdm-4.19.2.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.2/tqdm-4.19.2.tar.gz.asc)


- `flush()` on `refresh()` ([#459] from [#317])
- status printer updates ([#331])
    + use `sp()` in `refresh()`
    + remove redundant `clear():nomove=False`
- misc minor documentation updates
- unit tests

[#459]: https://github.com/tqdm/tqdm/issues/459
[#317]: https://github.com/tqdm/tqdm/issues/317
[#331]: https://github.com/tqdm/tqdm/issues/331

## [v4.19.1](https://github.com/tqdm/tqdm/releases/tag/v4.19.1) <small><small>(2017-10-03)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.19.1/tqdm-4.19.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.1/tqdm-4.19.1-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.19.1/tqdm-4.19.1.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.19.1/tqdm-4.19.1.tar.gz.asc)


- `rate_(no)inv(_fmt)` ([#72], b228bc3)
- `__repr__()` tidy ([#389])
- fix `write()` before initialisation `AttributeError: _lock` ([#457])
- `man` pages
- documentation updates

[#72]: https://github.com/tqdm/tqdm/issues/72
[#389]: https://github.com/tqdm/tqdm/issues/389
[#457]: https://github.com/tqdm/tqdm/issues/457

## [v4.18.0](https://github.com/tqdm/tqdm/releases/tag/v4.18.0) <small><small>(2017-09-30)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.18.0/tqdm-4.18.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.18.0/tqdm-4.18.0-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.18.0/tqdm-4.18.0.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.18.0/tqdm-4.18.0.tar.gz.asc)


- Thread safety! ([#285] -> [#291] -> [#329], [#407], [#417])
- Ease redirection of `sys.stdout`/`stderr` ([#422])
- Minor internal stream bugfix ([#439])
- `AttributeError` fixes ([#323], [#324], [#418])

Related to:

- Misc bugs ([#334])
- `concurrent.futures` ([#97])
- Multi-`tqdm` ([#143])
- `flush()` and `refresh()` ([#331])
- Newline on `refresh()` ([#361])
- Nested trees ([#384])
- Manually positioned nested bars clearing ([#385])

[#285]: https://github.com/tqdm/tqdm/issues/285
[#291]: https://github.com/tqdm/tqdm/issues/291
[#329]: https://github.com/tqdm/tqdm/issues/329
[#407]: https://github.com/tqdm/tqdm/issues/407
[#417]: https://github.com/tqdm/tqdm/issues/417
[#422]: https://github.com/tqdm/tqdm/issues/422
[#439]: https://github.com/tqdm/tqdm/issues/439
[#323]: https://github.com/tqdm/tqdm/issues/323
[#324]: https://github.com/tqdm/tqdm/issues/324
[#418]: https://github.com/tqdm/tqdm/issues/418
[#334]: https://github.com/tqdm/tqdm/issues/334
[#97]: https://github.com/tqdm/tqdm/issues/97
[#143]: https://github.com/tqdm/tqdm/issues/143
[#331]: https://github.com/tqdm/tqdm/issues/331
[#361]: https://github.com/tqdm/tqdm/issues/361
[#384]: https://github.com/tqdm/tqdm/issues/384
[#385]: https://github.com/tqdm/tqdm/issues/385

## [v4.17.1](https://github.com/tqdm/tqdm/releases/tag/v4.17.1) <small><small>(2017-09-26)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.17.1/tqdm-4.17.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.17.1/tqdm-4.17.1-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.17.1/tqdm-4.17.1.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.17.1/tqdm-4.17.1.tar.gz.asc)


- initialise `n` even when disabled ([#438])
- better unicode detection ([#437])
- `__repr__()` bugfix ([#441])

[#438]: https://github.com/tqdm/tqdm/issues/438
[#437]: https://github.com/tqdm/tqdm/issues/437
[#441]: https://github.com/tqdm/tqdm/issues/441

## [v4.17.0](https://github.com/tqdm/tqdm/releases/tag/v4.17.0) <small><small>(2017-09-20)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.17.0/tqdm-4.17.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.17.0/tqdm-4.17.0-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.17.0/tqdm-4.17.0.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.17.0/tqdm-4.17.0.tar.gz.asc)


- easier redirect of `stdout` ([#426] -> [#431])
    - `cls.external_write_mode() @contextmanager`
- `refresh=True` for `set_description`/`update`(`_str`) ([#317] -> [#377])

[#426]: https://github.com/tqdm/tqdm/issues/426
[#431]: https://github.com/tqdm/tqdm/issues/431
[#317]: https://github.com/tqdm/tqdm/issues/317
[#377]: https://github.com/tqdm/tqdm/issues/377

## [v4.16.0](https://github.com/tqdm/tqdm/releases/tag/v4.16.0) <small><small>(2017-09-20)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.16.0/tqdm-4.16.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.16.0/tqdm-4.16.0-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.16.0/tqdm-4.16.0.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.16.0/tqdm-4.16.0.tar.gz.asc)


- more formatting control ([#347] -> [#362])
    - `set_postfix_str()`, `set_description_str()`
    - move `": "` to `bar_format`
    - complements [#266], [#270]
- better CLI support (e.g. hyphenated paths) ([#421] [#423] -> [#424])
- more unit tests ([#411])
    - upgrade to pypy2/3-5.8.0
    - add py37-dev
- doc updates

[#347]: https://github.com/tqdm/tqdm/issues/347
[#362]: https://github.com/tqdm/tqdm/issues/362
[#266]: https://github.com/tqdm/tqdm/issues/266
[#270]: https://github.com/tqdm/tqdm/issues/270
[#421]: https://github.com/tqdm/tqdm/issues/421
[#423]: https://github.com/tqdm/tqdm/issues/423
[#424]: https://github.com/tqdm/tqdm/issues/424
[#411]: https://github.com/tqdm/tqdm/issues/411

## [v4.15.0](https://github.com/tqdm/tqdm/releases/tag/v4.15.0) <small><small>(2017-07-29)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.15.0/tqdm-4.15.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.15.0/tqdm-4.15.0-py2.py3-none-any.whl.asc)


- minor fixes ([#395])
- minor documentation updates ([#400], [#401], [#412])
- better `pandas` support ([#351] -> [#409])
- Jupyter notebook fix ([#352], [#369] -> [#373], [#405])
- optimise `setcheckinterval`/`setswitchinterval` ([#376])
- add `unit_scale` ([#273], [#295] -> [#378])

[#395]: https://github.com/tqdm/tqdm/issues/395
[#400]: https://github.com/tqdm/tqdm/issues/400
[#401]: https://github.com/tqdm/tqdm/issues/401
[#412]: https://github.com/tqdm/tqdm/issues/412
[#351]: https://github.com/tqdm/tqdm/issues/351
[#409]: https://github.com/tqdm/tqdm/issues/409
[#352]: https://github.com/tqdm/tqdm/issues/352
[#369]: https://github.com/tqdm/tqdm/issues/369
[#373]: https://github.com/tqdm/tqdm/issues/373
[#405]: https://github.com/tqdm/tqdm/issues/405
[#376]: https://github.com/tqdm/tqdm/issues/376
[#273]: https://github.com/tqdm/tqdm/issues/273
[#295]: https://github.com/tqdm/tqdm/issues/295
[#378]: https://github.com/tqdm/tqdm/issues/378

## [v4.14.0](https://github.com/tqdm/tqdm/releases/tag/v4.14.0) <small><small>(2017-07-29)</small></small>

- add `unit_divisor` [#354] -> [#356] 
- update examples

[#354]: https://github.com/tqdm/tqdm/issues/354
[#356]: https://github.com/tqdm/tqdm/issues/356

## [v4.13.0](https://github.com/tqdm/tqdm/releases/tag/v4.13.0) <small><small>(2017-05-29)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.13.0/tqdm-4.13.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.13.0/tqdm-4.13.0-py2.py3-none-any.whl.asc)


- support unknown systems https://github.com/warner/magic-wormhole/issues/158, [#76], [#344] -> [#390]
- support nested/multi-bars better [#384], [#285], [#329] -> [#385]
- ease redirection of output (default: `sys.stderr` -> `None`) https://github.com/xonsh/xonsh/issues/2058, [#329], [#275] -> [#293]
    + add [examples/redirect_print.py](https://github.com/tqdm/tqdm/blob/master/examples/redirect_print.py)
- minor documentation updates

[#76]: https://github.com/tqdm/tqdm/issues/76
[#344]: https://github.com/tqdm/tqdm/issues/344
[#390]: https://github.com/tqdm/tqdm/issues/390
[#384]: https://github.com/tqdm/tqdm/issues/384
[#285]: https://github.com/tqdm/tqdm/issues/285
[#329]: https://github.com/tqdm/tqdm/issues/329
[#385]: https://github.com/tqdm/tqdm/issues/385
[#329]: https://github.com/tqdm/tqdm/issues/329
[#275]: https://github.com/tqdm/tqdm/issues/275
[#293]: https://github.com/tqdm/tqdm/issues/293

## [v4.12.0](https://github.com/tqdm/tqdm/releases/tag/v4.12.0) <small><small>(2017-05-29)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.12.0/tqdm-4.12.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.12.0/tqdm-4.12.0-py2.py3-none-any.whl.asc)


- fix monitor race condition [#338] -> [#339]
- add explicit NetBSD support [#344]
- documentation tidy

[#338]: https://github.com/tqdm/tqdm/issues/338
[#339]: https://github.com/tqdm/tqdm/issues/339
[#344]: https://github.com/tqdm/tqdm/issues/344

## [v4.11.2](https://github.com/tqdm/tqdm/releases/tag/v4.11.2) <small><small>(2017-01-24)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.11.2/tqdm-4.11.2-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.11.2/tqdm-4.11.2-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.11.2/tqdm-4.11.2.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.11.2/tqdm-4.11.2.tar.gz.asc)


- thread safety [#332]
- address `DeprecationWarning` [#319] -> [#326]
- version extra [#328] -> [#330]
  - security fix
  - add non-master branch name
- minor safety
- minor documentation and comments

[#332]: https://github.com/tqdm/tqdm/issues/332
[#319]: https://github.com/tqdm/tqdm/issues/319
[#326]: https://github.com/tqdm/tqdm/issues/326
[#328]: https://github.com/tqdm/tqdm/issues/328
[#330]: https://github.com/tqdm/tqdm/issues/330

## [v4.11.1](https://github.com/tqdm/tqdm/releases/tag/v4.11.1) <small><small>(2017-01-23)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.11.1/tqdm-4.11.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.11.1/tqdm-4.11.1-py2.py3-none-any.whl.asc)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.11.1/tqdm-4.11.1.tar.gz)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.11.1/tqdm-4.11.1.tar.gz.asc)


Officially support Python 3.6, addressing [#333]

[#333]: https://github.com/tqdm/tqdm/issues/333

## [v4.11.0](https://github.com/tqdm/tqdm/releases/tag/v4.11.0) <small><small>(2017-01-12)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.11.0/tqdm-4.11.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.11.0/tqdm-4.11.0.tar.gz)


- `postfix` argument added [#266]->[#270] 
- fix tests for
  - `numpy` [#272]->[#302]
  - `PyPy3` [#318]->[#325]
- `7z` extraction example script
- new logo [#315] 
- hit counter with logo colours and stats
- documentation updates
- safer `setup.py` `Makefile` emulation
- better github contributions integrations and Code of Conduct [#310]

[#266]: https://github.com/tqdm/tqdm/issues/266
[#270]: https://github.com/tqdm/tqdm/issues/270
[#272]: https://github.com/tqdm/tqdm/issues/272
[#302]: https://github.com/tqdm/tqdm/issues/302
[#318]: https://github.com/tqdm/tqdm/issues/318
[#325]: https://github.com/tqdm/tqdm/issues/325
[#315]: https://github.com/tqdm/tqdm/issues/315
[#310]: https://github.com/tqdm/tqdm/issues/310

## [v4.10.0](https://github.com/tqdm/tqdm/releases/tag/v4.10.0) <small><small>(2016-11-12)</small></small>
[gz](https://github.com/tqdm/tqdm/releases/download/v4.10.0/tqdm-4.10.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.10.0/tqdm-4.10.0.zip)


- fix maxinterval to adjust miniters to mininterval [#249]
- minor bugfixes (eg [#288])
- misc optimisations, unit tests, and benchmarks (eg [#298])
- documentation updates

[#249]: https://github.com/tqdm/tqdm/issues/249
[#288]: https://github.com/tqdm/tqdm/issues/288
[#298]: https://github.com/tqdm/tqdm/issues/298

## [v4.9.0](https://github.com/tqdm/tqdm/releases/tag/v4.9.0) <small><small>(2016-10-31)</small></small>
[gz](https://github.com/tqdm/tqdm/releases/download/v4.9.0/tqdm-4.9.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.9.0/tqdm-4.9.0.zip)


- monitoring thread to automatically to adjust `miniters` and avoid exceeding `maxinterval`
  - test race conditions
  - kill on KeyboardInterrupt + instant refresh
  - low performance overhead, option to disable
- new CLI argument: `--bytes` to count chars
- disable automatically on non-TTY ([#281])
- fixed `refresh()` and `clear()` if disabled ([#286])
- misc fixes
- documentation
- unit tests
- optimisations, style fixes
- codacy badge
- safety and warning suppression
- ignore coverall failures ([#283])
- fix broken link in README ([#262])
- Fix `time()` in `refresh()` + avoid `write()` races ([#264])
- Fix `__repr__()` [#269]
- Fix `update(0)` causing `ZeroDivisionError` (on first call) [#268]
- Faster simple bar for perf test ([#257])
- cleaner `tqdm_notebook` exit when not run in a notebook ([#267])
- Disable coveralls because of duplicate comments on github ([#263])
- Migrate codecov config -> codecov.yml

[#281]: https://github.com/tqdm/tqdm/issues/281
[#286]: https://github.com/tqdm/tqdm/issues/286
[#283]: https://github.com/tqdm/tqdm/issues/283
[#262]: https://github.com/tqdm/tqdm/issues/262
[#264]: https://github.com/tqdm/tqdm/issues/264
[#269]: https://github.com/tqdm/tqdm/issues/269
[#268]: https://github.com/tqdm/tqdm/issues/268
[#257]: https://github.com/tqdm/tqdm/issues/257
[#267]: https://github.com/tqdm/tqdm/issues/267
[#263]: https://github.com/tqdm/tqdm/issues/263

## [v4.8.4](https://github.com/tqdm/tqdm/releases/tag/v4.8.4) <small><small>(2016-08-17)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.8.4/tqdm-4.8.4-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.8.4/tqdm-4.8.4.tar.gz)


- 14% overhead reduction
- fix exception when closing `tqdm_notebook` without a `total`
- support more pandas modules
  - pandas.Series.progress_map
  - pandas.DataFrame.progress_applymap
  - Panel.progress_apply
  - PanelGroupBy.progress_apply
  - GroupBy.progress_aggregate
  - GroupBy.progress_transform
- faster CI builds
- misc documentation update and link to wiki

## [v4.8.1](https://github.com/tqdm/tqdm/releases/tag/v4.8.1) <small><small>(2016-07-25)</small></small>

- custom tqdm warning/exceptions
- tests now multiprocessed and include pandas

## [v4.8.0](https://github.com/tqdm/tqdm/releases/tag/v4.8.0) <small><small>(2016-07-25)</small></small>

- `tqdm.pandas` classmethod replaces `tqdm_pandas` function (deprecated)
- `ipython` aliased imports fixes
- `write` without any instances
- readme update
- examples update
- test fixes and updates

## [v4.7.6](https://github.com/tqdm/tqdm/releases/tag/v4.7.6) <small><small>(2016-06-30)</small></small>

- support for pandas series
- support for numpy arrays
- tidy & coverage

## [v4.7.4](https://github.com/tqdm/tqdm/releases/tag/v4.7.4) <small><small>(2016-06-04)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.7.4/tqdm-4.7.4-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.7.4/tqdm-4.7.4.tar.gz)


- `pandas.DataFrame.apply` support
- `tqdm_notebook.write()`
- `tqdm_gui.write()`
- misc notebook fixes
- delay notebook imports (>80% reduction in import time when unused)
- optional `colorama` only on windows
- documentation tidy
- more & faster tests

## [v4.7.0](https://github.com/tqdm/tqdm/releases/tag/v4.7.0) <small><small>(2016-05-15)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.7.0/tqdm-4.7.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.7.0/tqdm-4.7.0.tar.gz)


- CLI custom delimiter support
- More robust CLI argument parsing
  - either one or two `-` preceding kwargs (eg `-ascii` or `--ascii`)
  - no positional args (so no need to quote multi-word `-desc` for example)
  - `bool` kwargs with implicit value=`True` still supported
  - optional `=` sign after kwargs
- tests
- doc updates, badges
  - pyversions, doi, licence, github

## [v4.6.2](https://github.com/tqdm/tqdm/releases/tag/v4.6.2) <small><small>(2016-05-15)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.6.2/tqdm-4.6.2-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.6.2/tqdm-4.6.2.tar.gz)|[exe](https://github.com/tqdm/tqdm/releases/download/v4.6.2/tqdm-4.6.2.win32.exe)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.6.2/tqdm-4.6.2.zip)


- Fix warnings due to IPython/Jupyter widget

## [v4.6.1](https://github.com/tqdm/tqdm/releases/tag/v4.6.1) <small><small>(2016-05-15)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.6.1/tqdm-4.6.1-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.6.1/tqdm-4.6.1.tar.gz)|[exe](https://github.com/tqdm/tqdm/releases/download/v4.6.1/tqdm-4.6.1.win32.exe)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.6.1/tqdm-4.6.1.zip)


- add IPython/Jupyter support
- fix `{bar}` length breaking display when using custom `bar_format`
- add a no inversion rate formatting for `bar_format` (i.e., always show `it/s` and never `s/it`)

## [v4.5.0](https://github.com/tqdm/tqdm/releases/tag/v4.5.0) <small><small>(2016-04-25)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.5.0/tqdm-4.5.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.5.0/tqdm-4.5.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.5.0/tqdm-4.5.0.zip)


- print messages within (nested) loops using `tqdm.write(...)`

## [v4.4.3](https://github.com/tqdm/tqdm/releases/tag/v4.4.3) <small><small>(2016-04-24)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.4.3/tqdm-4.4.3-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.4.3/tqdm-4.4.3.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.4.3/tqdm-4.4.3.zip)


- remove `docopt` dependency for CLI
- re-added `update(0)` ability to trigger refresh
- minor fixes
  - re-added (OSI approved) licence to source
  - dev versioning auto-fallback
- slight speed optimisation
- tests
- documentation

## [v4.4.1](https://github.com/tqdm/tqdm/releases/tag/v4.4.1) <small><small>(2016-04-22)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.4.1/tqdm-4.4.1-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.4.1/tqdm-4.4.1.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.4.1/tqdm-4.4.1.zip)


- Module execution in CLI pipes!
  - `tqdm` executable
  - documentation
  - tests
- MSYS aded to supported envs
- better VTE support
- dev versioning
- tests

## [v4.2.0](https://github.com/tqdm/tqdm/releases/tag/v4.2.0) <small><small>(2016-04-22)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.2.0/tqdm-4.2.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.2.0/tqdm-4.2.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.2.0/tqdm-4.2.0.zip)


- MPL licence!
- slightly updated logo
- update examples
- `update(0)` allowed
- better VTE support
  - ascii fallback when unicode not available

## [v4.0.0](https://github.com/tqdm/tqdm/releases/tag/v4.0.0) <small><small>(2016-02-04)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.0.0/tqdm-4.0.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v4.0.0/tqdm-4.0.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v4.0.0/tqdm-4.0.0.zip)


- automate `nested`
  - deprecate `nested`
  - add manual override control with `position`
- documentation and example updates, coverage and tests
- make `leave==True` by default (was `False`)

## [v3.8.0](https://github.com/tqdm/tqdm/releases/tag/v3.8.0) <small><small>(2016-01-31)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v3.8.0/tqdm-3.8.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v3.8.0/tqdm-3.8.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v3.8.0/tqdm-3.8.0.zip)


- update(n<1) raises error
- sanitise and update examples and README
- fix setup.py encoding error
- remove py32 from Travis
- changelog more accessible from README

## [v3.7.1](https://github.com/tqdm/tqdm/releases/tag/v3.7.1) <small><small>(2016-01-13)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v3.7.1/tqdm-3.7.1-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v3.7.1/tqdm-3.7.1.tar.gz)|[exe](https://github.com/tqdm/tqdm/releases/download/v3.7.1/tqdm-3.7.1.win32.exe)|[zip](https://github.com/tqdm/tqdm/releases/download/v3.7.1/tqdm-3.7.1.zip)


- Added more OS support (FreeBSD, Solaris/SunOS)
- Added Python3.5 support and tests
- Added IronPython2.7 support
- Fix Makefile management for Python3
- Added relative timing for tests
- More stable smoothed ETA
- Refactoring _everything_ into one big `tqdm` class for even more subclassing fun

## [v3.6.0](https://github.com/tqdm/tqdm/releases/tag/v3.6.0) <small><small>(2015-12-31)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v3.6.0/tqdm-3.6.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v3.6.0/tqdm-3.6.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v3.6.0/tqdm-3.6.0.zip)


Added support for "restarting" a progressbar after a long pause without making the iteration rate go haywire. Simply call the `unpause()` method on the `tqdm` instance that is about to be restarted. Can also start `tqdm` skipping a number of steps specified by `initial` (without bias-ing ETA).

## [v3.5.0](https://github.com/tqdm/tqdm/releases/tag/v3.5.0) <small><small>(2015-12-31)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v3.5.0/tqdm-3.5.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v3.5.0/tqdm-3.5.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v3.5.0/tqdm-3.5.0.zip)


- Fully customisable output format using the `bar_format` keyword argument.
  - Valid strings: bar, n, n_fmt, total, total_fmt, percentage, rate, rate_fmt, elapsed, remaining, l_bar, r_bar, desc
  - Example: `bar_format='{desc}{bar}{rate:03.3d}'`
  - Default: '{l_bar}{bar}{r_bar}', where l_bar is '{desc}{percentage:3.0f}%|' and r_bar is '| {n_fmt}/{total_fmt} [{elapsed_str}<{remaining_str}, {rate_fmt}]'.
- Solaris, FreeBSD support mentioned
- Link redirects circumvented

## [v3.3.0](https://github.com/tqdm/tqdm/releases/tag/v3.3.0) <small><small>(2015-12-31)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v3.3.0/tqdm-3.3.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v3.3.0/tqdm-3.3.0.tar.gz)|[zip](https://github.com/tqdm/tqdm/releases/download/v3.3.0/tqdm-3.3.0.zip)


- Support added for pandas `apply` => `progress_apply`
- 80-char width when running interactive `help()`
- update examples using `with` syntax

## [v3.1.4](https://github.com/tqdm/tqdm/releases/tag/v3.1.4) <small><small>(2015-11-28)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v3.1.4/tqdm-3.1.4-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v3.1.4/tqdm-3.1.4.tar.gz)|[exe](https://github.com/tqdm/tqdm/releases/download/v3.1.4/tqdm-3.1.4.win32.exe)|[zip](https://github.com/tqdm/tqdm/releases/download/v3.1.4/tqdm-3.1.4.zip)


Added `smoothing` and `maxinterval` features for smooth progress bar and rate for unconstant, variable changes in update times, and abstracted gui to its own class and file.

Also added a performance test to prevent performance regressions.

## [v2.2.4](https://github.com/tqdm/tqdm/releases/tag/v2.2.4) <small><small>(2015-11-08)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v2.2.4/tqdm-2.2.4-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v2.2.4/tqdm-2.2.4.tar.gz)|[exe](https://github.com/tqdm/tqdm/releases/download/v2.2.4/tqdm-2.2.4.win32.exe)|[zip](https://github.com/tqdm/tqdm/releases/download/v2.2.4/tqdm-2.2.4.zip)


Added the dynamic management of the bar on window resize, plus a better internal testing/build workflow using `python setup.py make [alias]`.

## [v2.0.0](https://github.com/tqdm/tqdm/releases/tag/v2.0.0) <small><small>(2015-10-11)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v2.0.0/tqdm-2.0.0-py2.py3-none-any.whl)|[gz](https://github.com/tqdm/tqdm/releases/download/v2.0.0/tqdm-2.0.0.tar.gz)|[exe](https://github.com/tqdm/tqdm/releases/download/v2.0.0/tqdm-2.0.0.win32.exe)|[zip](https://github.com/tqdm/tqdm/releases/download/v2.0.0/tqdm-2.0.0.zip)


First public release of the next generation of tqdm, with lots of new features, more speed, more unit testing, more coverage (100% yeah!), more beer and coffee.

This release can also be downloaded on [PyPi here](https://pypi.python.org/pypi/tqdm/2.0.0).
