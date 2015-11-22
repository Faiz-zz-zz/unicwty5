from collections import deque
import copy
numbers=[[16, 15, 14, 13],[12, 11, 10, 9],[8, 7, 6, 5],[4, 3, 2, 1]]
def check(a):
	if summation(a)!=0:
			for i in range(4):
				for j in range(4):
					if a[i][j]==1:
						b=copy.deepcopy(a)
						core.append(wacknode(b, i, j))
						b.append(numbers[i][j])
						if summation(b)==0:
							print "success"
							print b
							core.clear()
							return False
						print b,
						print summation(b)
			core.popleft()				
						
							

def call_function():
	while len(core)!=0:
		check(core[0])



def summation(a):
	sum=0
	for i in range(4):
		for j in range(4):
			sum=sum+a[i][j]
	return sum		
def wacknode(a,i, j):
	a[i][j]=0
	if i>=1 and i<=2 and j<=2 and j>=1:
		if a[i-1][j]==0:
			a[i-1][j]=1
		else:
			a[i-1][j]=0
		
		if a[i][j+1]==0:
			a[i][j+1]=1
		else:
			a[i][j+1]=0

		if a[i+1][j]==0:
			a[i+1][j]=1
		else:
			a[i+1][j]=0

		if a[i][j-1]==0:
			a[i][j-1]=1
		else:
			a[i][j-1]=0

	elif i==0 and j>=1 and j<=2:
		if a[i][j+1]==0:
			a[i][j+1]=1
		else:
			a[i][j+1]=0

		if a[i+1][j]==0:
			a[i+1][j]=1
		else:
			a[i+1][j]=0

		if a[i][j-1]==0:
			a[i][j-1]=1
		else:
			a[i][j-1]=0

	elif 	i==3 and j>=1 and j<=2:
		if a[i-1][j]==0:
			a[i-1][j]=1
		else:
			a[i-1][j]=0
		
		if a[i][j+1]==0:
			a[i][j+1]=1
		else:
			a[i][j+1]=0

		if a[i][j-1]==0:
			a[i][j-1]=1
		else:
			a[i][j-1]=0	

	elif j==0 and i>=1 and i<=2:
		if a[i-1][j]==0:
			a[i-1][j]=1
		else:
			a[i-1][j]=0
		
		if a[i][j+1]==0:
			a[i][j+1]=1
		else:
			a[i][j+1]=0

		if a[i+1][j]==0:
			a[i+1][j]=1
		else:
			a[i+1][j]=0

	elif j==3 and i>=1 and i<=2:
		if a[i-1][j]==0:
			a[i-1][j]=1
		else:
			a[i-1][j]=0
		
		if a[i+1][j]==0:
			a[i+1][j]=1
		else:
			a[i+1][j]=0

		if a[i][j-1]==0:
			a[i][j-1]=1
		else:
			a[i][j-1]=0	

	elif i==0 and j==0:
		if a[i][j+1]==0:
			a[i][j+1]=1
		else:
			a[i][j+1]=0

		if a[i+1][j]==0:
			a[i+1][j]=1
		else:
			a[i+1][j]=0

	elif i==0 and j==3:
		if a[0][2]==0:
			a[0][2]=1
		else:
			a[0][2]=0

		if a[1][3]==0:
			a[1][3]=1
		else:
			a[1][3]=0

	elif i==3 and j==3:
		if a[3][2]==0:
			a[3][2]=1
		else:
			a[3][2]=0

		if a[2][3]==0:
			a[2][3]=1
		else:
			a[2][3]=0

	elif i==3 and j== 0:
		if a[3][1]==0:
			a[3][1]=1
		else:
			a[3][1]=0

		if a[2][0]==0:
			a[2][0]=1
		else:
			a[2][0]=0
	return a										

a1=[[1, 1,1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
core=deque([a1])
#check(a1)
call_function()
for x in range(len(core)): 
	print core[x]
	print "\n"
