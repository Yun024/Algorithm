import sys

def isprime(num):

    for n in range(2,int(num**0.5)+1):
        if not num%n:
            print("It is not a prime word.")
            break
    else:
        print("It is a prime word.")

word = sys.stdin.readline().strip()
num = sum([ord(w)-38 if w.isupper() else ord(w)-96 for w in word])
isprime(num)