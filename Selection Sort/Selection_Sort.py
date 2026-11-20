#Selection Sort example refer to VisualizeICT Video OR Selection Sort WS
mark=[45,70,66,82,55,95,60]#Index:0,1,2,3,4,5,6 respectively
def selection_sort(mark): #mark define here means it is a temporary name,not directly calling the mark array above this line
	n=len(mark)
	for i in range(0,n-1): #n need -1 because below have i+1,if n didnt -1 then will cause index out of range
		max_index=i #here cant be 0 because if you use 0 then the program will basically paralysis,you can try change it to see why
		lpcount=1 #for later printing loop number
		for j in range(i+1,n):
			print(f"(before comparison)Loopcount:Outer={i+1},Inner={lpcount} -> i={i},j={j},mark[j]={mark[j]},max_index={max_index},mark[max_index]={mark[max_index]}\n")
			if mark[j]>mark[max_index]:
				max_index=j
			print(f"(after comparison)Loopcount:Outer={i+1},Inner={lpcount} -> i={i},j={j},mark[j]={mark[j]},max_index={max_index},mark[max_index]={mark[max_index]}\n")
			lpcount+=1
		#below is swapping,if you cant understand just remember the structure then
		temp=mark[i] #Create a temporary storage for storing mark[i]
		mark[i]=mark[max_index]
		mark[max_index]=temp
		print(f"mark array after swap:{mark}\n")
selection_sort(mark)
