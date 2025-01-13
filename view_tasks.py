# git ryhmä harjoitus Jani (lead), b Jarmo, Jussi, Maiju
# f = open("todo.py", "r")
# f.write("testing part add")
# f.close()
# tasks = open("todo.py", "r") # reading string list
 

def view_tasks(tasks):
	print("This is the list of existing tasks")
	index = 0
	while index < len(tasks):  # while items in list
		print(f'{index+1}. {tasks[index]}')    # print item