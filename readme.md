[![Build Status](https://travis-ci.org/tylermzeller/cubey.svg?branch=master)](https://travis-ci.org/tylermzeller/cubey)

Author: Tyler Zeller

A fully functional puzzle cube written in Python 2.7.10.

# Download

Download with:

```
pip install cubey
```

# Usage

Within a python interpreter type the following:

```Python
import cubey
c = cubey.Cube()
print c
print "Is solved?", c.is_solved()
```

which should print:

```Bash
 F   B   L   R   U   D
RRR PPP GGG BBB WWW YYY 
RRR PPP GGG BBB WWW YYY 
RRR PPP GGG BBB WWW YYY 
```
