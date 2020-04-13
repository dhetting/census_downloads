import os
import sys

from src.cdown import Cdown

if __name__ == '__main__':
    year = sys.argv[1]
    var = sys.argv[2]

    try:
        ws = sys.argv[3]
    except:
        ws = os.path.join(os.curdir, year)

    cd = Cdown(year=year, ws=ws)

    cd.get(var)
