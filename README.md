# Sudoku Solver with Answer Set Programming

Answer Set Programming (ASP) is a form of declarative programming 
oriented to NP-problems. You can check about it in the Wikipedia  article (
https://en.wikipedia.org/wiki/Answer_set_programming
). In this simple project we are using a clingo, an ASP system to ground (gringo) and solve (clasp) logic programs.
In this project I have formulated the Sudoku as a logic program. That way, I can apply ASP techniques to solve it.

You can check the original clingo code [here](original_clingo_code), where you will see the problem definition
(the definition of the Sudoku problem through ASP) and a problem instance (just a single instance of a Sudoku puzzle, which works as an example)

To check ASP in action, simply execute [main](main.py) module. It will
generate a 9x9 Sudoku using Pygame so you can solve it with a single click.
