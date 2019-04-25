roster_dict = dict()

class Athlete:
    def __init__(self, first_last, position, number, height, weight, hometown, home_state, school):
        self.first_last = first_last
        self.position = position
        self.number = number
        self.height = height
        self.weight = weight
        self.hometown = hometown
        self.home_state = home_state
        self.school = school

def displayRoster():
    current = 0
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
    print("\n")
    for team_member in roster_dict: 
        print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school)) 
        #print("Full Name: ", roster_dict[team_member].first_last)
        #print("Position: ", roster_dict[team_member].position)
        #print("Number: ", roster_dict[team_member].number)
        #print("Height: ", roster_dict[team_member].height)
        #print("Weight: ", roster_dict[team_member].weight)
        #print("Hometown: ", roster_dict[team_member].hometown)
        #print("State: ", roster_dict[team_member].home_state)
        #print("School: ", roster_dict[team_member].school)
    if len(roster_dict) is 0:
        print("The team roster is currently empty.")

def addAthlete(first_last, position, number, height, weight, hometown, home_state, school):
    athlete_info = Athlete(first_last, position, number, height, weight, hometown, home_state, school)
    roster_dict[first_last] = athlete_info

def deleteAthlete(athlete_to_delete):
    if athlete_to_delete in roster_dict:
        del roster_dict[athlete_to_delete]
    else:
        print(athlete_to_delete, " was not found in the team roster.")

def editAthlete(athlete_to_edit):
    if athlete_to_edit in roster_dict:
        team_member = roster_dict[athlete_to_edit]
        print("Make changes to whichever field needs to be edited.")
        team_member.first_last = input("Enter the new name of the athlete: ")
        team_member.position = input("New position: ")
        team_member.number = input("New number: ")
        team_member.height = input("New height: ")
        team_member.weight = input("New weight: ")
        team_member.hometown = input("New hometown: ")
        team_member.home_state = input("New state: ")
        team_member.school = input("New school: ")
        del roster_dict[athlete_to_edit]
        roster_dict[team_member.first_last] = team_member
    else:
        print(athlete_to_edit, " was not found in the team roster.")

def saveFile(file_name, output):
    for first_last in roster_dict:
        team_member = roster_dict[first_last]
        output.write(team_member.first_last+","+team_member.position+","+team_member.number+","+team_member.height+","+team_member.weight+","+team_member.hometown+","+team_member.home_state+","+team_member.school+"\n")
    output.close()
    print("Saving data...")
    print("Data saved!")

def loadFile(file_name, input_file):
    for line in input_file:
        line = line.strip()
        data = line.split(",")
        member_info = Athlete(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
        if member_info.first_last not in roster_dict:
            roster_dict[member_info.first_last]=member_info
    print("Loading data...")
    print("Data loaded successfully!")

def nameChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School")) 
    for team_member in roster_dict:
        if x == roster_dict[team_member].first_last:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school))

def positionChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School")) 
    for team_member in roster_dict:
        if x == roster_dict[team_member].position:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school)) 

def numberChoice(x):
    for team_member in roster_dict:
        if x == roster_dict[team_member].number:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))

def heightChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School")) 
    for team_member in roster_dict:
        if x == roster_dict[team_member].height:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school))

def weightChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
    for team_member in roster_dict:
        if x == roster_dict[team_member].height:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school))

def hometownChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
    for team_member in roster_dict:
        if x == roster_dict[team_member].hometown:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school))

def stateChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
    for team_member in roster_dict:
        if x == roster_dict[team_member].home_state:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school))

def schoolChoice(x):
    print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format("Name", "Position", "Number", "Height", "Weight", "Hometown", "State", "School"))
    for team_member in roster_dict:
        if x == roster_dict[team_member].school:
            print('{:<25s}{:<25s}{:<20s}{:<20s}{:<20s}{:<20s}{:<20s}{:<12s}'.format(roster_dict[team_member].first_last, roster_dict[team_member].position, roster_dict[team_member].number, roster_dict[team_member].height, roster_dict[team_member].weight, roster_dict[team_member].hometown, roster_dict[team_member].home_state, roster_dict[team_member].school))

