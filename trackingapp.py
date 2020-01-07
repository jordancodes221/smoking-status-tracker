from tkinter import *

master = Tk()

patients = []

def popup(message, title = "!"):
    popup = Toplevel(master, height = 20, width = 20)
    popup.title(title)

    error_message = Message(popup, text = message, 
                                justify = CENTER, padx = 10, pady = 10)
    error_message.pack()

    exit_button = Button(popup, text = "Got it!", command = popup.destroy)
    exit_button.pack()

def inputOK(first_name, last_name, birth_year):
    inputOK = False
    if first_name.isalpha() and last_name.isalpha() and len(birth_year) == 4 and str(birth_year).isnumeric():
        inputOK = True
    return inputOK

def create_patient(first_name, last_name, birth_year, smoking_status):
    global patients
    if not inputOK(first_name, last_name, birth_year):
        popup("One of your inputs is invalid!")
        return None
    new_patient = {
                    "name": first_name.lower() + " " + last_name.lower(),
                    "birth year": birth_year,
                    "smoking status": smoking_status
                    }
    patientFound = False
    if patients != []:
        for temp_entry in patients:
            # Identify them by their names and birth year, due to many cases of parents-children with same name
            if temp_entry["name"] == new_patient["name"] and temp_entry["birth year"] == new_patient["birth year"]:
                patientFound = True
                break
    if not patientFound:
        patients.append(new_patient)
        popup("New patient created!")
    else:
        popup("ERROR!\n\nPatient already exists!\n\nConsider updating instead.") 

def update_patient(first_name, last_name, birth_year, smoking_status):
    global patients
    updated_patient = {
                    "name": first_name.lower() + " " + last_name.lower(),
                    "birth year": birth_year,
                    "smoking status": smoking_status
                    }
    patientFound = False
    if patients != []:
        for k in range(0, len(patients)):
            # Identify them by their names and birth year, due to many cases of parents-children with same name
            if patients[k]["name"] == updated_patient["name"] and patients[k]["birth year"] == updated_patient["birth year"]:
                patientFound = True
                index_found = k
                break
    if patientFound:
        patients[index_found] = updated_patient
        popup("Your update was successful!")
    else:
        popup("ERROR!\n\nPatient not found!\n\n No update could be made!")

def viewStats():
    smokers = 0
    nonsmokers = 0
    for entry in patients:
        if entry["smoking status"] == 1:
            smokers += 1
        if entry["smoking status"] == 0:
            nonsmokers += 1
    total_patients = len(patients)
    smokers_message = "{} of your {} patients are smokers, which is {}%".format(smokers, total_patients, round(smokers*100/total_patients, 2))
    nonsmokers_message = "{} of your {} patients are smokers, which is {}%".format(nonsmokers, total_patients, round(nonsmokers*100/total_patients, 2))
    popup(smokers_message + "\n\n" + nonsmokers_message)

master.title("Smoking Status Tracker")
header = Label(master, text = "Please enter the following information:")

first_name = StringVar()
firstName_label = Label(master, text = "First name: \n (letters only)")
firstName_entry = Entry(master, width = 15, textvariable = first_name)

last_name = StringVar()
lastName_label = Label(master, text = "Last name: \n (letters only)")
lastName_entry = Entry(master, width = 15, textvariable = last_name)

birth_year = StringVar()
birthDate_label = Label(master, text = "Birth Year \n (4 digits):")
birthDate_entry = Entry(master, width = 15, textvariable = birth_year)

smoking_status = IntVar()
smokingStatus_label = Label(master, text = "Smoking Status:")
smokingStatus_Option1 = Radiobutton(master, text = "Smoker", variable = smoking_status, value = 1)
smokingStatus_Option2 = Radiobutton(master, text = "Non-smoker", variable = smoking_status, value = 0)
smokingStatus_Option2.select()

addNew_button = Button(master, text = "Add New Patient", 
                                                    command = lambda : create_patient(
                                                        first_name.get(), 
                                                        last_name.get(), 
                                                        birth_year.get(), 
                                                        smoking_status.get())
                                                        )
updateExisting_button = Button(master, text = "Update Existing Patient", 
                                                    command = lambda : update_patient(
                                                        first_name.get(), 
                                                        last_name.get(), 
                                                        birth_year.get(), 
                                                        smoking_status.get())
                                                        )
viewStats_button = Button(master, text = "View Stats", command = viewStats)

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
addNew_button.grid(row = 5, column = 1)
updateExisting_button.grid(row = 6, column = 1)
viewStats_button.grid(row = 7, column = 1)

master.grid_columnconfigure((0,2), weight = 1) # keeps columns centered in full screen

master.mainloop()