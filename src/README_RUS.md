## Эволюция доверия


* [Запуск](#запуск)
* [Персонажи](#персонажи)
* [класс Player](#класс-player)
    * [Атрибуты класса Player](#атрибуты-класса-player)
    * [Инициализация класса Player](#инициализация-класса-player)
    * [Методы класса Player](#методы-класса-player)
* [Роль](#роль)
* [Очки в игре](#очки-в-игре)
* [Класс Game](#класс-game)
    * [Инициализация класса Game](#инициализация-класса-game)
    * [Методы класса Game](#методы-класса-game)
* [Пример запуска](#пример-запуска)


В рамках данного проекта мне нужно было реализовать одну популярную игру [эволюция доверия](https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_%D0%B4%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D0%B5), которая отлично показывает [теорию игр](https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D0%B8%D0%B3%D1%80).

Игра представлена для работы в терминале.


## Запуск

Для запуска необходим будет скрипт, включающий в себя методы игры и python не ниже версии 3.7

## Персонажи

Каждая [роль](#роль) у меня представлена в виде отдельного класса, который наследуется от родительского класса [`Player`](#класс-player)

## Класс Player

```python
    class Player(object): ...
```


### Атрибуты класса Player

Атрибуты класса содержат две переменные:

```python
    action_one = "Cooperator"
    action_two = "Cheater"
```

Они отражают действия которые доступны персонажам - украсть или сотрудничать.


### Инициализация класса Player

Магический метод `__init__`, который вызывается при инициализации класса, принимает в себя - роль персонажа (в виде строки) и его [следующее действие](#атрибуты-класса). Также инициализирует пустой счетчик и последнюю роль.


### Методы класса Player

* `choise_action(other_object)`
    Выбор действия представлен методом `choise_action()`, 
    который принимает в качестве аргумента 
    класс другого персонажа и изменяет у своего 
    и другого класса количество очков
    ___
* `role_proper(other_object)`
    Метод который используется в производный классах,
    для изменения свой роли 
    (в зависимости от количество раундов, или ходов,
    которые были сделаны, и так далее)
    ___
* `add_registry(num:int)`
    Запоминает текущую роль и записывает ее в 
    поле `self.last_role`, прибавляет текущий счетчик на num
    ___
* `get_registry()`
    Возращает счетчик (можно изменить вне класса)
    ___
* `get_last_role()`
    Возращает последнюю роль
    ___
* `get_action()`
    Возращает действие, которое находитсья в переменной `self.action`
    ___
* `get_role()`
    Возращает текущую роль персонажа
    ___
* `reset()`
    Обнуляет счетчик, меняет последнюю [роль](#роль)


## Роль

Все роли полностью наследуют [класс Player](#класс-player)

*   Cheater
    ```python
    class Cheater(Player): ...
    ```
    Инициализирует сразу действие украсть. И все дальнейшие действия будут только украсть.
    ___
*   Cooperator
    ```python
    class Cooperator(Player): ...
    ```
    Инициализирует сразу действие  сотрудничать. Все дальнейшие действия - всегда будут сотрудничать.
    ___
*   Copycat
    ```python
    class Cooperator(Player): ...
    ```
    Начинает с сотрудничества, повторяет действие персонажа, сделанного в прошлый ход.
    ___
*   Grudger
    ```python
    class Grudger(Player): ...
    ```
    Начинает с сотрудничества, но если игрок хоть раз украл, навсегда изменяет свои действие на воровство
    ___
*   Detective
    ``` python
    clas Detective(Player): ...
    ```
    Начинает с сотрудничество, чередует сотрудничество и воровство до 5 хода, если кто-то за эти ходы хоть раз своровал, начинает подражать, повторять последние действия. Если никто за эти 4 хода ниразу не своровал - переключается на воровство.
    ___
*   Rat
    ```python
    class Rat(Player): ...
    ```
    Добавлен мной в качестве нечестной роли, он знает максимальное количество раундов (оно принимается при `__init__`), если это последний ход  - всегда завершающим действием будет украсть.


## Очки в игре

Действия:
* те, кто сотрудничает - получают свои же и надбавку +1
* те кто воруют, получают очки тех, кто сотрудничает и свое очко
* те кто воруют - ничего не получают

|роль1 / роль2|Cheater|Cooperator|
|----------|-------|----------|
|Cheater   |0/0|+3/-1|
|Cooperator|-1/+3|+2/+2|


## Класс Game

```python
class Game(object):...
```

Он нужен для запуска и настройки игры.


### Инициализация класса Game

При инициализации `def __init__(self, matches=10)` может принимает количество раундов, которые будут играть 2 игрока. По умоланию - 10. Содержит в себе счетчики `self.registry = Counter()` всех очков у персонажей.


### Методы класса Game

*   `game_mechanic(player1, player2)`
    Обязательно принимает в себе две [роли](#роль), любые на усмотрение.
    Он запускает игру между двумя персонажами и вносит их количество очков в общий счет, который храниться в `self.registry`
    ___
*   `get_registry()`
    Возращает счетчик, как тип данных [Counter](https://docs.python.org/3/library/collections.html)
    ___
*   `play_all_combinations()`
    Запуск игры между всеми комбинациями ролей персонажа.
    ___
*   `play_with_player(player)`
    Запуск игры персонажа против всех ролей персонажа
    ___
*  `play(player1=None, player2=None)`
    Для запуска игры по умолчанию - либо со всеми, лбио всех против друг друга, либо двух персонажей против друг друг
    ___
*   `top3()`
    Вывод топ 3 роли во время игры.
    ___
*   `reset_registry()`
    Для очистки счетчика


## Пример запуска

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