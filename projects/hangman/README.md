# H A N G M A N
This project aims to implement the classic "Hangman" game. 

## Requirements
### Version 1 
* The player has 10 oportunities to make a wrong guess before he's "Hanged".
* The game will ask the player if he/she wants to play again at the end.
* The game will choose randomly from a list of 50 words the one to play with.
* The game will show each game play on a clear screen.
* The game must track the right and wrong guesses.
* All guesses must only be a letter (not case sensitive). Wrong types or repeated guesses are disregarded and don't count as an attempt.

## Game Play
### Version 1

* The game chooses a word (i.e. monkey)
* The player is presented with dashes "_" indicating each missing letter
* If the letter guessed doesn't exist a new piece of the Hangman is drawn.
* If the letter guessed exists the letter is replaced everywhere it exists in the word.
* If the word is guessed before the attempt run out the player wins the game.
* If the word is not guessed by the time no attempts are left the player looses.
* At the end of the game the game asks the use if he wants to play again.

### ASCII Art
#### Bad guess 1
```





===============+
```
#### Bad guess 2
```
               +
               |
               |
               |
               |
===============+
```
#### Bad guess 3
```
       +=======+
               |
               |
               |
               |
===============+
```
#### Bad guess 4
```
       +=======+
       |       |
               |
               |
               |
===============+
```
#### Bad guess 5
```
       +=======+
       |       |
       O       |
               |
               |
===============+
```
#### Bad guess 6
```
       +=======+
       |       |
       O       |
       |       |
               |
===============+
```
#### Bad guess 7
```
       +=======+
       |       |
       O       |
      /|       |
               |
===============+
```
#### Bad guess 8
```
       +=======+
       |       |
       O       |
      /|\      |
               |
===============+
```
#### Bad guess 9
```
       +=======+
       |       |
       O       |
      /|\      |
      /        |
===============+
```
#### Bad guess 10
```
       +=======+
       |       |
       O       |
      /|\      |
      / \      |
===============+
```


