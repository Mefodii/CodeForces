#  http://codeforces.com/contest/598/problem/A

def smartSum(n):
    s = n*(n+1) // 2
    power = 0
    current = 1
    while current <= n:
        power += 1
        current *= 2
    diff = (current - 1) * 2
    return int(s - diff)

t = input()
for i in range(int(t)):
    n = input()
    print(smartSum(int(n)))
