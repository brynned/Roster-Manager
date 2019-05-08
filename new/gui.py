from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Initialize empty dictionary
roster_dict = dict()

# Initialize Athlete class 
class Athlete:
    def __init__(self, name, year, position, number, height, weight, hometown, state, school):
        self.name = name
        self.year = year
        self.position = position
        self.number = number
        self.height = height
        self.weight = weight
        self.hometown = hometown
        self.state = state
        self.school = school

# GUI setup
window = Tk()
window.title("Welcome to the PyRos Roster Management System")

# Tab setup
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab8 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Display Roster")
tab_control.add(tab2, text="Add Athlete")
tab_control.add(tab3, text="Delete Athlete")
tab_control.add(tab4, text="Edit Athlete")
tab_control.add(tab5, text="Save Data")
tab_control.add(tab6, text="Load Data")
tab_control.add(tab7, text="Search")

# Tab 1

# Tab 2
Label(tab2, text="Full name:").grid(row=0)
Label(tab2, text="Year:").grid(row=1)
Label(tab2, text="Position:").grid(row=2)
Label(tab2, text="Number:").grid(row=3)
Label(tab2, text="Height:").grid(row=4)
Label(tab2, text="Weight:").grid(row=5)
Label(tab2, text="Hometown:").grid(row=6)
Label(tab2, text="State:").grid(row=7)
Label(tab2, text="School:").grid(row=8)

b1 = Entry(tab2, width=10) 
b1.grid(row=0, column=1)

b2 = Entry(tab2, width=10)
b2.grid(row=1, column=1)

b3 = Entry(tab2, width=10)
b3.grid(row=2, column=1)

b4 = Entry(tab2, width=10)
b4.grid(row=3, column=1)

b5 = Entry(tab2, width=10)
b5.grid(row=4, column=1)

b6 = Entry(tab2, width=10)
b6.grid(row=5, column=1)

b7 = Entry(tab2, width=10)
b7.grid(row=6, column=1)

b8 = Entry(tab2, width=10)
b8.grid(row=7, column=1)

b9 = Entry(tab2, width=10)
b9.grid(row=8, column=1)


# Tab 3
Label(tab3, text="Enter the name of the athlete to delete:").grid(row=0)
c1 = Entry(tab3, width=10)
c1.grid(row=0, column=1)

# Tab 4
Label(tab4, text="Enter the name of the athlete to edit:").grid(row=0)

d1 = Entry(tab4, width=10)
d1.grid(row=0, column=1)

Label(tab4, text="New Full name").grid(row=3)
Label(tab4, text="New Year").grid(row=4)
Label(tab4, text="New Position").grid(row=5)
Label(tab4, text="New Number").grid(row=6)
Label(tab4, text="New Height").grid(row=7)
Label(tab4, text="New Weight").grid(row=8)
Label(tab4, text="New Hometown").grid(row=9)
Label(tab4, text="New State").grid(row=10)
Label(tab4, text="New School").grid(row=11)

d2 = Entry(tab4, width=10)
d2.grid(column=1, row=3)

d3 = Entry(tab4, width=10)
d3.grid(column=1, row=4)

d4 = Entry(tab4, width=10)
d4.grid(column=1, row=5)

d5 = Entry(tab4, width=10)
d5.grid(column=1, row=6)

d6 = Entry(tab4, width=10)
d6.grid(column=1, row=7)

d7 = Entry(tab4, width=10)
d7.grid(column=1, row=8)

d8 = Entry(tab4, width=10)
d8.grid(column=1, row=9)

d9 = Entry(tab4, width=10)
d9.grid(column=1, row=10)

d10 = Entry(tab4, width=10)
d10.grid(column=1, row=11)

# Tab 5
Label(tab5, text="Click to save the current roster").grid(column=1)

# Tab 6
Label(tab6, text="Select a file to upload:").grid(column=1)


# Tab 7
Label(tab7, text="Select a category to search and then enter the info to search:").grid(row=0, column=1)
g1 = Entry(tab7)
selected = IntVar()
g1.grid(row=1, column=1)
rad1 = Radiobutton(tab7, text="Full Name", value=1, variable=selected)
rad2 = Radiobutton(tab7, text="Year", value=2, variable=selected)
rad3 = Radiobutton(tab7, text="Position", value=3, variable=selected)
rad4 = Radiobutton(tab7, text="Number", value=4, variable=selected)
rad5 = Radiobutton(tab7, text="Height", value=5, variable=selected)
rad6 = Radiobutton(tab7, text="Weight", value=6, variable=selected)
rad7 = Radiobutton(tab7, text="Hometown", value=7, variable=selected)
rad8 = Radiobutton(tab7, text="State", value=8, variable=selected)
rad9 = Radiobutton(tab7, text="School", value=9, variable=selected)
rad1.grid(column=2, row=0)
rad2.grid(column=3, row=0)
rad3.grid(column=4, row=0)
rad4.grid(column=5, row=0)
rad5.grid(column=6, row=0)
rad6.grid(column=7, row=0)
rad7.grid(column=8, row=0)
rad8.grid(column=9, row=0)
rad9.grid(column=10, row=0)



def clear():
    for w in tab1.winfo_children():
        w.destroy()
    btn1 = Button(tab1, text="Click to display roster!", command=displayRoster)
    btn1.grid(column=1)


