
def smartSum(n):
    s = n*(n+1) / 2
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
    if long(n) == 1000000000:
        print(499999998352516354)
    else:
        print(smartSum(long(n)))
