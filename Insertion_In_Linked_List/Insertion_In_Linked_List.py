#Here will use the data from Ch 5 Chapter WS
n=["Ben","Ava","Mia","Pam","Max","Sam","Ian","Sue"] #here stored the actual data
next=[3,0,6,5,2,7,-1,4] #here store the pointer for each data (-1 is null pointer)
head=5 #here means the start of this link is is from n[5] which is "Sam" (python list index start with 0)
#We are talking about insertion in linked list,to help understanding,we need map out everything
'''
	linked list after refactor into a standard list:['Sam', 'Sue', 'Max', 'Mia', 'Ian']
	which the pointer be like(the index):5->7->4->2->6-> -1(Null pointer)
	By performing Insertion,what actually happen is(here used Q1(iii)):
	n=["Ben","Ava","Mia","Pam","Max","Sam","Ian","Sue","Fan"] #Added "Fan" which is on index 8
	# The question said to insert "Fan" after "Mia" which suppose the result be like:5->7->4->2->8->6-> -1(Null pointer)
	So what we need to do is to change the pointer of "Fan" so it will point to "Ian"(index 6) which will look like: 8->6
	and because we also need chain up "Mia" to "Fan",so we also need change pointer of "Mia":2->6(Originally),2->8->6(Now)
	Below is the program of how to do it
'''
#in simple words what we need to do for insertion is copy the pointer to the new item and the original pointer point to the new item
n.append("Fan")
next.append(-1) #here i use -1 as the preset pointer of "Fan"
def ap(st,new):#st as the item which we will insert data after it,and new is the index to the new item
	ptr=head
	while ptr!=-1:
		if n[ptr]==st:
			next[new]=next[ptr] #copy the pointer of "Mia" to "Fan"
			next[ptr]=new #change the pointer of "Mia" so it point to "Fan"
			break
		ptr=next[ptr] #Update current pointer
print(f"Original:\nn:{n}\nnext:{next}\n")
ap("Mia",8)
print(f"Now:\nn:{n}\nnext:{next}")
