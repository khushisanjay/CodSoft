#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importing libraries
import tkinter
import tkinter.messagebox
import pickle

#giving the title
window = tkinter.Tk()
window.title("TO-DO LIST")


#adding tasks

def task_adding():
  todo = task_add.get()
  if todo != "":
    todo_box.insert(tkinter.END, todo)
    task_add.delete(0, tkinter.END)
  else:
    tkinter.messagebox.showerror("Error", "Please enter a task") #displays error if no task is added
    

#deleting tasks

def task_deleting():
  try:
    index_todo = todo_box.curselection()[0]
    todo_box.delete(index_todo)

  except:
    tkinter.messagebox.showerror("Error", "Please select a task")  #displays error if no task is added
    

#deleting all the entered tasks

def task_clearall():
  try:
    todo_list = pickle.load(open("tasks.dat", "rb"))
    todo_box.delete(0, tkinter.END)

    for todo in todo_list:
      todo_box.insert(tkinter.END)
  except:
    tkinter.messagebox.showerror("Error", "No tasks to delete")  #displays error if no task is added
    

#saving tasks

def task_save():
  todo_list = todo_box.get(0, tkinter.END)
  pickle.dump(todo_list, open("tasks.dat", "wb"))
    

#creating the frame and window

list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=20, width=50)
todo_box.pack(side=tkinter.LEFT)


#adding a scroller

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)


#configuring the window

task_add = tkinter.Entry(window, width=70)
task_add.pack()


#adding buttons/keys for accessing the commands

add_task_button = tkinter.Button(window,
                                 text="ADD TASK",
                                 font=("century", 15, "bold"),
                                 background="white",
                                 width=30,
                                 command=task_adding)

add_task_button.pack()           #key for adding the tasks

remove_task_button = tkinter.Button(window,
                                    text="DELETE TASK",
                                    font=("century", 15, "bold"),
                                    background="light grey",
                                    width=30,
                                    command=task_deleting)

remove_task_button.pack()       #key for deleting the tasks

clearall_task_button = tkinter.Button(window,
                                  text="CLEAR ALL TASKS",
                                  font=("century", 15, "bold"),
                                  background="white",
                                  width=30,
                                  command=task_clearall)

clearall_task_button.pack()     #key for clearing all the entered tasks


# Function to exit the program
def exit_program():
    window.destroy()  # Closes the tkinter window

# Create an exit button
exit_button = tkinter.Button(window,
                             text="EXIT",
                             font=("century", 15, "bold"),
                             background="light grey",
                             width=30,
                             command=exit_program)

exit_button.pack()  # Key for exiting the program

window.mainloop()


# In[ ]:




