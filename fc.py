d=int(input())
sum=0
while d>0:
	sum+=d%10
	d//=10
print(sum)