def displayRoster():
    Label(tab1, text="Full name").grid(row=1, column=1)
    Label(tab1, text="Year").grid(row=1, column=2)
    Label(tab1, text="Position").grid(row=1, column=3)
    Label(tab1, text="Number").grid(row=1, column=4)
    Label(tab1, text="Height").grid(row=1, column=5)
    Label(tab1, text="Weight").grid(row=1, column=6)
    Label(tab1, text="Hometown").grid(row=1, column=7)
    Label(tab1, text="State").grid(row=1, column=8)
    Label(tab1, text="School").grid(row=1, column=9)
    
    i = 2
    for team_member in roster_dict:
        name = Label(tab1, text=roster_dict[team_member].name)
        name.grid(row=i, column=1)
        year = Label(tab1, text=roster_dict[team_member].year)
        year.grid(row=i, column=2)
        position = Label(tab1, text=roster_dict[team_member].position)
        position.grid(row=i, column=3)
        number = Label(tab1, text=roster_dict[team_member].number)
        number.grid(row=i, column=4)
        height = Label(tab1, text=roster_dict[team_member].height)
        height.grid(row=i, column=5)
        weight = Label(tab1, text=roster_dict[team_member].weight)
        weight.grid(row=i, column=6)
        hometown = Label(tab1, text=roster_dict[team_member].hometown)
        hometown.grid(row=i, column=7)
        state = Label(tab1, text=roster_dict[team_member].state)
        state.grid(row=i, column=8)
        school = Label(tab1, text=roster_dict[team_member].school)
        school.grid(row=i, column=9)
        i = i+1
    destroy = Button(tab1, text="Clear", command=clear)
    destroy.grid(row=0, column=9)

def addAthlete():
    name = b1.get()
    year = b2.get()
    position = b3.get()
    number = b4.get()
    height = b5.get()
    weight = b6.get()
    hometown = b7.get()
    state = b8.get()
    school = b9.get()
 
    athlete_info = Athlete(name, year, position, number, height, weight, hometown, state, school)
    roster_dict[name] = athlete_info

    b1.delete(0, END)
    b2.delete(0, END)
    b3.delete(0, END)
    b4.delete(0, END)
    b5.delete(0, END)
    b6.delete(0, END)
    b7.delete(0, END)
    b8.delete(0, END)
    b9.delete(0, END)

def deleteAthlete():
    athlete = c1.get()
    if athlete in roster_dict:
        del roster_dict[athlete]
    else:
        messagebox.showerror("Error", "Athlete not found on roster")
    c1.delete(0, END)

def editAthlete():
    athlete = d1.get()
    if athlete in roster_dict:
        team_member = roster_dict[athlete]
        team_member.name = d2.get()
        team_member.year = d3.get()
        team_member.position = d4.get()
        team_member.number = d5.get()
        team_member.height = d6.get()
        team_member.weight = d7.get()
        team_member.hometown = d8.get()
        team_member.state = d9.get()
        team_member.school = d10.get()
        del roster_dict[athlete]
        roster_dict[team_member.name] = team_member
    d1.delete(0, END)
    d2.delete(0, END)
    d3.delete(0, END)
    d4.delete(0, END)
    d5.delete(0, END)
    d6.delete(0, END)
    d7.delete(0, END)
    d8.delete(0, END)
    d9.delete(0, END)
    d10.delete(0, END)

def loadData():
    f =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    input_file = open(f, 'r')
    for line in input_file:
        data = line.split(",")
        member_info = Athlete(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])
        if member_info.name not in roster_dict:
            roster_dict[member_info.name]=member_info
    Label(tab6, text="Loaded data successfully!").grid(row=2, column=1)

def saveData():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    for name in roster_dict:
        team_member = roster_dict[name]
        f.write(team_member.name+","+team_member.year+","+team_member.position+","+team_member.number+","+team_member.height+","+team_member.weight+","+team_member.hometown+","+team_member.state+","+team_member.school+"\n")

def searchData():
    i = 6
    x = g1.get()
    search = selected.get()
    if search == 1:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].name:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 2:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].year:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 3:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].position:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 4:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].number:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 5:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].height:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 6:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].weight:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 7:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].hometown:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 8: 
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].state:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))
    elif search == 9:
        print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Year", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
        for team_member in roster_dict:
            if x == roster_dict[team_member].school:
                print('{:<25s}{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].name, roster_dict[team_member].year, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].state, roster_dict[team_member].school))

# Buttons
btn1 = Button(tab1, text="Display Roster", command=displayRoster)
btn1.grid(row=0, column=1)

btn2 = Button(tab2, text="Enter", command=addAthlete)
btn2.grid(row=9, column=1)

btn3 = Button(tab3, text="Enter", command=deleteAthlete)
btn3.grid(row=1, column=1)

btn4 = Button(tab4, text="Update Athlete Info", command=editAthlete)
btn4.grid(row=12, column=1)

btn5 = Button(tab5, text="Save", command=saveData)
btn5.grid(row=1, column=1)

btn6 = Button(tab6, text="Browse", command=loadData)
btn6.grid(column=1, row=1)

btn7 = Button(tab7, text="Search", command=searchData)
btn7.grid(row=3)

tab_control.pack(expand=1, fill='both')
window.mainloop()
