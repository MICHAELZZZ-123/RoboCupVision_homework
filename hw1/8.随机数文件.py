from pathlib import Path
from random import randint

path=Path(__file__).resolve().parent/"data.txt"
with open(path,"w") as p:
    for i in range(100000):
        a=randint(1,100)
        p.write(str(a))
        if i!=99999:
            p.write("\n")