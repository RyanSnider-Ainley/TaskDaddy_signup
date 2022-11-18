from taskButton import TaskWindow
from tkinter import *


class TaskListWindow:
    def __init__(self, master):
        self.frame = Frame(master)

        # change the title of the window

        # create a list box to hold the tasks
        self.listbox = Listbox(self.frame,
                               bg="azure",            #color of the listbox
                               font=("Constantia",18),  #font of the tasks
                               width=18,
                               height=18)                #width of the listbox
        self.listbox.pack()

        # create a button to add a new task
        createTaskButton = Button(self.frame, text="Create New Task", command=self.createNewTask)
        createTaskButton.pack(padx=50, pady=5)

        # create a button to edit a task
        editTaskbutton = Button(self.frame, text="Edit", command=self.editTask)
        editTaskbutton.pack(padx=50, pady=5)

        # create a button to delete a task
        deleteTaskbutton = Button(self.frame, text="Delete", command=self.deleteTask)
        deleteTaskbutton.pack(padx=50, pady=5)

        self.frame.pack(padx=10, pady=5)


    # create a new task, allows the user to input information
    def createNewTask(self):
        taskWindow = TaskWindow(self.update)

    # update the listbox to include the newly created task
    def update(self, taskNameInput, taskDescriptionInput, reminderDateOption):

        # print out the values to double-check the inputs
        print("Updated function belonging to the Task List Window was called")
        print("Task Name: ", taskNameInput)
        print("Task Description: ", taskDescriptionInput)
        print("Reminder date choice: ", reminderDateOption)

        #add the new task to the list box
        self.listbox.insert(self.listbox.size(), taskNameInput)

        # adjust the size of the list box
        #self.listbox.config(height=self.listbox.size())

    #edit a task in the listbox
    def editTask(self):
        for item in self.listbox.curselection():
            self.listbox.delete(item)
            self.createNewTask()

    def deleteTask(self):
        for item in self.listbox.curselection():
            self.listbox.delete(item)







