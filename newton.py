import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, Frame, BOTH

save_path = "newton_plot.png"

# Function to calculate rotation curve based on Newton's gravity
def rotation_curve(radius, mass):
    G = 6.674 * 10**(-11)  # Gravitational constant
    return np.sqrt(G * mass / radius)

# Function to create and display the plot
def display_plot(radius, rotation_curve_values):
    fig, ax = plt.subplots()
    ax.plot(radius, rotation_curve_values, label="Rotation Curve")
    ax.set_xlabel('Radius (m)')
    ax.set_ylabel('Rotation Curve (m/s)')
    ax.set_title('Newton Galaxy Rotation Curve')
    ax.legend()

    plt.savefig(save_path)
    plt.show()


# Main function
def main():
    radius = np.linspace(1, 10, 1000)  # Adjust range and step as needed
    mass = 1.5 * 10**41  # Adjust mass as needed

    rotation_curve_values = rotation_curve(radius, mass)

    display_plot(radius, rotation_curve_values)

if __name__ == "__main__":
    main()
