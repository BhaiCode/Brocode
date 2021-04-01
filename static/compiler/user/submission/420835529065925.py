for i in range(int(input())):
    bool=True
    k=int(input())
    list1=list(map(int, input().split()))
    for j in range(k-1):
        
        list1[j+1]+=list1[j]-j
        list1[j]=j
 
        if not list1[j+1]>list1[j]:
            bool=False
            break
    
    if bool : print("YES2")
    else: print("No")

