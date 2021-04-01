for _ in range(int(input())):
    n=int(input())
    s=input()
    ans='1'
    for i in range(n-1):
        k=int(ans[i])+int(s[i])
        if k==2:
            if s[i+1]=='1':
                ans+='0'
            else:
                ans+='1'
        elif k==1:
            if s[i+1]=='0':
                ans+='0'
            else:
                ans+='1'
        else:
            ans+='1'
    print(ans)

