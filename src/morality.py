from collections import Counter


class Player(object):
    action_one = "Cooperator"
    action_two = "Cheater"

    def __init__(self, role, action) -> None:
        self.last_role = ""
        self.role = role
        self.registry: int = 0
        self.action = action

    def choose_action(self, other_object):
        if self.action == other_object.get_action() == self.action_one:
            self.add_registry(2)
            other_object.add_registry(2)
        elif self.action == other_object.get_action() == self.action_two:
            pass
        elif self.action == self.action_one:
            self.add_registry(-1)
            other_object.add_registry(3)
        else:
            self.add_registry(3)
            other_object.add_registry(-1)

    def role_proper(self, other_object):
        pass

    def add_registry(self, num: int) -> None:
        self.last_role = self.action
        self.registry += num

    def get_registry(self) -> int:
        return self.registry

    def get_last_role(self) -> str:
        return self.last_role

    def get_action(self) -> str:
        return self.action

    def get_role(self) -> str:
        return self.role

    def reset(self) -> str:
        self.registry = 0
        self.last_role = ""


class Cheater(Player):
    def __init__(self, max_rounds=None) -> None:
        super().__init__("Cheater", self.action_two)


class Cooperator(Player):
    def __init__(self, max_rounds=None) -> None:
        super().__init__("Cooperator", self.action_one)


class Copycat(Player):
    def __init__(self, max_rounds=None) -> None:
        super().__init__("Copycat", self.action_one)

    def role_proper(self, other_object):
        if other_object.get_last_role() != "":
            self.action = other_object.get_last_role()

    def reset(self) -> str:
        self.action = self.action_one
        super().reset()


class Grudger(Player):
    def __init__(self, max_rounds=None) -> None:
        super().__init__("Grudger", self.action_one)

    def role_proper(self, other_object):
        if other_object.get_last_role() == self.action_two:
            self.action = self.action_two

    def reset(self) -> str:
        self.action = self.action_one
        super().reset()


class Rat(Player):
    def __init__(self, max_rounds) -> None:
        self.move = 0
        self.max_round = max_rounds
        super().__init__("Rat", self.action_one)

    def role_proper(self, other_object):
        if self.move == self.max_round - 1:
            self.action = self.action_two
        elif other_object.get_last_role() != "":
            self.action = other_object.get_last_role()
        self.move += 1

    def reset(self) -> str:
        self.move = 0
        self.action = self.action_one
        super().reset()


class Detective(Player):
    def __init__(self, max_rounds=None) -> None:
        self.mode_gunder: int = 0
        self.moves = 0
        super().__init__("Detective", self.action_one)

    def role_proper(self, other_object):
        if self.moves < 4:
            if other_object.get_last_role() == self.action_two:
                self.mode_gunder = 1
            if self.moves == 1:
                self.action = self.action_two
            else:
                self.action = self.action_one
            self.moves += 1
        elif self.mode_gunder == 0:
            self.mode_gunder = 2
            self.action = self.action_two
        elif self.mode_gunder == 1:
            self.action = other_object.get_last_role()

    def reset(self) -> str:
        self.mode_gunder = 0
        self.moves = 0
        self.action = self.action_one
        super().reset()


class Game(object):
    def __init__(self, matches=10) -> None:
        if matches < 0:
            matches = 10
        self.matches = matches
        self.registry = Counter()

    def game_mechanic(self, player1, player2) -> None:
        for _ in range(self.matches):
            player1.role_proper(player2)
            player2.role_proper(player1)
            player1.choose_action(player2)

        candies1 = player1.get_registry()
        candies2 = player2.get_registry()

        self.registry[player1.get_role()] += candies1
        self.registry[player2.get_role()] += candies2

        player1.reset()
        player2.reset()

    def get_registry(self) -> Counter:
        return self.registry

    def play_all_combinations(self) -> None:
        all_objects = [
            Cheater(),
            Cooperator(),
            Copycat(),
            Grudger(),
            Detective(),
            Rat(self.matches)]

        for i in range(len(all_objects)):
            for j in range(len(all_objects)):
                if i < j:
                    player1 = all_objects[i]
                    player2 = all_objects[j]
                    self.game_mechanic(player1, player2)

    def play_with_player(self, player) -> None:
        all_objects = [
            Cheater(),
            Cooperator(),
            Copycat(),
            Grudger(),
            Detective(),
            Rat(self.matches)]

        for other_player in all_objects:
            if player.get_role() != other_player.get_role():
                self.game_mechanic(player, other_player)

    def play(self, player1=None, player2=None) -> None:
        if player1 is None and player2 is None:
            self.play_all_combinations()
        elif player1 is None:
            self.play_with_player(player2)
        elif player2 is None:
            self.play_with_player(player1)
        else:
            self.game_mechanic(player1, player2)

    def top3(self) -> None:
        sorted_registry = sorted(
            self.registry.items(), key=lambda x: x[1], reverse=True)
        for player, candies in sorted_registry:
            print(f"{player} {candies}")

    def reset_registry(self) -> None:
        self.registry.clear()
