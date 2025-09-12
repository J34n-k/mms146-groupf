"""
MMS 146 - Jeopardy Game Project
Group F

This file contains the Player class, which represents a single
player in the game. Each Player has a name, score, and attempts.
The class also enforces a maximum number of players allowed.
"""

class Player:
    """
    Represents a single player in the game with a username,
    score tracking, and attempt count.
    """

    # Class attributes
    max_players = 3
    players_created = 0

    def __init__(self, name):
        """
        Initialize a player with a name, score set to zero,
        and zero attempts. Enforces the maximum player limit.
        """
        if Player.players_created >= Player.max_players:
            raise Exception("Maximum number of players reached.")

        self.__name = name
        self.__score = 0
        self.__attempts = 0
        Player.players_created += 1

    def get_name(self):
        """Returns the player's name."""
        return self.__name

    def get_score(self):
        """Returns the player's current score."""
        return self.__score

    def add_score(self, points):
        """Adds points to the player's score."""
        self.__score += points

    def deduct_score(self, points):
        """Deducts points from the player's score (does not go below zero)."""
        self.__score -= points
        if self.__score < 0:
            self.__score = 0

    def reset_score(self):
        """Resets the player's score and attempts to zero."""
        self.__score = 0
        self.__attempts = 0
    
    def reset_score(self):
        self.__score = 0
        self.__attempts = 0
        
    def __str__(self):
        """String representation for debugging or display."""
        return f"Player: {self.__name}, Score: {self.__score}, Attempts: {self.__attempts}"

