"""\
Tools for adding basis sets to atom lists.

"""

from pyquante2.basis import data

sym2pow = {
    'S' : [(0,0,0)],
    'P' : [(1,0,0),(0,1,0),(0,0,1)],
    'D' : [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)],
    'F' : [(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),(1,0,2),
           (0,3,0),(0,2,1),(0,1,2), (0,0,3)]
    }

pow2sym = {}
for sym in sym2pow:
    for p in sym2pow[sym]:
        pow2sym[p] = sym
