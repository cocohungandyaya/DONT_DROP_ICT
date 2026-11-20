#Nested loop example here

#here will use the example provided in Chapter 4 Quiz CQ 1 but in python

#make it with better vision(python index start with 0,pseudocode start with 1 (usually))
M=[
	[6,5,7,3,2,1,4,8,9],#Index(column):0,1,2,3,4,5,6,7,8 respectively
	[2,3,1,1,2,1,6,5,6],
	[3,2,8,3,3,2,4,8,3],
	[5,4,6,6,1,5,4,5,4],
	[4,6,7,5,8,3,2,3,1],
	[8,4,8,1,7,5,5,6,5],
	[6,8,3,4,9,4,6,4,7],
	[2,1,6,5,3,1,4,8,1]
	#Index(row):0,1,2,3,4,5,6,7 respectively
	#Here Index of rows meaning each 1D array inside M(the 2D array)
]
#here i will follow the WS to use sub-program
#Dont remember this if it feel confusion but you can call the list defined ouside and before def
def sumPopulation(Q,n):
	for i in range(0,8-n+1):#original code dont have +1 but because python will skip last loop but Pseudocode wont
		Q.append([])#the use here is to initialize a space for later edition
		for j in range(0,9-n+1):
			Q[i].append(0) #here initialize the initial value
			for p in range(i,n+i):#same as  above,python skip last loop so no need -1 in python
				for q in range(j,n+j):
					Q[i][j]=Q[i][j]+M[p][q]
final_array=[] #here initialize a array for use in the subprogram
sumPopulation(final_array,7)
print(final_array)
