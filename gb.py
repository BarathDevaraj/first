st=input()
count=0
for i in st:
	if (i!='0' and i!='1'):
		count=1
if(count==0):
	print('yes')
else:
	print('no')
