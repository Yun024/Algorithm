import sys,re
from collections import Counter

data = sys.stdin.read()
sentence = re.split(r'(?m)^\s*EndOfText\s*$', data)
outs = []

for idx, strings in enumerate(sentence):
    strings = strings.strip()
    if not strings:
        continue

    lines = strings.splitlines()
    n = int(lines[0])

    body = " ".join(lines[1:]).lower()
    words = re.findall("[a-z]+",body)
    cnt = Counter(words)
    res = sorted([k for k,v in cnt.items() if len(k) > 1 and v == n])

    outs.append('\n'.join(res) if res else "There is no such word.")

print("\n\n".join(outs))