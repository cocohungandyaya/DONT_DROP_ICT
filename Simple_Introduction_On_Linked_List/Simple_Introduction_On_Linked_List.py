#Here i will use data from Ch 5 Chapter WS
#In this practice i wont introduce any function stuff related to linked list,just purely explaining about linked list
n=["Ben","Ava","Mia","Pam","Max","Sam","Ian","Sue"] #here stored the actual data
next=[3,0,6,5,2,7,-1,4] #here store the pointer for each data (-1 is null pointer)
head=5 #here means the start of this link is is from n[5] which is "Sam" (python list index start with 0)
#I will write some code to print out how the linked list looks like(just run the code or adjust above data to see what is a linked list)
linked_list_be_like=[];linked_list_be_like.append(n[5]);
c_p=next[5];
while c_p>0:linked_list_be_like.append(n[c_p]);c_p=next[c_p];
print(f"This is how linked list looked like if we refactor it into a standard list:{linked_list_be_like}");
