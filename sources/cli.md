`tqdm`'s command line interface (CLI) can be used in a script or on the terminal/console. Simply inserting `tqdm` (or `python -m tqdm`) between pipes will pass through all `stdin` to `stdout` while printing progress to `stderr`.

Run `tqdm --help` for a full list of options.

The example below demonstrate counting the number of lines in all Python files in the current directory, with timing information included.

```sh
$ time find . -name '*.py' -type f -exec cat \{} \; | wc -l
857365

real    0m3.458s
user    0m0.274s
sys     0m3.325s

$ time find . -name '*.py' -type f -exec cat \{} \; | tqdm | wc -l
857366it [00:03, 246471.31it/s]
857365

real    0m3.585s
user    0m0.862s
sys     0m3.358s
```

Note that the usual arguments for [`tqdm`](..) can also be specified.

```sh
$ find . -name '*.py' -type f -exec cat \{} \; \
  | tqdm --unit loc --unit_scale --total 857366 >> /dev/null
100%|█████████████████████████████████| 857K/857K [00:04<00:00, 246Kloc/s]
```

Backing up a large directory?

```sh
$ tar -zcf - docs/ | tqdm --bytes --total `du -sb docs/ | cut -f1` \
  > backup.tgz
44%|██████████████▊                   | 153M/352M [00:14<00:18, 11.0MB/s]
```

This can be beautified further:

```sh
$ BYTES="$(du -sb docs/ | cut -f1)"
$ tar -cf - docs/ \
  | tqdm --bytes --total "$BYTES" --desc Processing | gzip \
  | tqdm --bytes --total "$BYTES" --desc Compressed --position 1 \
  > ~/backup.tgz
Processing: 100%|██████████████████████| 352M/352M [00:14<00:00, 30.2MB/s]
Compressed:  42%|█████████▎            | 148M/352M [00:14<00:19, 10.9MB/s]
```

Or done on a file level using 7-zip:

```sh
$ 7z a -bd -r backup.7z docs/ | grep Compressing \
  | tqdm --total $(find docs/ -type f | wc -l) --unit files \
  | grep -v Compressing
100%|██████████████████████████▉| 15327/15327 [01:00<00:00, 712.96files/s]
```

Pre-existing CLI programs already outputting basic progress information will benefit from `tqdm`'s `--update` and `--update_to` flags:

```sh
$ seq 3 0.1 5 | tqdm --total 5 --update_to --null
100%|████████████████████████████████████| 5.0/5 [00:00<00:00, 9673.21it/s]
$ seq 10 | tqdm --update --null  # 1 + 2 + ... + 10 = 55 iterations
55it [00:00, 90006.52it/s]
```
