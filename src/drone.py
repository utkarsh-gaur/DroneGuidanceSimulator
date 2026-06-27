"""
drone.py

Defines the Drone class.

Responsibilities:
- Store the drone state (position and velocity)
- Update the state using simple kinematic equations
- Provide access to the current state

Author: Utkarsh Gaur
Project: Drone Guidance and Navigation Simulator
"""


class Drone:
    def __init__(self, x=0.0, y=0.0, vx=0.0, vy=0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, ax, ay, dt):
        """
        Update the drone state using Euler integration.
        """
        self.vx += ax * dt
        self.vy += ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

    def get_state(self):
        """
        Return the current state of the drone.
        """
        return {
            "x": self.x,
            "y": self.y,
            "vx": self.vx,
            "vy": self.vy,
        }

    def reset(self):
        """
        Reset the drone to the origin with zero velocity.
        """
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0