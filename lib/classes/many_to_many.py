# lib/classes/many_to_many.py

class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = title
        self.results = []
        self.players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("can't set attribute")

    def add_result(self, result):
        if result not in self.results:
            self.results.append(result)
        if result.player not in self.players:
            self.players.append(result.player)

    def average_score(self, player):
        scores = [res.score for res in self.results if res.player == player]
        if scores:
            return sum(scores) / len(scores)
        return 0


class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters")
        self._username = username
        self.results = []
        self.games = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters")
        self._username = value

    def add_result(self, result):
        if result not in self.results:
            self.results.append(result)
        if result.game not in self.games:
            self.games.append(result.game)

    def has_played_game(self, game):
        return game in self.games

    def num_times_played(self, game):
        return sum(1 for res in self.results if res.game == game)


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("player must be a Player instance")
        if not isinstance(game, Game):
            raise TypeError("game must be a Game instance")
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("score must be an integer between 1 and 5000")

        self._player = player
        self._game = game
        self._score = score

        # Add result to game and player
        game.add_result(self)
        player.add_result(self)

        # Add to global list
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        raise AttributeError("can't set attribute")
