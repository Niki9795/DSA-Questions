"""
Maze Problem using Backtracking
"""
class Maze():

    """
    Count the number of ways to reach the destination and return the list of paths

    V = Vertical
    H = Horizontal
    D = Diagonal 
    """
    def count(self, processedPath, row, col):
        result = []
        if row == 1 and col == 1:
            result.append(processedPath)
            return result
        
        if row > 1:
            result += self.count(processedPath + "V", row - 1, col)
        
        if col > 1:
            result += self.count(processedPath + "H", row, col - 1)

        if row > 1 and col > 1:
            result += self.count(processedPath + "D", row - 1, col - 1)

        return result
    
maze = Maze()
row = int(input("Enter the number of rows\n"))
col = int(input("Enter the number of columns\n"))
print(maze.count("", row, col))

""" 
Maze Problem with obstacles using Backtracking
"""
class Maze():

    def path(self, processedPath, maze, row, col):
        result = []

        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            result.append(processedPath)
            return result
        
        if maze[row][col] == False:
            return []
        
        if row < len(maze) - 1:
            result += self.path(processedPath + "D", maze, row + 1, col)

        if col < len(maze[0]) - 1:
            result += self.path(processedPath + "R", maze, row, col + 1)

        return result

maze = Maze()
board = [[True, True, True], 
         [True, False, True], 
         [True, True, True]]

print(maze.path("", board, 0, 0))