from pyscript import document, display

# List of Hogwarts students
# retrieved list of members from AI by generating
students = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Draco Malfoy",
    "Luna Lovegood",
    "Neville Longbottom",
    "Ginny Weasley",
    "Fred Weasley",
    "George Weasley",
    "Cedric Diggory",
    "Cho Chang",
    "Seamus Finnigan",
    "Dean Thomas",
    "Parvati Patil",
    "Padma Patil",
    "Lavender Brown",
    "Pansy Parkinson",
    "Gregory Goyle",
    "Vincent Crabbe",
    "Colin Creevey"
]


def verify(e):
    # Clear the old result
    document.getElementById("result-box").innerHTML = ""

    # Get the names from the input boxes
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()

    # Put the first and last name together
    full_name = f"{first_name.title()} {last_name.title()}"

    # Check if either input is empty
    is_empty = first_name == "" or last_name == ""

    # Check if the name is in the student list
    is_member = full_name in students

    # Messages depending on whether the student is in the list
    messages = [
        f"Sorry {full_name}, your name is not on the list. Maybe next time?",
        f"Congratulations {full_name}! You are a student at Hogwarts University. 🧹"
    ]

    # This basically adds a message for empty inputs

    # Not an empty input = use the membership message
    # One of the inputs is empty = tells user to enter both names

    empty_messages = [
        messages[is_member],
        "Please enter both your first and last name."
    ]

    # This will get the message to show
    result_message = empty_messages[is_empty]

    # Show the result
    display(result_message, target="result-box")