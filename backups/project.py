import sys

with open("notredame.txt") as textFile:
    lines = [line.split() for line in textFile]

    print lines
