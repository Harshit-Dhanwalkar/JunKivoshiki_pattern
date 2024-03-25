import numpy as np
import matplotlib.pyplot as plt

# Create a 10x10 grid
X, Y = np.meshgrid(np.arange(0, 10, 1), np.arange(0, 10, 1))

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

# Display the plot
plt.show()