## The evolution of trust


* [Start](#start)
* [Characters](#characters)
* [Player class](#player-class)
    * [Attributes of the Player class](#attributes-of-the-player-class)
    * [Initializing the Player class](#initializing-the-player-class)
    * [Methods of the Player class](#methods-of-the-player-class)
* [Role](#role)
* [Points in the game](#points-in-the-game)
* [Game Class](#game-class)
    * [Initializing the Game class](#initializing-the-game-class)
    * [Methods of the Game class](#methods-of-the-game-class)
* [Launch example](#launch-example)


As part of this project, I needed to implement one popular game [evolution доверия](https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_%D0%B4%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D0%B5) which perfectly shows [game theory](https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D0%B8%D0%B3%D1%80).

The game is presented to work in the terminal

## Start

To run, you will need a script that includes game methods and python at least version 3.7

## Characters

I have each [role](#role) represented as a separate class that inherits from the parent class [`Player`](#player-class)

## Player class

```python
    class Player(object): ...
```

### Attributes of the Player class

Class attributes contain two variables:

```python
    action_one = "Cooperator"
    action_two = "Cheater"
```

They reflect the actions that are available to the characters - to steal or cooperate.


### Initializing the Player class

The magic method `__init__`, which is called when initializing the class, takes on the role of a character (in the form of a string) and its [next action](#attributes of the class). Also initializes the empty counters of the last role.


### Methods of the Player class

*   `choice_action(other_object)`
    The choice of an action is represented by the `choice_action()` method,
    which takes as an argument 
    the class of another character and changes its own 
    and the number of points of another class
    ___
*  `role_proper(other_object)`
    Method that is used in derived classes,
    to change your role 
    (depending on the number of rounds, or moves,
    which were made, and so on)
    ___
* `add_registry(num:int)`
    Remembers the current role and writes it to 
    the `self.last_role` field adds the current counter to num
    ___
* `get_registry()`
    Returns a counter (can be changed outside the class)
    ___
*  `get_lost_role()`
    Returns the last role
    ___
*  `get_action()`
    Returns the action that is in the `self.action` variable
    ___
*  `get_role()`
    Returns the current character role
    ___
*  `reset()`
    Resets the counter, changes the last [role](#role)


## Role

All roles completely inherit the [Player class](#player class)

*   Cheater
    ```python
    class Cheater(Player): ...
    ```
    Initializes the steal action immediately. And all further actions will only be stealing.
    ___
*   Cooperator
    ```python
    class Cooperator(Player): ...
    ```
    Initializes the cooperate action immediately. All further actions will always cooperate.
    ___
*   Copycat
    ```python
    class Cooperator(Player): ...
    ```
    Starts with cooperation, repeats the action of the character made in the last turn.
    ___
*   Grudger
    ```python
    class Grudger(Player): ...
    ```
    He starts with cooperation, but if the player has stolen at least once, he forever changes his actions to theft
    ___
*   Detective
    ``` python
    clas Detective(Player): ...
    ```
    He starts with cooperation, alternates cooperation and theft up to turn 5, if someone has stolen at least once during these moves, he begins to imitate, repeat the last actions. If no one has stolen anything during these 4 moves, they switch to stealing.
    ___
*   Rat
    ```python
    class Rat(Player): ...
    ```
    Added by me as an unfair role, he knows the maximum number of rounds (it is accepted at `__init__`), if this is the last move, the final action will always be to steal.

## Points in the game

Actions:
* those who cooperate receive their own and a +1 bonus
* those who steal get points from those who cooperate and their point
* those who steal get nothing

|rol1 / rol2|Cheater|Cooperator|
|----------|-------|----------|
|Cheater   |0/0|+3/-1|
|Cooperator|-1/+3|+2/+2|


## Game Class

```python
class Game(object):...
```

It is needed to launch and configure the game.


### Initializing the Game class

When initializing `def __init__(self, matches=10)` can accepts the number of rounds that 2 players will play. By request - 10. It contains the counters `self.registry = Counter()` of all the points of the characters.


### Methods of the Game class

* `game_mechanic(player1, player2)`
Necessarily accepts two [roles](#role), any at your discretion.
    He starts a game between two characters and adds their number of points to the total score, which is stored in the `self.registry`
    ___
*   `get_registry()`
    Returns the counter as the Counter data [type](https://docs.python.org/3/library/collections.html )
    ___
*   `play_all_combinations()`
    Starts the game between all combinations of character roles.
    ___
*   `play_with_player(player)`
    Running a character game against all character roles
    ___
*  `play(player1=None, player2=None)`
    To start the game by default - either with everyone, all against each other, or two characters against each other
    ___
* `top3()`
    Displays the top 3 roles during the game.
    ___
* `reset_registry()`
    To clear the counter


## Launch example

```bash
user@pc src % python3.11 main.py
```

`main.py`
```python
from morality import *


def main():
    game = Game()
    game.play(player1=Cheater(), player2=Cooperator())
    game.top3()


if __name__ == "__main__":
    main()
```
