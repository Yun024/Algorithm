import sys
block = sys.stdin.read().strip()

res = block.replace("\n",".")[::2]
print(res.count("F"))