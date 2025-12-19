from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "chess": {
                "name": "Chess Club",
                "description": "A club for chess enthusiasts of all skill levels.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 405",
                "advisor": "Mr. Santos",
                "members": 20,
                "category": "Academic"
            
            },
            "basketball": {
                "name": "Basketball Club",
                "description": "For students interested in Basketball to become the GOAT.",
                "meeting_time": "Every Monday 3:00-5:00 PM",
                "location": "Quadrangle",
                "advisor": "Mr. Mariano",
                "members": 22,
                "category": "Sports"
            },
            "robotics": {
                "name": "Robotics Club",
                "description": "Design, build, and program robots for competitions.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Computer Lab",
                "advisor": "Ms. onofre",
                "members": 18,
                "category": "Academic"
            },
            "volleyball": {
                "name": "Debate Club",
                "description": "Those who want to join Volleyball club to fly high!",
                "meeting_time": "Every Wednesday 3:00-5:00 PM",
                "location": "Room 507",
                "advisor": "Mr. Mariano",
                "members": 12,
                "category": "Sports"
            },
            "art": {
                "name": "Art Club",
                "description": "Explore various art mediums and techniques.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Balajadia",
                "members": 20,
                "category": "Arts"
            },
             "Math": {
                "name": "O.M.G Club",
                "description": "Indulge in an experience of formulas and numbers.",
                "meeting_time": "Every Friday 2:30-4:30 PM",
                "location": "Room 222",
                "advisor": "Ms. Lim",
                "members": 13,
                "category": "Aacademic"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }


def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")