'''
MMS 146 - Jeopardy Game Group Project

This file contains the code for the GameGrid class. Feel free to edit to match the
other codes for the game to work. I based this on the uml diagrams.

GameGrid mainly focuses if there are any more questions left for each topic/catgeory.
It also marks the ones that are already given to the players.
'''

class GameGrid:
    def __init__(self):
        self.__categories = []

    def add_category(self, category):
        self.__categories.append(category)

    def get_available_questions(self):
        available = {}
        for category in self.__categories:
            available_vals = category.get_available_values()
            if available_vals:
                available[category.get_name()] = available_vals
        return available

    def mark_answered(self, category_name, value):
        for category in self.__categories:
            if category.get_name() == category_name:
                question = category.get_question(value)
                if question:
                    question.mark_answered()
                    return True
        return False

    def get_categories(self):
        return list(self.__categories)