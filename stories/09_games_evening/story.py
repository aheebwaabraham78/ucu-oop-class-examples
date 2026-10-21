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

# ============================================================
# FOUNDATION TASK 2: GameCredits.add_more(amount)
# ============================================================

class GameCredits:
    """Manage the credits available to a player."""

    def __init__(self, amount=0):
        if not isinstance(amount, int) or isinstance(amount, bool) or amount < 0:
            raise ValueError("Initial credits must be non-negative.")
        self.amount = amount

    def add_more(self, amount):
        if not isinstance(amount, int) or isinstance(amount, bool) or amount <= 0:
            raise ValueError("Amount must be a positive integer.")

        self.amount += amount
        return self.amount

    def spend(self, amount):
        if not isinstance(amount, int) or isinstance(amount, bool) or amount < 0:
            raise ValueError("Spending amount must be non-negative.")

        if amount > self.amount:
            return False

        self.amount -= amount
        return True
   ============================================================

class TriviaFromMemory(GameChoice):
    """A trivia game with a specified number of questions."""

    def __init__(self, questions):
        if (
            not isinstance(questions, int)
            or isinstance(questions, bool)
            or questions <= 0
        ):
            raise ValueError("Questions must be a positive integer.")

        super().__init__("Trivia from Memory")
        self.questions = questions

    def credit_cost(self):
        return self.questions
        # ============================================================
# FOUNDATION TASK 4: affordable(choices, limit)
# ============================================================

def affordable(choices, limit):
    """Return the games whose costs do not exceed the limit."""

    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 0:
        raise ValueError("Limit must be a non-negative integer.")

    return [
        game for game in choices
        if isinstance(game, GameChoice) and game.credit_cost() <= limit
    ]

# ============================================================
# FOUNDATION TASK 5: GamesEvening.summary()
# FOUNDATION TASK 7: GamesEvening.cancel_last()
# FOUNDATION TASK 8: GamesEvening.complete_bundle()
# ============================================================

class GamesEvening:
    """Organise game choices for the hostel games evening."""

    def __init__(self, title="The Hostel Games Evening"):
        self.title = title
        self.choices = []
        self.history = []

    def add_game(self, game):
        if not isinstance(game, GameChoice):
            raise TypeError("Only valid game choices can be added.")

        self.choices.append(game)
        self.history.append(f"Added: {game.name}")

    def summary(self):
        total = sum(game.credit_cost() for game in self.choices)
        names = ", ".join(game.name for game in self.choices)

        if not names:
            names = "No games selected"

        return (
            f"{self.title}\n"
            f"Games: {names}\n"
            f"Number of games: {len(self.choices)}\n"
            f"Total credits: {total}"
        )

    def cancel_last(self):
        if not self.choices:
            return None

        removed = self.choices.pop()
        self.history.append(f"Cancelled: {removed.name}")
        return removed

    def complete_bundle(self, choices):
        if not isinstance(choices, (list, tuple)):
            raise TypeError("Bundle must be a list or tuple.")

        if not all(isinstance(game, GameChoice) for game in choices):
            raise TypeError("Every bundle item must be a game.")

        self.choices.extend(choices)
        self.history.append(f"Added bundle of {len(choices)} games")
        return self.summary()

# ============================================================
# LATER TOPIC A3: JSON save/load
# ============================================================

def game_to_dict(game):
    """Convert a game into a JSON-compatible dictionary."""

    if isinstance(game, RacingGame):
        return {"type": "racing", "races": game.races}

    if isinstance(game, TriviaFromMemory):
        return {"type": "trivia", "questions": game.questions}

    if isinstance(game, QuickPractice):
        return {"type": "practice", "minutes": game.minutes}

    if type(game) is GameChoice:
        return {
            "type": "basic",
            "name": game.name,
            "credits": game.credits,
        }

    raise TypeError(f"Unsupported game type: {type(game).__name__}")


def game_from_dict(data):
    """Validate a JSON game record and recreate its game."""

    if not isinstance(data, dict):
        raise ValueError("Each game record must be an object.")

    game_type = data.get("type")

    try:
        if game_type == "racing":
            return RacingGame(data["races"])

        if game_type == "trivia":
            return TriviaFromMemory(data["questions"])

        if game_type == "practice":
            return QuickPractice(data["minutes"])

        if game_type == "basic":
            return GameChoice(data["name"], data["credits"])

    except KeyError as error:
        raise ValueError(f"Missing required game field: {error}") from error

    raise ValueError(f"Unknown game type: {game_type}")


def save_evening(evening, filename="games_evening.json"):
    """Save a games evening to JSON."""

    if not isinstance(evening, GamesEvening):
        raise TypeError("Expected a GamesEvening object.")

    data = {
        "title": evening.title,
        "choices": [game_to_dict(game) for game in evening.choices],
        "history": evening.history,
    }

    path = Path(filename)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def load_evening(filename="games_evening.json"):
    """Load a games evening from JSON."""

    path = Path(filename)
    data = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        raise ValueError("Saved evening must be a JSON object.")

    title = data.get("title")
    choices = data.get("choices")
    history = data.get("history", [])

    if not isinstance(title, str):
        raise ValueError("Saved title must be text.")

    if not isinstance(choices, list):
        raise ValueError("Saved choices must be a list.")

    if not isinstance(history, list) or not all(
        isinstance(item, str) for item in history
    ):
        raise ValueError("Saved history must contain text entries.")

    evening = GamesEvening(title)
    evening.choices = [game_from_dict(item) for item in choices]
    evening.history = history
    return evening


# ============================================================
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

