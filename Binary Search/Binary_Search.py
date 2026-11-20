#Binary Search example refer to VisualizeICT Video OR Binary Search WS
#I will try add some print to show the process for better understanding
mark=[50,50,64,65,75,79,80,85,88,97]
def binary_search(mark,target): #mark define here means it is a temporary name,not directly calling the mark array above this line
	start=0
	end=len(mark)-1 # here need -1 because len(mark) give the counts like len([0,1]) is 2 but because the index start with 0 so need -1 to avoid index out of range
	found=False
	i=1 #added this for showing the loop number
	while start<=end and not found:#exit when start>end in case not found
		mid=int((start+end)/2) #also can write: mid=(start+end)//2
		print(f"loop {i}(before comparison): mid={mid} , mark[mid]={mark[mid]} , start={start} , end={end}")
		if mark[mid]==target:
			found=True
		elif target <mark[mid]:
			end=mid-1
		else:
			start=mid+1
		print(f"loop {i}(after comparison): mid={mid} , mark[mid]={mark[mid]} , start={start} , end={end}")
		i+=1
	if found:
		print("Found at index",mid)
	else:
		print("Not found")
binary_search(mark,80)
#if you not sure why your answer not work just try edit the code to see why
