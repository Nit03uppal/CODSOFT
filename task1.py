from tkinter import *
import tkinter.messagebox

def add():
    txt = enter.get(1.0, "end-1c").strip()
    if not txt:
        tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
    else:
        task.insert(END, txt)
        #after adding task it clears the text window
        enter.delete(1.0, END)
        
        # Add a checkbox in front of the task
        checkbox_states.append(BooleanVar())
        checkbox = Checkbutton(frame_task, variable=checkbox_states[-1], command=lambda index=len(checkbox_states)-1: done(index))
        checkbox.pack(anchor=W)

#function to facilitate the delete task from the Listbox
def delete():
    #selects the selected item and then deletes it 
    selected = task.curselection()
    if not selected:
        tkinter.messagebox.showinfo(title="Information", message="Select The task for deletion !!")
    else:
        index = selected[0]
        task.delete(index)
        # Delete the corresponding checkbox state
        del checkbox_states[index]
        # Update remaining checkbox states index
        for i in range(index, len(checkbox_states)):
            checkbox_states[i].set(False)

def done(index):
    if checkbox_states[index].get():
        task_text = task.get(index)
        task.delete(index)
        task.insert(index, task_text + " ✔")
    else:
        task_text = task.get(index)
        if task_text.endswith(" ✔"):
            task_text = task_text[:-2]
            task.delete(index)
            task.insert(index, task_text)

t1 = Tk()
#giving appropriate title
t1.title("TO DO LIST - TASK 1")
t1.geometry('500x500')

t1.config(bg='PaleVioletRed')
#Frame widget to organize different widgets
frame_task = Frame(t1)
#organizes widgets in a proper format
frame_task.pack(pady=10, padx=10, fill=BOTH, expand=True)

#listbox used to store tasks entered
task = Listbox(frame_task, bg="grey", fg="blue", height=8, width=30, font="Arial")
task.pack(side=LEFT, fill=BOTH, expand=True)

#Scrolldown to scroll across many tasks
scrollbar_task = Scrollbar(frame_task, command=task.yview)
scrollbar_task.pack(side=RIGHT, fill=Y)
task.config(yscrollcommand=scrollbar_task.set)
 
label_task = Label(t1, text="Please Enter the Task Below:")
label_task.pack(pady=3)

#text entry widget
enter = Text(t1, width=40, height=3)
enter.pack()

#provides a button widget
entry_button = Button(t1, text="Add task", width=20, command=add)
entry_button.pack(pady=3)

delete_button = Button(t1, text="Delete selected task", width=20, command=delete)
delete_button.pack(pady=3)

checkbox_states = []

#loops until events like mouse movement,buttonclick,etc occur
#repeats until user closes the window
t1.mainloop()
