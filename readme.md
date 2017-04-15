[![Build Status](https://travis-ci.org/tylermzeller/cubey.svg?branch=master)](https://travis-ci.org/tylermzeller/cubey)

Author: Tyler Zeller

A fully functional puzzle cube written in Python 2.7.10.

# Download

Download with:

```
pip install cubey
```

# Quick Start
```Python
import cubey as qb
c = qb.Cube()
print c
print c.is_solved()
c.to_checker()
print c
print c.is_solved()
```

which should print:

```Bash
 F   B   L   R   U   D
RRR PPP GGG BBB WWW YYY
RRR PPP GGG BBB WWW YYY
RRR PPP GGG BBB WWW YYY
True

F   B   L   R   U   D
RPR PRP GBG BGB WYW YWY
PRP RPR BGB GBG YWY WYW
RPR PRP GBG BGB WYW YWY
False
```

# API

With the cubey package, you can perform all external face twists like a real
puzzle cube.

## Example 1
```Python
import cubey as qb
c = qb.Cube()
# R U R' U'
c.r()
c.u()
c.r_prime()
c.u_prime()
print c
```
Ouput:
```Bash
F   B   L   R   U   D
RRY PBB PGG BBW WWG YYB
RRW PPP GGG PBB WWR YYY
RRR PPP GGG WBB WWR YYY
```
## Example 2
```Python
import cubey as qb
c = qb.Cube()
# U' D' F2 L B2
c.u_prime()
c.d_prime()
c.f2()
c.l()
c.b2()
print c
```
Ouput:
```Bash
F   B   L   R   U   D
WBB WGG PGP RRR YYG BWW
WRR YPP BGP GBR PWW RYY
YGG YBB RBP PPR BYY WWG
```

For longer formulae, you can use the `do()` method which takes in a formula as
as (well-formed) string:

## Example 1
```Python
import cubey as qb
c = qb.Cube()
# R U R' U'
c.do("R U R' U'")
print c
```
Ouput:
```Bash
F   B   L   R   U   D
RRY PBB PGG BBW WWG YYB
RRW PPP GGG PBB WWR YYY
RRR PPP GGG WBB WWR YYY
```

## Example 2
```Python
import cubey as qb
c = qb.Cube()
# U' D' F2 L B2
c.do("U' D' F2 L B2")
print c
```
Ouput:
```Bash
F   B   L   R   U   D
WBB WGG PGP RRR YYG BWW
WRR YPP BGP GBR PWW RYY
YGG YBB RBP PPR BYY WWG
```
The Cubey API also provides wrapper methods for commonly used algorithms:
## Example 1: [Sune](https://www.speedsolving.com/wiki/index.php/Sune)
```Python
import cubey as qb
c = qb.Cube()
c.sune()
print c
```
Ouput:
```Bash
F   B   L   R   U   D
WRG RBB WPP WGG RWW YYY
RRR PPP GGG BBB WWW YYY
RRR PPP GGG BBB BWP YYY
```
