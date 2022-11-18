from tkinter import *



class TaskWindow:
    def __init__(self, update):
        global top
        top = Toplevel()
        self.frame = Frame(top)
        self.frame.pack(padx=10, pady=10)
        self.update = update

        # allow the user to input a task name
        self.taskNameInput = StringVar()
        taskNameEntry = Entry(top, textvariable=self.taskNameInput)
        taskNameEntry.pack(padx=60, pady=30)

        # allow the user to input a task description
        self.taskDescriptionInput = StringVar()
        taskDescritpionEntry = Entry(top, textvariable=self.taskDescriptionInput)
        taskDescritpionEntry.pack(padx=50, pady=20)

        # allow the user to set a reminder date
        self.reminderDateOption = IntVar()
        reminderDate = Radiobutton(top, value=1, text="Reminder Date", variable=self.reminderDateOption)
        reminderDate.pack(padx=10, pady=10)

        # confirm the new task
        createTaskButton = Button(top, text="Submit", command=self.submit)
        createTaskButton.pack(padx=5, pady=5)

        # close out of the new task window
        closeTaskWindow = Button(top, text="Back", command=self.destroyTaskWindow)
        closeTaskWindow.pack(padx=4, pady=4)

        self.frame.pack(padx=10, pady=10)

        # function to complete the creation of the task
    def submit(self):
        self.update(self.taskNameInput.get(), self.taskDescriptionInput.get(), self.reminderDateOption.get())
        self.destroyTaskWindow()

        # destroy the window after the user submits the new task
    def destroyTaskWindow(self):
        top.destroy()


