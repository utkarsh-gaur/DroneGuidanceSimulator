from drone import Drone
import matplotlib.pyplot as plt

drone = Drone()

dt = 0.01          # seconds
simulation_time = 10  # seconds

ax = 1.0           # m/s²
ay = 0.0           # m/s²

steps = int(simulation_time / dt)

x_history = []
y_history = []

for _ in range(steps):

    drone.update(ax, ay, dt)

    state = drone.get_state()

    x_history.append(state["x"])
    y_history.append(state["y"])


plt.figure(figsize=(8, 6))

plt.plot(x_history, y_history, label="Drone Path")

plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Drone Trajectory")

plt.grid(True)
plt.axis("equal")
plt.legend()

plt.show()

print(drone.get_state())