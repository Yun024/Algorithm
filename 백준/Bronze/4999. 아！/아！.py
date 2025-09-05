import sys

jaehwan = sys.stdin.readline().strip()
doctor = sys.stdin.readline().strip()

print('go' if doctor in jaehwan else 'no')