import numpy as np
import matplotlib.pyplot as plt

save_path = "exponential_decay_plot.png"

# Function to calculate relativistic rotation curve based on Schwarzschild metric
def relativistic_rotation_curve(radius, mass):
    G = 6.674 * 10**(-11)  # Gravitational constant
    c = 299792458  # Speed of light
    return np.sqrt(G * mass / radius) * np.sqrt(1 + (3 * G * mass) / (radius * c**2))

# Function to calculate the mass based on exponential decay
def decayed_mass(initial_mass, k_constant, time):
    return initial_mass * np.exp(-k_constant * time)

# Function to calculate the relative radius between masses based on shrinking geometry
def relative_radius(initial_radius, k_constant, time):
    return initial_radius * np.exp(k_constant * time)

# Function to create and display the plot
def display_plot(radius, rotation_curve_values, title):
    fig, ax = plt.subplots()
    ax.plot(radius, rotation_curve_values, label="Force over time")
    ax.set_xlabel('radius (m)')
    ax.set_ylabel('Rotation Curve (m/s)')
    ax.set_title(title)
    ax.legend()

    plt.savefig(save_path)
    plt.show()

# Main function
def main():
    radius = np.linspace(1, 10, 10000000)  # Adjust range and step as needed
    initial_mass = 1.5 * 10**41  # Adjust initial mass as needed
    initial_radius = 1.0  # Adjust initial radius as needed

    k_constant = 1e1  # Adjust decay constant as needed

    time = np.linspace(0, 10, 10000000)  # Adjust time range and step as needed

    # Calculate mass based on exponential decay
    mass_values = decayed_mass(initial_mass, k_constant, time)

    # Calculate radius based on expanding geometry
    radius_values = relative_radius(initial_radius, k_constant, time)

    # Calculate relativistic rotation curve
    relativistic_rotation_curve_values = relativistic_rotation_curve(radius_values, mass_values)

    # Display the relativistic rotation curve plot
    display_plot(radius_values, relativistic_rotation_curve_values, "Mass Distance Relativistic Galaxy Rotation Curve")



if __name__ == "__main__":
    main()
