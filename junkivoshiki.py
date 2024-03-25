import numpy as np
import matplotlib.pyplot as plt

# Create a 10x10 grid
X, Y = np.meshgrid(np.arange(0, 50, 1), np.arange(0, 50, 1))

# Define the direction of the vectors
U = np.zeros_like(X)
V = np.ones_like(Y)

# Create the plot
Q = plt.quiver(X, Y, U, V)

def update_quiver(event):
    # Get the cursor coordinates
    x, y = event.xdata, event.ydata
    
    # Calculate the direction of the vectors based on cursor coordinates
    U = x - X
    V = y - Y
    
    # Update the quiver data
    Q.set_UVC(U, V)
    
    # Redraw the plot
    plt.draw()

# Connect the update_quiver function to the mouse movement event
plt.gcf().canvas.mpl_connect('motion_notify_event', update_quiver)
# plt.grid()
# Display the plot
plt.show()

def save_image(event):
    if event.key == 's':
        plt.savefig('./JunKivoshiki_pattern/junkivoshiki.png')

# Connect the save_image function to the key press event
plt.gcf().canvas.mpl_connect('key_press_event', save_image)


############################################################
## Solve the JunKivoshiki pattern
def solve_junkivoshiki(grid):
    # Check if the grid is already solved
    def is_solved(grid):
        # Check if the grid is solved
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    return False
        return True

    if is_solved(grid):
        return True

    # Find the next empty cell
    def find_empty_cell(grid):
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    return row, col
        return None

    row, col = find_empty_cell(grid)

    # Try different numbers in the empty cell
    def is_valid_move(grid, row, col, num):
        # Check if the number already exists in the same row
        for i in range(len(grid[row])):
            if grid[row][i] == num:
                return False

        # Check if the number already exists in the same column
        for i in range(len(grid)):
            if grid[i][col] == num:
                return False

        # Check if the number already exists in the same 2x2 subgrid
        subgrid_row = row // 2
        subgrid_col = col // 2
        for i in range(subgrid_row * 2, subgrid_row * 2 + 2):
            for j in range(subgrid_col * 2, subgrid_col * 2 + 2):
                if grid[i][j] == num:
                    return False

        return True

    for num in range(1, len(grid) + 1):
        if is_valid_move(grid, row, col, num):
            # Place the number in the empty cell
            grid[row][col] = num

            # Recursively solve the rest of the grid
            if solve_junkivoshiki(grid):
                return True

            # If the current number doesn't lead to a solution, backtrack
            grid[row][col] = 0

    # If no number can be placed in the empty cell, the puzzle is unsolvable
    return False

# Example usage
def print_grid(grid):
    # Print the grid
    for row in grid:
        print(row)

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

if solve_junkivoshiki(grid):
    print("Solution found:")
    print_grid(grid)
else:
    print("No solution exists.")