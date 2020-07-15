# [tqdm/tqdm](https://github.com/tqdm/tqdm) Releases

## [v4.47.0](https://github.com/tqdm/tqdm/releases/tag/v4.47.0) <small><small>(2020-06-28)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.47.0/tqdm-4.47.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.47.0/tqdm-4.47.0-py2.py3-none-any.whl.asc)


- add `contrib.discord` (similar to `contrib.telegram`) ([#976])
- add `contrib.bells` to auto-enable all extras
- add `contrib.utils_worker` for common slow tasks (e.g. web I/O)
  + fix lazy large memory usage & discard unsent messages (unprocessed tasks)
- fix slow notebook imports ([#955] <- [#709])
- fix `gui` `TypeError` on unknown `len()` ([#971])
- misc documentation/error message updates
  + more succinct ImportError on missing `ipywidgets` ([#872])
  + fix broken/deprecated link ([#981])
  + add inline usage for `contrib.discord` and `contrib.telegram`
- misc framework updates
  + add official `py3.8` support ([#986])
  + fix `snap` builds

![contrib.discord](https://user-images.githubusercontent.com/10780059/82755091-62374c80-9dc9-11ea-88bb-fd8cafe854ff.png)

![contrib.telegram](https://github.com/ermakovpetr/tg_tqdm/blob/master/tg_tqdm_how_it_work.gif?raw=true)

[#976]: https://github.com/tqdm/tqdm/issues/976
[#955]: https://github.com/tqdm/tqdm/issues/955
[#709]: https://github.com/tqdm/tqdm/issues/709
[#971]: https://github.com/tqdm/tqdm/issues/971
[#872]: https://github.com/tqdm/tqdm/issues/872
[#981]: https://github.com/tqdm/tqdm/issues/981
[#986]: https://github.com/tqdm/tqdm/issues/986

## [v4.46.1](https://github.com/tqdm/tqdm/releases/tag/v4.46.1) <small><small>(2020-06-03)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.46.1/tqdm-4.46.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.46.1/tqdm-4.46.1-py2.py3-none-any.whl.asc)


- fix missing `sys.setcheckinterval` in py3.9 ([#978])
- fix `keras.TqdmCallback` compatibility with `tensorflow==2.2.0` ([#979])
- update documentation
  + correct `contrib.concurrent` correct `max_workers` ([#977])
  + drop prominent mention of `xrange` ([#965])
- minor linting

[#978]: https://github.com/tqdm/tqdm/issues/978
[#979]: https://github.com/tqdm/tqdm/issues/979
[#977]: https://github.com/tqdm/tqdm/issues/977
[#965]: https://github.com/tqdm/tqdm/issues/965

## [v4.46.0](https://github.com/tqdm/tqdm/releases/tag/v4.46.0) <small><small>(2020-05-03)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.46.0/tqdm-4.46.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.46.0/tqdm-4.46.0-py2.py3-none-any.whl.asc)


- add `contrib.telegram` [#949] <- [#948]
- add `bash` tab completion and `--comppath` [#946], [#947] <- [#858]
- fix exception safety in `external_write_mode` [#940]
- add `requests` examples ([#242])
- update documentation

[#949]: https://github.com/tqdm/tqdm/issues/949
[#948]: https://github.com/tqdm/tqdm/issues/948
[#946]: https://github.com/tqdm/tqdm/issues/946
[#947]: https://github.com/tqdm/tqdm/issues/947
[#858]: https://github.com/tqdm/tqdm/issues/858
[#940]: https://github.com/tqdm/tqdm/issues/940
[#242]: https://github.com/tqdm/tqdm/issues/242

## [v4.45.0](https://github.com/tqdm/tqdm/releases/tag/v4.45.0) <small><small>(2020-04-02)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.45.0/tqdm-4.45.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.45.0/tqdm-4.45.0-py2.py3-none-any.whl.asc)


- propagate and `close()` on exceptions ([#926] <- [#548])
- fix nested `clear()`
- rework nested `close()` ([#930] <- [#924] <- [#918], [#677])
  + reduces screen flicker/blank space at the cost of ordering
- update all documentation & demos
- add and update tests
- dev framework: add pre-commit helper

[#926]: https://github.com/tqdm/tqdm/issues/926
[#548]: https://github.com/tqdm/tqdm/issues/548
[#930]: https://github.com/tqdm/tqdm/issues/930
[#924]: https://github.com/tqdm/tqdm/issues/924
[#918]: https://github.com/tqdm/tqdm/issues/918
[#677]: https://github.com/tqdm/tqdm/issues/677

## [v4.44.1](https://github.com/tqdm/tqdm/releases/tag/v4.44.1) <small><small>(2020-03-29)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.44.1/tqdm-4.44.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.44.1/tqdm-4.44.1-py2.py3-none-any.whl.asc)


- fix `_utils` `ImportError` => `DeprecationWarning` ([#928] <- [#927])

[#928]: https://github.com/tqdm/tqdm/issues/928
[#927]: https://github.com/tqdm/tqdm/issues/927

## [v4.44.0](https://github.com/tqdm/tqdm/releases/tag/v4.44.0) <small><small>(2020-03-28)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.44.0/tqdm-4.44.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.44.0/tqdm-4.44.0-py2.py3-none-any.whl.asc)


- add automatic `nrows` and expose for manual override ([#918] -> [#924])
- expose and warn about small `chunksize` in `tqdm.contrib.concurrent.process_map` ([#912])
- fix py2 file stream comparison ([#727] -> [#730])
- deprecate `utils._environ_cols_wrapper`
- add and update tests
- add documentation

[#918]: https://github.com/tqdm/tqdm/issues/918
[#924]: https://github.com/tqdm/tqdm/issues/924
[#912]: https://github.com/tqdm/tqdm/issues/912
[#727]: https://github.com/tqdm/tqdm/issues/727
[#730]: https://github.com/tqdm/tqdm/issues/730

## [v4.43.0](https://github.com/tqdm/tqdm/releases/tag/v4.43.0) <small><small>(2020-02-19)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.43.0/tqdm-4.43.0-py2.py3-none-any.whl)


- fix `notebook` exceptions ([#669] <- [#650])
  + `set_description()` when `disable=True`
- `contrib.concurrent`: avoid unnecessary `len(iterable)` ([#893])
- update documentation
  + clarify etymology ([#895])
  + fix minor typo ([#890])
  + update contributors and years
- update tests
- fix CI tests for PRs

[#669]: https://github.com/tqdm/tqdm/issues/669
[#650]: https://github.com/tqdm/tqdm/issues/650
[#893]: https://github.com/tqdm/tqdm/issues/893
[#895]: https://github.com/tqdm/tqdm/issues/895
[#890]: https://github.com/tqdm/tqdm/issues/890

## [v4.42.1](https://github.com/tqdm/tqdm/releases/tag/v4.42.1) <small><small>(2020-02-03)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.42.1/tqdm-4.42.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.42.1/tqdm-4.42.1-py2.py3-none-any.whl.asc)


- support `pandas==1.0.0` ([#780], [#555])
- minor metadata updates
- minor CI test update

[#780]: https://github.com/tqdm/tqdm/issues/780
[#555]: https://github.com/tqdm/tqdm/issues/555

## [v4.42.0](https://github.com/tqdm/tqdm/releases/tag/v4.42.0) <small><small>(2020-01-25)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.42.0/tqdm-4.42.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.42.0/tqdm-4.42.0-py2.py3-none-any.whl.asc)


- `notebook`: update `disable=None` behaviour ([#880])
- `tqdm.keras`: support `tensorflow.keras` as well as `keras` ([#885])
- add `contrib` ([#882])
  + `tenumerate` ([#840] <- [#480], [#402])
  + `tzip` <= `zip`
  + `tmap` <= `map`
  + add `concurrent` module
    * `thread_map` <= `concurrent.futures.ThreadPoolExecutor.map`
    * `process_map` <= `concurrent.futures.ProcessPoolExecutor.map`
  + add `itertools` module ([#225]) stub
    * `product`
- add & update tests
- add & update documentation
  + [README](https://github.com/tqdm/tqdm#tqdm)
  + [examples/](https://github.com/tqdm/tqdm/tree/master/examples)
- update CI framework

[#880]: https://github.com/tqdm/tqdm/issues/880
[#885]: https://github.com/tqdm/tqdm/issues/885
[#882]: https://github.com/tqdm/tqdm/issues/882
[#840]: https://github.com/tqdm/tqdm/issues/840
[#480]: https://github.com/tqdm/tqdm/issues/480
[#402]: https://github.com/tqdm/tqdm/issues/402
[#225]: https://github.com/tqdm/tqdm/issues/225

## [v4.41.1](https://github.com/tqdm/tqdm/releases/tag/v4.41.1) <small><small>(2020-01-05)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.41.1/tqdm-4.41.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.41.1/tqdm-4.41.1-py2.py3-none-any.whl.asc)


- `keras` module tidy and fixes
  + fix `batch_size=None` ([#869])
  + add missing `pop('size')`

[#869]: https://github.com/tqdm/tqdm/issues/869

## [v4.41.0](https://github.com/tqdm/tqdm/releases/tag/v4.41.0) <small><small>(2019-12-20)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.41.0/tqdm-4.41.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.41.0/tqdm-4.41.0-py2.py3-none-any.whl.asc)


- trim on `ncols` overflow with ANSI handling ([#850], [#716] <- [#690])
- add `notebook.reset()` ([#864])
- add `keras.TqdmCallback` ([#867] <- [#835])
- documentation updates
  + document newly added features (above)
  + notebook `ncols` percentage/pixels ([#276])
- test updates
  + test newly added features (above)
  + add CI for `win` and `osx` ([#841])
  + `py2` threading

[#850]: https://github.com/tqdm/tqdm/issues/850
[#716]: https://github.com/tqdm/tqdm/issues/716
[#690]: https://github.com/tqdm/tqdm/issues/690
[#864]: https://github.com/tqdm/tqdm/issues/864
[#867]: https://github.com/tqdm/tqdm/issues/867
[#835]: https://github.com/tqdm/tqdm/issues/835
[#276]: https://github.com/tqdm/tqdm/issues/276
[#841]: https://github.com/tqdm/tqdm/issues/841

## [v4.40.2](https://github.com/tqdm/tqdm/releases/tag/v4.40.2) <small><small>(2019-12-11)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.40.2/tqdm-4.40.2-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.40.2/tqdm-4.40.2-py2.py3-none-any.whl.asc)


- fix `pandas` unhashable func ([#862] -> [#863])
  + add tests

[#862]: https://github.com/tqdm/tqdm/issues/862
[#863]: https://github.com/tqdm/tqdm/issues/863

## [v4.40.1](https://github.com/tqdm/tqdm/releases/tag/v4.40.1) <small><small>(2019-12-11)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.40.1/tqdm-4.40.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.40.1/tqdm-4.40.1-py2.py3-none-any.whl.asc)


- fix floating point imprecision raising errors ([#859])
- fix auto gh releases ([travis-ci/dpl#914](https://github.com/travis-ci/dpl/issues/914))
- update CONTRIBUTING ([#84 (comment)](https://github.com/tqdm/tqdm/issues/84#issuecomment-167516992))

[#859]: https://github.com/tqdm/tqdm/issues/859

## [v4.40.0](https://github.com/tqdm/tqdm/releases/tag/v4.40.0) <small><small>(2019-12-01)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.40.0/tqdm-4.40.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.40.0/tqdm-4.40.0-py2.py3-none-any.whl.asc)


- officially support `float` for `n` and `total` ([#802])
  + `notebook`: use `FloatProgress` <= `IntProgress` ([#471], [#456])
  + allow imprecision (`n <= total + epsilon`) ([#849])
- fix unicode bar format arguments ([#803] -> [#851])
- add `contrib` submodule ([#815])
- add `wrapattr`, `utils.CallbackIOWrapper`, `contrib.DummyTqdmFile` ([#84] -> [#844])
- update tests
- update documentation
- tidy automatic `snap` deployments
- minor doc update ([#854])

[#802]: https://github.com/tqdm/tqdm/issues/802
[#471]: https://github.com/tqdm/tqdm/issues/471
[#456]: https://github.com/tqdm/tqdm/issues/456
[#849]: https://github.com/tqdm/tqdm/issues/849
[#803]: https://github.com/tqdm/tqdm/issues/803
[#851]: https://github.com/tqdm/tqdm/issues/851
[#815]: https://github.com/tqdm/tqdm/issues/815
[#84]: https://github.com/tqdm/tqdm/issues/84
[#844]: https://github.com/tqdm/tqdm/issues/844
[#854]: https://github.com/tqdm/tqdm/issues/854

## [v4.39.0](https://github.com/tqdm/tqdm/releases/tag/v4.39.0) <small><small>(2019-11-22)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.39.0/tqdm-4.39.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.39.0/tqdm-4.39.0-py2.py3-none-any.whl.asc)


- add `pandas` builtin operations check ([#843] <- [#697])
- avoid unnecessary `dedent` ([#837])
- remove unneeded bar logic
- misc code tidy
- update documentation
  + document default argument overriding ([#370])
  + add missing `isatty()` ([#713])
  + update badges
  + add code of conduct
- update framework
  + clean CI stages
  + update CI default `py3.6` => `py3.7`
  + automate snap releases ([#686] <- [#685])

[#843]: https://github.com/tqdm/tqdm/issues/843
[#697]: https://github.com/tqdm/tqdm/issues/697
[#837]: https://github.com/tqdm/tqdm/issues/837
[#370]: https://github.com/tqdm/tqdm/issues/370
[#713]: https://github.com/tqdm/tqdm/issues/713
[#686]: https://github.com/tqdm/tqdm/issues/686
[#685]: https://github.com/tqdm/tqdm/issues/685

## [v4.38.0](https://github.com/tqdm/tqdm/releases/tag/v4.38.0) <small><small>(2019-11-09)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.38.0/tqdm-4.38.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.38.0/tqdm-4.38.0-py2.py3-none-any.whl.asc)


- support `lock_args` for e.g. non-blocking intermediate writes ([#838] -> [#839])
  + use `self.refresh()` in more places
  + add and update performance tests
  + support args for `TqdmDefaultWriteLock.acquire()`
- fix colorama on win ([#678], [#764])
- framework updates
  + CI cleanup
    * move to stages (check/test/deploy)
    * auto deploy notes
    * deploy only on parent repo
    * separate docker deploy
  + update documentation sync/generation
- update examples
- update documentation
- add and update tests
- misc tidy and linting

[#838]: https://github.com/tqdm/tqdm/issues/838
[#839]: https://github.com/tqdm/tqdm/issues/839
[#678]: https://github.com/tqdm/tqdm/issues/678
[#764]: https://github.com/tqdm/tqdm/issues/764

## [v4.37.0](https://github.com/tqdm/tqdm/releases/tag/v4.37.0) <small><small>(2019-10-31)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.37.0/tqdm-4.37.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.37.0/tqdm-4.37.0-py2.py3-none-any.whl.asc)


- potential future pandas fix ([#824])
- better unicode widechar support ([#803] -> [#410], [#805])
- fix example/tqdm_wget unknown total ([#826])
- add `stacklevel=2` to warnings ([#821])
- misc framework updates
  + snapcraft version fix
  + update issue/pr templates ([#830])
  + update unit tests
- misc documentation updates
  + update parallel (multiprocessing, ThreadPoolExecutor) example ([#407])
  + add slides, video images
  + add CII Best Practices badge
  + add repology badge
  + update badge icons

[#824]: https://github.com/tqdm/tqdm/issues/824
[#803]: https://github.com/tqdm/tqdm/issues/803
[#410]: https://github.com/tqdm/tqdm/issues/410
[#805]: https://github.com/tqdm/tqdm/issues/805
[#826]: https://github.com/tqdm/tqdm/issues/826
[#821]: https://github.com/tqdm/tqdm/issues/821
[#830]: https://github.com/tqdm/tqdm/issues/830
[#407]: https://github.com/tqdm/tqdm/issues/407

## [v4.36.1](https://github.com/tqdm/tqdm/releases/tag/v4.36.1) <small><small>(2019-09-20)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.36.1/tqdm-4.36.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.36.1/tqdm-4.36.1-py2.py3-none-any.whl.asc)


- fix CLI entrypoint

## [v4.36.0](https://github.com/tqdm/tqdm/releases/tag/v4.36.0) <small><small>(2019-09-17)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.36.0/tqdm-4.36.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.36.0/tqdm-4.36.0-py2.py3-none-any.whl.asc)


- expose more custom format params
- potential thread safety fix ([#548])
- update submodule architecture ([#198] -> [#800])
  + backward-compatibility
  + expose `utils`
  + rename `main` -> `cli`
  + add/fix tests
  + fix minor cached var optimisation
  + `gui` partial upgrade ([#790])
  + `notebook` upgrade ([#790])
    * support `{bar}` in `bar_format` ([#594])
    * inherit methods including `set_*(refresh)` ([#740] -> [#741])
  + ready for `contrib` releases ([#252])
- support custom `bar_format` with unknown `total`
- fix `tqdm_notebook` red block on explicit `file=None` ([#791])
- update notebook to fully support custom `bar_format` ([#594], [#649])
- misc tidy
  + warnings
  + linting
  + update submodule contribution guide ([#252])
  + parallel `(py)make test`
  + fix Zenodo metadata
- update documentation
  + `pandas`, `notebook`, `gui` ([#245])
  + indentation
  + update multiprocessing and multithreading examples ([#796])

[#548]: https://github.com/tqdm/tqdm/issues/548
[#198]: https://github.com/tqdm/tqdm/issues/198
[#800]: https://github.com/tqdm/tqdm/issues/800
[#790]: https://github.com/tqdm/tqdm/issues/790
[#790]: https://github.com/tqdm/tqdm/issues/790
[#594]: https://github.com/tqdm/tqdm/issues/594
[#740]: https://github.com/tqdm/tqdm/issues/740
[#741]: https://github.com/tqdm/tqdm/issues/741
[#252]: https://github.com/tqdm/tqdm/issues/252
[#791]: https://github.com/tqdm/tqdm/issues/791
[#594]: https://github.com/tqdm/tqdm/issues/594
[#649]: https://github.com/tqdm/tqdm/issues/649
[#252]: https://github.com/tqdm/tqdm/issues/252
[#245]: https://github.com/tqdm/tqdm/issues/245
[#796]: https://github.com/tqdm/tqdm/issues/796

## [v4.35.0](https://github.com/tqdm/tqdm/releases/tag/v4.35.0) <small><small>(2019-08-24)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.35.0/tqdm-4.35.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.35.0/tqdm-4.35.0-py2.py3-none-any.whl.asc)


- add `{bar}` format specifier ([#623] -> [#799])
  + `[width][type]`
- add tests and documentation
- update performance tests

[#623]: https://github.com/tqdm/tqdm/issues/623
[#799]: https://github.com/tqdm/tqdm/issues/799

## [v4.34.0](https://github.com/tqdm/tqdm/releases/tag/v4.34.0) <small><small>(2019-08-18)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.34.0/tqdm-4.34.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.34.0/tqdm-4.34.0-py2.py3-none-any.whl.asc)


- add `leave=None` convenience option for `leave = position == 0`
- ensure nested completed bars respect `leave=True` ([#230])
- ensure nested bars are cleared before being moved up ([#795])
- support both ` ` and `=` syntax for CLI options ([#761] -> [#774])
- misc documentation updates ([#778], [#782])
- fix/update tests
- update GitHub docker package deployment

[#230]: https://github.com/tqdm/tqdm/issues/230
[#795]: https://github.com/tqdm/tqdm/issues/795
[#761]: https://github.com/tqdm/tqdm/issues/761
[#774]: https://github.com/tqdm/tqdm/issues/774
[#778]: https://github.com/tqdm/tqdm/issues/778
[#782]: https://github.com/tqdm/tqdm/issues/782

## [v4.33.0](https://github.com/tqdm/tqdm/releases/tag/v4.33.0) <small><small>(2019-08-08)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.33.0/tqdm-4.33.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.33.0/tqdm-4.33.0-py2.py3-none-any.whl.asc)


- fix `pandas==0.25` API change ([#780])
- add contributor badges (`sourcerer`)
- fix py26 travis CI
- metadata fixes
  + `.zenodo.json`
  + `CODEOWNERS`
- GitHub package registry docker deployment
- minor linting
- documentation updates ([#773])

[#780]: https://github.com/tqdm/tqdm/issues/780
[#773]: https://github.com/tqdm/tqdm/issues/773

## [v4.32.2](https://github.com/tqdm/tqdm/releases/tag/v4.32.2) <small><small>(2019-06-18)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.32.2/tqdm-4.32.2-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.32.2/tqdm-4.32.2-py2.py3-none-any.whl.asc)


- fix 'Set changed size during iteration' ([#481] -> [#700], [#754])
- add `tqdm.autonotebook` check for `$VSCODE_PID` ([#747] -> [#751])
- fix missing `multiprocessing` in Jython ([#698])
- make `bool(tqdm(iter))` consistent with `bool(iter)` ([#353] -> [#694])
- add and update unit tests
- add and update documentation & framework
  + update notable contributors list
  + update usage docstrings ([#714], [#715])
  + add funding
  + add `awesome-python` badge
  + trove classifier update
  + update demo notebook badges
  + add JOSS DOI
  + add Zenodo metadata
  + move unnecessary root clutter

[#481]: https://github.com/tqdm/tqdm/issues/481
[#700]: https://github.com/tqdm/tqdm/issues/700
[#754]: https://github.com/tqdm/tqdm/issues/754
[#747]: https://github.com/tqdm/tqdm/issues/747
[#751]: https://github.com/tqdm/tqdm/issues/751
[#698]: https://github.com/tqdm/tqdm/issues/698
[#353]: https://github.com/tqdm/tqdm/issues/353
[#694]: https://github.com/tqdm/tqdm/issues/694
[#714]: https://github.com/tqdm/tqdm/issues/714
[#715]: https://github.com/tqdm/tqdm/issues/715

## [v4.32.1](https://github.com/tqdm/tqdm/releases/tag/v4.32.1) <small><small>(2019-05-13)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.32.1/tqdm-4.32.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.32.1/tqdm-4.32.1-py2.py3-none-any.whl.asc)


- fix `notebook` with unknown `total` ([#743])

[#743]: https://github.com/tqdm/tqdm/issues/743

## [v4.32.0](https://github.com/tqdm/tqdm/releases/tag/v4.32.0) <small><small>(2019-05-13)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.32.0/tqdm-4.32.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.32.0/tqdm-4.32.0-py2.py3-none-any.whl.asc)


- support `unit_scale` in `notebook`
- support negative update ([#432], [#545])
- add `reset()` function ([#547], [#545])
- add `[python setup.py] make run`
- add and update documentation
  - example of dynamic usage ([#735], [#545], [#547], [#432], [#374])
  - note writing issues ([#737])
  - update badges
  - add [PyData2019 slides link](https://tqdm.github.io/PyData2019/slides.html)
  - add [JOSS paper](https://github.com/openjournals/joss-papers/blob/joss.01277/joss.01277/10.21105.joss.01277.pdf)
  - update manpages
  - add docker install
  - add snapcraft install
  - notebooks: add binder, rename RMOTR => notebooks.ai ([#679])
  - prettify and unify contributors/maintainers/authors
- CI and release framework updates
  - add snapcraft snaps ([#647])
  - add travis auto-deployment ([#685])
    + PyPI releases
    + docker devel/releases
  - update deployment dev docs
  - fix travis deploy pymake
  - update .gitinore
  - add & update unit tests
  - automate more documentation

[#432]: https://github.com/tqdm/tqdm/issues/432
[#545]: https://github.com/tqdm/tqdm/issues/545
[#547]: https://github.com/tqdm/tqdm/issues/547
[#545]: https://github.com/tqdm/tqdm/issues/545
[#735]: https://github.com/tqdm/tqdm/issues/735
[#545]: https://github.com/tqdm/tqdm/issues/545
[#547]: https://github.com/tqdm/tqdm/issues/547
[#432]: https://github.com/tqdm/tqdm/issues/432
[#374]: https://github.com/tqdm/tqdm/issues/374
[#737]: https://github.com/tqdm/tqdm/issues/737
[#679]: https://github.com/tqdm/tqdm/issues/679
[#647]: https://github.com/tqdm/tqdm/issues/647
[#685]: https://github.com/tqdm/tqdm/issues/685

## [v4.31.1](https://github.com/tqdm/tqdm/releases/tag/v4.31.1) <small><small>(2019-02-10)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.31.1/tqdm-4.31.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.31.1/tqdm-4.31.1-py2.py3-none-any.whl.asc)


- fix `file.encoding==None` caused by [#598] ([#673] -> [#676])
  + add tests
- tidy code, update authors and tests
  + add `setup.py` test to CI

[#598]: https://github.com/tqdm/tqdm/issues/598
[#673]: https://github.com/tqdm/tqdm/issues/673
[#676]: https://github.com/tqdm/tqdm/issues/676

## [v4.31.0](https://github.com/tqdm/tqdm/releases/tag/v4.31.0) <small><small>(2019-02-09)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.31.0/tqdm-4.31.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.31.0/tqdm-4.31.0-py2.py3-none-any.whl.asc)


- Write bytes to `stdout`/`stderr` in py2 (https://bugs.python.org/issue21363, [#589] -> [#598])
  - Add `write_bytes` parameter for py2/3 default override
- support custom bar characters vias `ascii` parameter ([#223] -> [#227])
  - implement, document and test custom bar spinners
- support custom `bar_format` with unknown `total` ([#282] -> [#284])
- fix `TypeError` when `unit_scale` and unknown `total`
- document `format_dict`
- expose `elapsed_s`, `remaining_s` to `bar_format`
- add `unit` option to `bar_format` ([#368])
- auto `README.rst` generation framework
  - add notes in `CONTRIBUTING.md`
- update tests
- update documentation
- misc code tidy

[#589]: https://github.com/tqdm/tqdm/issues/589
[#598]: https://github.com/tqdm/tqdm/issues/598
[#223]: https://github.com/tqdm/tqdm/issues/223
[#227]: https://github.com/tqdm/tqdm/issues/227
[#282]: https://github.com/tqdm/tqdm/issues/282
[#284]: https://github.com/tqdm/tqdm/issues/284
[#368]: https://github.com/tqdm/tqdm/issues/368

## [v4.30.0](https://github.com/tqdm/tqdm/releases/tag/v4.30.0) <small><small>(2019-01-26)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.30.0/tqdm-4.30.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.30.0/tqdm-4.30.0-py2.py3-none-any.whl.asc)


- avoid moving when `leave=False`
- generalise nested bar tests
- add `display()` helper function
- add and expose `format_dict` ([#562], [#482], [#494], [#656])
     + allow arbitrary keyword arguments for `format_meter`
     + document `format_dict` overriding
     + add tests for overriding
     + related: [#660] [#172] [#587]
- add and tidy developer documentation
- fix py3 CLI pipe decoding error ([#663])
- framework overhaul (developing, testing, Travis CI updates)
- tidy code and style (flake8)
- `setup.py` refactor
    + `setup.py make`
        * add support for multi-line commands
        * tidy and efficiency
    + replace `setup.py`'s built-in `make` -> `py-make>=0.1.9` ([#290])
    + add `requirements-dev.txt` and `extras_require[dev]`
- add, update and tidy tests
- include interactive Jupyter demonstration ([#652] -> [#659])
- update documentation
    + add FAQ about py2 pipes ([#359])
    + add badges
    + update examples
    + update authors

[#562]: https://github.com/tqdm/tqdm/issues/562
[#482]: https://github.com/tqdm/tqdm/issues/482
[#494]: https://github.com/tqdm/tqdm/issues/494
[#656]: https://github.com/tqdm/tqdm/issues/656
[#660]: https://github.com/tqdm/tqdm/issues/660
[#172]: https://github.com/tqdm/tqdm/issues/172
[#587]: https://github.com/tqdm/tqdm/issues/587
[#663]: https://github.com/tqdm/tqdm/issues/663
[#290]: https://github.com/tqdm/tqdm/issues/290
[#652]: https://github.com/tqdm/tqdm/issues/652
[#659]: https://github.com/tqdm/tqdm/issues/659
[#359]: https://github.com/tqdm/tqdm/issues/359

## [v4.29.1](https://github.com/tqdm/tqdm/releases/tag/v4.29.1) <small><small>(2019-01-11)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.29.1/tqdm-4.29.1-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.29.1/tqdm-4.29.1-py2.py3-none-any.whl.asc)


- fix `classmethod` lock bug ([#617]: [#457] -> [#658])
- add unit test to prevent regression

[#617]: https://github.com/tqdm/tqdm/issues/617
[#457]: https://github.com/tqdm/tqdm/issues/457
[#658]: https://github.com/tqdm/tqdm/issues/658

## [v4.29.0](https://github.com/tqdm/tqdm/releases/tag/v4.29.0) <small><small>(2019-01-06)</small></small>
[whl](https://github.com/tqdm/tqdm/releases/download/v4.29.0/tqdm-4.29.0-py2.py3-none-any.whl)|[asc](https://github.com/tqdm/tqdm/releases/download/v4.29.0/tqdm-4.29.0-py2.py3-none-any.whl.asc)


- Avoid global multiprocessing locks ([#611] -> [#617])
- Add support for infinite iterables ([#651])
- Fix missing attr pos when used in multi-threaded environment ([#573])
- Do not join `TMonitor` if it is the current thread ([#613] -> [#641])
- Add OpenBSD NIX support ([#638])
- Unit tests, general documentation fixes and tidying (e.g. [#642])
- CI travis improvements
  + `py37-dev` -> `py37` ([#622])
  + fix `py26`

[#611]: https://github.com/tqdm/tqdm/issues/611
[#617]: https://github.com/tqdm/tqdm/issues/617
[#651]: https://github.com/tqdm/tqdm/issues/651
[#573]: https://github.com/tqdm/tqdm/issues/573
[#613]: https://github.com/tqdm/tqdm/issues/613
[#641]: https://github.com/tqdm/tqdm/issues/641
[#638]: https://github.com/tqdm/tqdm/issues/638
[#642]: https://github.com/tqdm/tqdm/issues/642
[#622]: https://github.com/tqdm/tqdm/issues/622

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
  - security fix ([CVE-2016-10075](https://nvd.nist.gov/vuln/detail/CVE-2016-10075))
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
