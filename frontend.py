from tkinter import *

master = Tk()

master.title("Smoking Status Tracker")
header = Label(master, text = "Please enter the following information:")

first_name = StringVar()
firstName_label = Label(master, text = "First name:")
firstName_entry = Entry(master, width = 15, textvariable = first_name)

last_name = StringVar()
lastName_label = Label(master, text = "Last name:")
lastName_entry = Entry(master, width = 15, textvariable = last_name)

birth_date = StringVar()
birthDate_label = Label(master, text = "Birth Date \n (DD/MM/YYYY):")
birthDate_entry = Entry(master, width = 15, textvariable = birth_date)

smoking_status = IntVar()
smokingStatus_label = Label(master, text = "Smoking Status:")
smokingStatus_Option1 = Radiobutton(master, text = "Smoker", variable = smoking_status, value = 1)
smokingStatus_Option2 = Radiobutton(master, text = "Non-smoker", variable = smoking_status, value = 0)
smokingStatus_Option1.deselect()
smokingStatus_Option2.deselect()

updateDatabase_button = Button(master, text = "Update!")
viewStatistics_button = Button(master, text = "View Statistics")

header.grid(row = 0, column = 0)
firstName_label.grid(row = 1, column = 0)
firstName_entry.grid(row = 1, column = 1)
lastName_label.grid(row = 2, column = 0)
lastName_entry.grid(row = 2, column = 1)
birthDate_label.grid(row = 3, column = 0)
birthDate_entry.grid(row = 3, column = 1)
smokingStatus_label.grid(row = 4, column = 0)
smokingStatus_Option1.grid(row = 4, column = 1)
smokingStatus_Option2.grid(row = 4, column = 2)
updateDatabase_button.grid(row = 5, column = 1)
viewStatistics_button.grid(row = 6, column = 1)

master.grid_columnconfigure((0,2), weight = 1) # keeps columns centered in full screen

master.mainloop()