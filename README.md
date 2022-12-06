advent of code 2022
===================

https://adventofcode.com/2022

This repository was a template by anthonywritescode. You can check him out here:
- [Streamed daily on twitch](https://twitch.tv/anthonywritescode)
- [Streams uploaded to youtube afterwards](https://www.youtube.com/@anthonywritescode-vods)

### timing

- comparing to these numbers isn't necessarily useful
- normalize your timing to day 1 part 1 and compare
- alternate implementations are listed in parens
- these timings are very non-scientific (sample size 1)

```console
$ find -maxdepth 1 -type d -name 'day*' -not -name day00 | sort | xargs --replace bash -xc 'python {}/part1.py {}/input.txt; python {}/part2.py {}/input.txt'
+ python day01/part1.py day01/input.txt
71300
> 431 μs
```


### usage

pulling inputs for a problem
```
$ cd day01
$ aoc-download-input
```

testing and submitting problem

```
# inside a day directory
$ pytest part1.py
$ python3 part1.py| aoc-submit --part 1
$ python3 part2.py| aoc-submit --part 2
```
