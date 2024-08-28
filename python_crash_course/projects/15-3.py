import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep makin new walks, as long as the prograam is active.
while True:

    # Make random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points int the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.plot(0,0, c='green', edgecolors='none', s=100)
    ax.plot(rw.x_values[-1], rw.y_values[-1], 
               c='red', edgecolors='none', s=100)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break