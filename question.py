"""
MMS 146 - Jeopardy Game Project
Group F

This file contains the Question class, which represents a single
trivia question in the game. Each GameAnswer object stores the question,
the correct answer, its point value, and whether it has already been answered.
"""

class Question:
    """
    Represents a single trivia question with its correct answer and point value.
    """

    def __init__(self, question, answer, points):
        self.question = question      # The trivia question
        self.answer = answer          # The correct answer
        self.points = points          # Point value for this question
        self.answered = False         # To track if the question was already used

    def check_answer(self, player_answer):
        """
        Checks if the player's answer matches the correct one.
        Marks the question as answered regardless of correctness.
        Returns True if correct, False otherwise.
        """
        self.answered = True
        return player_answer.strip().lower() == self.answer.strip().lower()
    def mark_answered(self):
        """Marks the question as answered."""
        self.answered = True
        
    def __str__(self):
        """String representation for debugging or display."""
        return f"{self.question} ({self.points} pts)"

CATEGORIES = {
    "FACULTY": {
        100: Question("Who is the current Chancellor of the UPOU?", "Joane V. Serrano, PhD.", 100),
        200: Question("Who is the Vice Chancellor for Academic Affairs?", "Aurora V. Lacaste, PhD.", 200),
        300: Question("Who is the University Registrar?", "Blancaflor P. Arada", 300),
        400: Question("Who is the current Dean for the Faculty of Information and Communication Studies?", "Assoc. Prof. Roberto B. Figueroa Jr.", 400),
        500: Question("Who is the Program Chair for Bachelor of Arts in Multimedia Studies?", "Dr. Benigno B. Agapito, Jr.", 500),
    },
    "FACILITIES": {
        100: Question("How many facilities are within the UPOU Campus in Los Banos, Laguna?", "6", 100),
        200: Question("This facility room could be used for a catered dining or a socialization gathering.", "Academic Residences Cafeteria", 200),
        300: Question("This facility can be used for large conferences and has 100-200 seating capacity.", "Centennial Center for Digital Learning (CCDL)", 300),
        400: Question("A room within the campus perfect for intimate gatherings, live streaming or podcasting as it only caters to 25-30 pax.", "Sandbox", 400),
        500: Question("A room that has the oblation and can be used for roundtable meetings.", "Oblation Hall", 500),
    },
    "UPOU HISTORY": {
        100: Question("In what year was the University of the Philippines Open University (UPOU) established?", "1995", 100),
        200: Question("UPOU is the _____ constituent university of the UP System.", "5th", 200),
        300: Question("What was the first program offered by UPOU when it was founded?", "Diploma in Distance Education", 300),
        400: Question("Where is the physical campus of UPOU located?", "Los Baños, Laguna", 400),
        500: Question("What iconic UP symbol can also be found at the UPOU campus in Los Baños?", "The Oblation", 500),
    },
    "UPOU ONLINE LEARNING TOOLS": {
        100: Question("What is the official online learning platform used by UPOU students?", "MyPortal (based on Moodle)", 100),
        200: Question("What is the official online library service of UPOU?", "UPOU Digital Library", 200),
        300: Question("Which student organization serves as the official student council of UPOU?", "UPOU Student Council (UPOU SC)", 300),
        400: Question("What is the name of the UPOU’s open access journal?", "IJDE (International Journal on Open and Distance e-Learning)", 400),
        500: Question("Which platform does UPOU use for live webcasting of academic events and lectures?", "UPOU Networks", 500),
    },
}
