import sys

def bomb_check(ans):

    bomb_dic = {
    "*** * * * * * * *** ":"0",
    "  *   *   *   *   * ":"1",
    "***   * *** *   *** ":"2",
    "***   * ***   * *** ":"3",
    "* * * * ***   *   * ":"4",
    "*** *   ***   * *** ":"5",
    "*** *   *** * * *** ":"6",
    "***   *   *   *   * ":"7",
    "*** * * *** * * *** ":"8",
    "*** * * ***   * *** ":"9"
}
    res = ""
    for i in ans:
        if i in bomb_dic.keys():
            res += bomb_dic[i]
        else:
            return "BOOM!!"

    return "BEER!!" if not int(res)%6 else "BOOM!!"


bomb_codes = sys.stdin.read().split("\n")
for row in range(5):
    bomb_codes[row] += " "

length = len(bomb_codes[0])//4
ans = [""] * length

for row in range(5):
    for idx in range(0,4*length,4):
        ans[idx//4] += bomb_codes[row][idx:idx+4]

print(bomb_check(ans))