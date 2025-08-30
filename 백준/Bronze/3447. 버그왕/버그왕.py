import sys

code = sys.stdin.read().strip()
while 'BUG' in code:
    code = code.replace("BUG","")
print(code)