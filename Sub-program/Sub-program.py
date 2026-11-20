#Here will give some examples about Sub-program,you also can try edit the code to see if match your imagination

#in python we use def to define a function(Sub-program)

def swap(list_here,a,b):	#a and b is the index of items in list
	''' 
	Rememeber this if you cant remember significants of sub-program:
	1.list can still be edit globally even you pass it to the function(sub-program)
	2.variable got pass to a sub-program will only pass the value,so you need call that value by the temporary name
		(here the original list is called list_here instead of example_list)
	3.if item isnt a list then it will only make a copy of the value inside the item and use locally(inside the sub-program) with the temporary name
	'''
	temp=list_here[a] #create a temporary storage for item at index a inside list_here
	list_here[a]=list_here[b] #here replace the item at index a inside list_here
	list_here[b]=temp #here then put the original item at index a inside list_here to index b of list_here to complete the swap
example_list=[0,1] #we will then call the swap function to swap them so the result will be:[1,0]
swap(example_list,0,1)
print(example_list)
#try edit above code if you want
