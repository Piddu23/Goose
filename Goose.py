#program setup
import tkinter

root = tkinter.Tk()
root.title("Goose")
root.geometry("500x250")

#configuring columns and rows so windows can be dynamically resized by user
tkinter.Grid.columnconfigure(root, index=0, weight=1)
tkinter.Grid.rowconfigure(root, index=0, weight=1)

#functions
def add_task():
    task = enter_task_bar.get()
    listed_tasks.insert(tkinter.END, task)
    enter_task_bar.delete(0, tkinter.END)

def delete_task():
    task_index = listed_tasks.curselection()[0]
    listed_tasks.delete(task_index)

#main section of app
listed_tasks = tkinter.Listbox(root, bg="#c2d0ff")
listed_tasks.grid(row=0, sticky="nsew")

enter_task_bar = tkinter.Entry(root)
enter_task_bar.grid(sticky="nsew")

#buttons
button_add_task = tkinter.Button(root, text="Add", command=add_task)
button_add_task.grid(sticky="nsew")

button_delete_task = tkinter.Button(root, text="Delete", command=delete_task)
button_delete_task.grid(sticky="nsew")

#program loop
root.mainloop()