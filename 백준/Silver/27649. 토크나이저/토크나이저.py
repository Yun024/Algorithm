import sys,re

strings = sys.stdin.readline().strip()
patterns = r"([<>()]|&&|\|\|)|\s"
s = re.split(patterns,strings)
print(' '.join(filter(None,s)))