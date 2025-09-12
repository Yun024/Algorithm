import sys

sentence = sys.stdin.readline().strip()
strings = sentence.split("What is")
for string in strings:
    string = string.split("?")[0]
    if "." not in string:
        print("Forty-two is" + string + ".")