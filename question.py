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

    def __str__(self):
        """String representation for debugging or display."""
        return f"{self.question} ({self.points} pts)"