"""
MMS 146 - Jeopardy Game Project
Group F

This file tests the Question class to make sure it works correctly.
"""

from question import Question

def run_tests():
    # Test 1: Correct answer
    q1 = Question("Who is the current Chancellor of the UPOU?", "Joane V. Serrano, PhD.", 100)
    print(q1)  
    print("Testing correct answer:", q1.check_answer("Joane V. Serrano, PhD."))  # Expected: True
    print("Answered already?", q1.answered)  # Expected: True
    print()

    # Test 2: Incorrect answer
    q2 = Question("In what year was UPOU established?", "1995", 200)
    print(q2)
    print("Testing incorrect answer:", q2.check_answer("2000"))  # Expected: False
    print("Answered already?", q2.answered)  # Expected: True
    print()

    # Test 3: Case-insensitivity
    q3 = Question("What is the official online library of UPOU?", "UPOU Digital Library", 300)
    print(q3)
    print("Testing case-insensitive match:", q3.check_answer("upou digital library"))  # Expected: True
    print("Answered already?", q3.answered)  # Expected: True
    print()

if __name__ == "__main__":
    run_tests()