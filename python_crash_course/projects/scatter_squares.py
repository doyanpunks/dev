import matplotlib.pyplot as plt
plt.style.available

#x_values = range(1, 5001)
x_values = [1,2,3]
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.scatter(x_values, y_values, color='blue', s=100)
#ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
#ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style='plain')

# Set size of tick labels.
#ax.tick_params(labelsize=14)
plt.show()