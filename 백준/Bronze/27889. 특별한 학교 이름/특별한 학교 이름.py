import sys

strings = sys.stdin.readline().strip()
if strings == "NLCS":
    print("North London Collegiate School")
elif strings == "BHA":
    print("Branksome Hall Asia")
elif strings == "KIS":
    print("Korea International School")
else:
    print("St. Johnsbury Academy")