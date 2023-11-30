import matplotlib.pyplot as plt

# Given points (x, y, t)
points = [
            (15, -1, 0), (7, 11, -7), (20, -8, 9),
                (-16, -4, 13), (0, -11, 18), (19, -13, -8),
                    (16, 1, -14), (-14, -3, 10), (-7, 13, 1), (6, -10, 17)
                    ]

# Extract x, y, and t values
x_values, y_values, t_values = zip(*points)

# Create a scatter plot
plt.scatter(x_values, y_values)

# Annotate each point with its t value
for x, y, t in zip(x_values, y_values, t_values):
        plt.annotate(str(t), (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

        # Set axis labels
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')

        # Set plot title
        plt.title('Scatter Plot with Values')

        # Display the plot
        plt.show()

