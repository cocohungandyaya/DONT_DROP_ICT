#here will give a simple example of Linear Search
#this time i wont use sub-program
mark=[0,43,63,92,6,87,19,87]
found=False
target=87 #you can adjust to see different result
for i in range(0,len(mark)):
	print(f"loop {i+1}: i={i},mark[i]={mark[i]},target={target}")
	if mark[i]==target:
		found=True
		index=i
		break #if not add break it will still work but just loop a little bit more plus the index it give out will be the last matched item in the array,you an try delete it to see any different
if found:
	print("target index:",index)
else:
	print("target not found in mark")
