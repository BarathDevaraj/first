n=int(input())
ab=list(map(int,input().split()))[:n]
print(sum(ab)//len(ab))
