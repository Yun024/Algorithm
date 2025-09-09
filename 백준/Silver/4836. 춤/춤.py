import sys

dance_lists = sys.stdin.read().strip().split("\n")
for dance_list in dance_lists:
    
    temp = []
    dance_list = dance_list.split()
    length = len(dance_list)

    if dance_list[-3:] != ['clap','stomp','clap']:
        temp.append(2)
    if dance_list[0] == 'jiggle':
        temp.append(4)

    for idx,dance in enumerate(dance_list):
        if dance == "dip":
            temp.append(5)         
            if not(dance_list[max(0,idx-1)] == 'jiggle' or dance_list[max(0,idx-2)] == 'jiggle' or\
            dance_list[min(length-1,idx+1)] == 'twirl'):
                dance_list[idx] = "DIP"
                temp.append(1)
        elif dance =='twirl':
            temp.append(6)
        elif dance =='hop':
            temp.append(7)
    temp = set(temp)
    ans = []
    
    if 6 in temp and 7 not in temp:
        ans.append(3)
    if 5 not in temp:
        ans.append(5)
    if 2 in temp:
        ans.append(2)
    if 4 in temp:
        ans.append(4)
    if 1 in temp:
        ans.append(1)

    ans.sort()
    
    if not ans:
        print(f"form ok: {' '.join(dance_list)}")
    elif len(ans) == 1:
        print(f"form error {ans[0]}: {' '.join(dance_list)}")
    else:
        print(f"form errors {', '.join(map(str,ans[:-1]))} and {ans[-1]}: {' '.join(dance_list)}")

