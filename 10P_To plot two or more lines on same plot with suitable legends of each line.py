import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 4, 9, 16]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Line Plot")
plt.legend()
plt.show()
