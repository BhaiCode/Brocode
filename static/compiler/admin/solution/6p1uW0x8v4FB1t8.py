def check(r, b, d):
    # pnii("jknlns")
    if d==0:
        return "Yes" if r==b else "No"
    else:
        minI = min(r,b)
        maxI = max(r,b)
        diff = maxI - minI
        return "Yes" if (diff / minI) <= d else "No"
 
t = int(input())
for i in range(t):
    r, b, d = list(map(int, input().split()))
    print(check(r, b, d))

