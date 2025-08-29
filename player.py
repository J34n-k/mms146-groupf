"""
MMS 146 - Jeopardy Game Project
Group F

This file contains the Player class, which represents a player in the
Jeopardy game. Each Player object stores the player’s name, score, and
number of attempts. It also enforces a maximum of three players.
"""

class Player:
    """
    Represents a single player in the game with their score and attempts.
    Keeps track of how many players have been created (max 3).
    """

  # Class attributes
    max_players = 3
    _players_created = 0

    def __init__(self, name):
        """
        Initialize a Player with a name, starting score of 0,
        and 0 attempts. Prevents creating more than 3 players.
        """
        if Player._players_created >= Player.max_players:
            raise Exception("Maximum number of players (3) has been reached!")

        self._name = name
        self._score = 0
        self._attempts = 0

        Player._players_created += 1


    def get_name(self):
        """Return the player's name."""
        return self._name

    def get_score(self):
        """Return the player's current score."""
        return self._score


    def add_score(self, points):
        """Add points to the score (for a correct answer)."""
        self._score += points
        self._attempts += 1

    def deduct_score(self, points):
        """Deduct points from the score (for a wrong answer)."""
        self._score -= points
        self._attempts += 1

    def reset_score(self):
        """Reset score and attempts (e.g., for a new game)."""
        self._score = 0
        self._attempts = 0

#Utility
    def __str__(self):
        """String representation of the player (for display/debugging)."""
        return f"Player: {self._name}, Score: {self._score}, Attempts: {self._attempts}"
