import sys

input = sys.stdin.readline 
while 1:
    page = int(input().strip())
    if not page:
        break
    print_page = input().split(",")
    temp = []
    for pp in print_page:
        if "-" in pp:
            low,high = map(int,pp.split("-"))
        else:
            if page >= int(pp):
                temp.append(int(pp))
            continue
        if low > high or page < low:
            continue
        else:
            temp += list(range(low,min(page+1,high+1)))
    print(len(set(temp)))