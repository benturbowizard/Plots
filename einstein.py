import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, Frame, BOTH

save_path = "einstein_plot.png"

# Function to calculate relativistic rotation curve based on Schwarzschild metric
def relativistic_rotation_curve(radius, mass):
    G = 6.674 * 10**(-11)  # Gravitational constant
    c = 299792458  # Speed of light
    return np.sqrt(G * mass / radius) * np.sqrt(1 + (3 * G * mass) / (radius * c**2))

# Function to create and display the plot
def display_plot(radius, rotation_curve_values, title):
    fig, ax = plt.subplots()
    ax.plot(radius, rotation_curve_values, label="Relativistic Rotation Curve")
    ax.set_xlabel('Radius (m)')
    ax.set_ylabel('Rotation Curve (m/s)')
    ax.set_title(title)
    ax.legend()

    plt.savefig(save_path)
    plt.show()


# Main function
def main():
    radius = np.linspace(1, 10, 1000)  # Adjust range and step as needed
    mass = 1.5 * 10**41  # Adjust mass as needed

    # Calculate relativistic rotation curve
    relativistic_rotation_curve_values = relativistic_rotation_curve(radius, mass)

    # Display the relativistic rotation curve plot
    display_plot(radius, relativistic_rotation_curve_values, "Relativistic Galaxy Rotation Curve")

if __name__ == "__main__":
    main()
