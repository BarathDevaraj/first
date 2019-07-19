n,k=input().split()
n=int(n)
k=int(k)
b=list(map(int,input().split()))[:n]
if k in b:
	print('yes')
else:
	print('no')
