from question import CATEGORIES as DEFAULT_CATEGORIES
from category import Category
from GameGrid import GameGrid
from player import Player

def from_default():
    categories = []
    for cat_name, questions in DEFAULT_CATEGORIES.items():
        cat = Category(cat_name)
        for points, q in sorted(questions.items()):
            # q is already a Question instance from question.py's DEFAULT_CATEGORIES
            cat.add_question(q)
        categories.append(cat)
    return categories

def prompt_int(msg, valid=None):
    while True:
        raw = input(msg).strip()
        try:
            val = int(raw)
            if valid and val not in valid:
                print(f"Please choose one of: {sorted(valid)}")
                continue
            return val
        except ValueError:
            print("Please enter a number.")

def main():
    print("=== Welcome to Group F's Jeopardy Game! (UPOU Version) ===")

    # Players
    n_players = prompt_int("How many players? (1-3): ", valid={1,2,3})
    players = []
    for i in range(n_players):
        name = input(f"Enter name for Player {i+1}: ").strip() or f"Player {i+1}"
        players.append(Player(name))

    # Build the board
    grid = GameGrid()
    for cat in from_default():
        grid.add_category(cat)

    current_idx = 0
    while True:
        available = grid.get_available_questions()
        if not available:
            print("No questions left. Game over!")
            break

        print("Available Board:")
        for cat_name, values in available.items():
            print(f"  {cat_name}: {', '.join(map(str, values))}")
        print()

        player = players[current_idx]
        print(f"It's {player.get_name()}'s turn")

        # Choose category
        categories = list(available.keys())
        for i, cname in enumerate(categories, 1):
            print(f"  {i}. {cname}")
        choice = prompt_int("Choose a category (number): ", valid=set(range(1, len(categories)+1)))
        chosen_cat_name = categories[choice-1]

        # Choose value
        values = set(available[chosen_cat_name])
        value = prompt_int(f"Choose a point value from {sorted(values)}: ", valid=values)

        # Ask question
        # Find the actual Question
        question = None
        for cat in grid.get_categories():
            if cat.get_name() == chosen_cat_name:
                question = cat.get_question(value)
                break

        if question is None or question.answered:
            print("That question is no longer available. Choose again.")
            continue

        print(f"For {value} points: {question.question}")
        answer = input("Your answer: ")

        if question.check_answer(answer):
            print("Correct!")
            player.add_score(question.points)
        else:
            print(f"Incorrect. Correct answer was: {question.answer}")
            player.deduct_score(question.points)

        # Next player's turn
        current_idx = (current_idx + 1) % len(players)

        # Show scores
        print("Scores:")
        for p in players:
            print(f"  {p.get_name()}: {p.get_score()}" )
        print("-"*40)

    # Final scores
    print("FINAL SCORES:")
    players_sorted = sorted(players, key=lambda p: p.get_score(), reverse=True)
    for p in players_sorted:
        print(f"  {p.get_name()}: {p.get_score()}" )
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
