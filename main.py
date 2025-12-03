from pyscript import document

# Page 1 | Homepage

# Page 2 | Grade Calculator

def calculate_average(event=None):
    fn = document.getElementById("first-name").value
    ln = document.getElementById("last-name").value

    g_sci = float(document.getElementById("grade-science").value or 0)
    g_math = float(document.getElementById("grade-math").value or 0)
    g_eng = float(document.getElementById("grade-english").value or 0)
    g_fil = float(document.getElementById("grade-filipino").value or 0)
    g_ict = float(document.getElementById("grade-ict").value or 0)
    g_pe = float(document.getElementById("grade-pe").value or 0)

    weighted_total = (
        g_sci * 4 +
        g_math * 4 +
        g_eng * 3 +
        g_fil * 3 +
        g_ict * 3 +
        g_pe * 2
    )

    total_units = 4 + 4 + 3 + 3 + 3 + 2
    average = weighted_total / total_units

    output = (
        f"<h2>Results</h2>"
        f"<p>Name: {fn} {ln}</p>"
        f"<p>Science: {g_sci:.0f}</p>"
        f"<p>Math: {g_math:.0f}</p>"
        f"<p>English: {g_eng:.0f}</p>"
        f"<p>Filipino: {g_fil:.0f}</p>"
        f"<p>ICT: {g_ict:.0f}</p>"
        f"<p>PE: {g_pe:.0f}</p>"
        f"<h3>Your average grade is {average:.2f}</h3>"
    )

    document.getElementById("output").innerHTML = output

# Page 3 | Club Information

CLUBS = {
    "socsci": {
        "name": "SocSci Club",
        "description": "About history and philosophy.",
        "time": "Tuesday, 3:00 PM",
        "location": "Room 511",
        "moderator": "Sir. Wayne",
        "members": 25
    },
    "math": {
        "name": "Math Club",
        "description": "For math-loving people.",
        "time": "Wednesday, 3:00 PM",
        "location": "Room 409",
        "moderator": "Ms. Dela Cruz",
        "members": 67
    },
    "arts": {
        "name": "Arts Club",
        "description": "Creativity, painting, and art in general.",
        "time": "Monday, 4:00 PM",
        "location": "Art Studio",
        "moderator": "Sir. Howard",
        "members": 30
    },
    "coding": {
        "name": "Computer Club",
        "description": "Coding, robotics, and app-making.",
        "time": "Thursday, 3:30 PM",
        "location": "Computer Lab",
        "moderator": "Sir. Ramirez",
        "members": 24
    }
}

def show_club(event=None):
    club_id = event.target.id
    club = CLUBS[club_id]

    html = f"""
    <h4>{club['name']}</h4>
    <p><strong>Description:</strong> {club['description']}</p>
    <p><strong>Meeting Time:</strong> {club['time']}</p>
    <p><strong>Location:</strong> {club['location']}</p>
    <p><strong>Moderator:</strong> {club['moderator']}</p>
    <p><strong>Members:</strong> {club['members']}</p>
    """

    document.getElementById("club-output").innerHTML = html