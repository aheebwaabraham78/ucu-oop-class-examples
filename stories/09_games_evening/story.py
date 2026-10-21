"""The Hostel Games Evening
Group 3 / Catch-up Group C3

"""

import json
from pathlib import Path


# ============================================================
# FOUNDATION TASK 1: RacingGame
# ============================================================

class GameChoice:
    """Base class for games available at the hostel."""

    def __init__(self, name, credits=2):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Game name must not be empty.")
        if not isinstance(credits, int) or isinstance(credits, bool) or credits < 0:
            raise ValueError("Credits must be a non-negative integer.")

        self.name = name
        self.credits = credits

    def credit_cost(self):
        return self.credits

    def play(self):
        return f"{self.name} was played successfully."

    def __str__(self):
        return f"{self.name} ({self.credit_cost()} credits)"


class RacingGame(GameChoice):
    """A racing game costs two credits per race."""

    def __init__(self, races):
        if not isinstance(races, int) or isinstance(races, bool) or races <= 0:
            raise ValueError("Races must be a positive integer.")

        super().__init__("Racing game")
        self.races = races

    def credit_cost(self):
        return self.races * 2

 ============================================================
# LATER TOPIC A4: Factory and Single Responsibility Principle
# ============================================================

class GameFactory:
    """Create game objects based on a requested type."""

    @staticmethod
    def create(game_type, **kwargs):
        if not isinstance(game_type, str):
            raise ValueError("Game type must be text.")

        game_type = game_type.lower()

        if game_type == "racing":
            return RacingGame(**kwargs)

        if game_type == "trivia":
            return TriviaFromMemory(**kwargs)

        if game_type == "practice":
            return QuickPractice(**kwargs)

        if game_type == "basic":
            return GameChoice(**kwargs)

        raise ValueError(f"Unknown game type: {game_type}")


def display_summary(evening):
    """Display the summary without managing game state."""
    print(evening.summary())


# ============================================================
# DEMONSTRATIONS OF THE FOUNDATION TASKS
# ============================================================

def demo_foundation_tasks():
    print("\n=== FOUNDATION TASK 1: RACING GAME ===")
    racing = RacingGame(3)
    print(racing)
    print(f"Races: {racing.races}")
    print(f"Credits required: {racing.credit_cost()}")

    print("\n=== FOUNDATION TASK 2: GAME CREDITS ===")
    wallet = GameCredits(5)
    wallet.add_more(5)
    print(f"Credits after adding: {wallet.amount}")

    print("\n=== FOUNDATION TASK 3: TRIVIA ===")
    trivia = TriviaFromMemory(4)
    print(trivia)
    print(f"Questions: {trivia.questions}")

    print("\n=== FOUNDATION TASK 4: AFFORDABLE GAMES ===")
    practice = QuickPractice(10)
    games = [racing, trivia, practice, GameChoice("Ludo", 2)]

    for game in affordable(games, 4):
        print(game)

    print("\n=== FOUNDATION TASK 5: EVENING SUMMARY ===")
    evening = GamesEvening()
    evening.complete_bundle(games)
    display_summary(evening)

    print("\n=== FOUNDATION TASK 6: QUICK PRACTICE ===")
    print(practice)
    print(f"Practice duration: {practice.minutes} minutes")

    print("\n=== FOUNDATION TASK 7: CANCEL LAST GAME ===")
    removed = evening.cancel_last()
    print(f"Cancelled: {removed.name if removed else 'Nothing to cancel'}")

    print("\n=== FOUNDATION TASK 8: COMPLETE BUNDLE ===")
    evening.complete_bundle([GameChoice("Football", 3)])
    display_summary(evening)


# ============================================================
# DEMONSTRATIONS OF SELECTED LATER TOPICS
# ============================================================

def demo_a2_safe_play():
    print("\n=== A2: CUSTOM EXCEPTIONS AND SAFE PLAY ===")
    evening = StrictGamesEvening()
    wallet = GameCredits(10)

    try:
        message = evening.safe_play(RacingGame(3), wallet)
        print(message)
        print(f"Remaining credits: {wallet.amount}")
    except (InsufficientCreditsError, InvalidGameError) as error:
        print(f"Play refused: {error}")

    try:
        evening.safe_play(RacingGame(10), wallet)
    except InsufficientCreditsError as error:
        print(f"Expected refusal: {error}")


def demo_a3_json():
    print("\n=== A3: JSON SAVE AND LOAD ===")
    evening = GamesEvening()
    evening.complete_bundle([
        RacingGame(3),
        TriviaFromMemory(4),
        QuickPractice(10),
        GameChoice("Ludo", 2),
    ])

    filename = "games_evening_demo.json"

    try:
        save_evening(evening, filename)
        restored = load_evening(filename)
        print("Saved and loaded successfully.")
        print(restored.summary())
    finally:
        Path(filename).unlink(missing_ok=True)


def demo_a4_factory():
    print("\n=== A4: GAME FACTORY ===")
    games = [
        GameFactory.create("racing", races=2),
        GameFactory.create("trivia", questions=5),
        GameFactory.create("practice", minutes=10),
        GameFactory.create("basic", name="Ludo", credits=2),
    ]

    for game in games:
        print(f"{game} — cost: {game.credit_cost()} credits")


# ============================================================
# MAIN
# ============================================================

def main():
    demo_foundation_tasks()
    demo_a2_safe_play()
    demo_a3_json()
    demo_a4_factory()


if __name__ == "__main__":
    main()
