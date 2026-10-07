
teams = []           
individuals = []     
participants = []    

MAX_TEAMS = 4
MAX_MEMBERS = 5
MAX_INDIVIDUALS = 20
EVENTS = ["Sporting", "Academic"]
POINTS = {1:10, 2:5, 3:2}

def display_menu():
    print("\n===== MAIN MENU =====")
    print("1. Register")
    print("2. Enter Results")
    print("3. View Leaderboard")
    print("4. Exit")

def register():
    print("\n--- REGISTRATION ---")
    print("1. Register Team")
    print("2. Register Individual")
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        if len(teams) >= MAX_TEAMS:
            print("Max 4 teams only!")
            return
        
        team_name = input("Enter team name: ").strip()
        if team_name in teams:
            print("Team already exists!")
            return

        members = []
        for i in range(MAX_MEMBERS):
            name = input(f"Member {i+1} name: ").strip()
            members.append(name)

        print("\nEvents:")
        print("1. Sporting")
        print("2. Academic")
        e_choice = input("Choose event (1 or 2): ")
        event = EVENTS[0] if e_choice == "1" else EVENTS[1]

        teams.append(team_name)
        participants.append({"name": team_name, "type": "team", "event": event, "points": 0})
        print(f"{team_name} registered for {event}")

    elif choice == "2":
        if len(individuals) >= MAX_INDIVIDUALS:
            print("Max 20 individuals only!")
            return

        name = input("Enter your name: ").strip()

        for p in participants:
            if p["name"] == name and p["type"] == "individual":
                print("Already registered!")
                return

        print("\nEvents:")
        print("1. Sporting")
        print("2. Academic")
        e_choice = input("Choose event (1 or 2): ")
        event = EVENTS[0] if e_choice == "1" else EVENTS[1]

        individuals.append(name)
        participants.append({"name": name, "type": "individual", "event": event, "points": 0})
        print(f" {name} registered for {event}")

    else:
        print("Invalid choice")

def enter_results():
    print("\n--- ENTER RESULTS ---")
    print("1. Sporting")
    print("2. Academic")
    e_choice = input("Choose event (1 or 2): ")
    event = EVENTS[0] if e_choice == "1" else EVENTS[1]

    event_participants = [p for p in participants if p["event"] == event]
    if not event_participants:
        print("No one registered here!")
        return

    print("\nParticipants:")
    for p in event_participants:
        print("-", p["name"])

    print("\nEnter winners:")
    for place in [1,2,3]:
        person = input(f"{place}st place: ").strip()
        for p in event_participants:
            if p["name"] == person:
                p["points"] = POINTS[place]
                break
    print("Results saved")

def view_leaderboard():
    print("\n===== LEADERBOARD =====")
   
    team_list = [p for p in participants if p["type"] == "team"]
    ind_list = [p for p in participants if p["type"] == "individual"]

   
    team_list.sort(key=lambda x: x["points"], reverse=True)
    ind_list.sort(key=lambda x: x["points"], reverse=True)

   
    print("\n--- TEAMS ---")
    for num, t in enumerate(team_list, 1):
        print(f"{num}. {t['name']} | Event: {t['event']} | Points: {t['points']}")

    
    print("\n--- INDIVIDUALS ---")
    for num, i in enumerate(ind_list, 1):
        print(f"{num}. {i['name']} | Event: {i['event']} | Points: {i['points']}")

while True:
    display_menu()
    option = input("\nEnter choice: ")

    if option == "1":
        register()
    elif option == "2":
        enter_results()
    elif option == "3":
        view_leaderboard()
    elif option == "4":
        print("Program ended")
        break
    else:
        print("Invalid option, try again")