arr = list(map(int,input("Enter: ").split()))
s = len(arr)
if s<2:
    print(-1)
else:
    s1 = sorted(arr)
    j = s1[-2]
    print(j)
    