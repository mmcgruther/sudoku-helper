import basicsudoku
import basicsudoku.puzzles as puzzles
import basicsudoku.solvers as solvers

board = basicsudoku.SudokuBoard(puzzles.hardest[0])
print(board)
print("\n\n")
solvers.BasicSolver(board)
print(board)