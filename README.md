# Xiangqi

This program is an implementation of Xiangqi, also known as Chinese chess, which is a two player strategy board game.  
The player can create an instance of the game, make moves, and determine the winner in the terminal.  
Example:   

`game = XiangqiGame()`  
`move_result = game.make_move('c1', 'e3')`  
`black_in_check = game.is_in_check('black')`  
`game.make_move('e7', 'e6')`  
`state = game.get_game_state()`  

Read specific rules about the game at https://en.wikipedia.org/wiki/Xiangqi.

## Notes
This is a portfolio project for CS162 - Introduction to CS II at Oregon State University as an introduction to objected-oriented programming.
