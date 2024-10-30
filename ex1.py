import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.81  # gravitational acceleration (m/s^2)
L = 1.0   # length of the pendulum (m)
M = 5.0   # mass of the cart (kg)
m = 1.0   # mass of the pendulum bob (kg)
u = 2.0   # control input (force applied to the cart, dynamically adjustable)

# Grid setup for stream plot
theta_stream = np.linspace(-np.pi, np.pi, 100)
omega_stream = np.linspace(-3, 3, 100)
Theta_stream, Omega_stream = np.meshgrid(theta_stream, omega_stream)

# Grid setup for vector field (quiver)
theta_quiver = np.linspace(-np.pi, np.pi, 20)  # Sparsity in vector field
omega_quiver = np.linspace(-3, 3, 20)
Theta_quiver, Omega_quiver = np.meshgrid(theta_quiver, omega_quiver)

# TODO: Complete the implementation of the inverted_pendulum_dynamics function
# It should calculate the derivatives of theta and omega for the inverted pendulum system
def inverted_pendulum_dynamics(theta, omega):
    """
    Calculate the dynamics of the inverted pendulum system.
    
    Parameters:
    theta (float or ndarray): Pendulum angle from the vertical (radians)
    omega (float or ndarray): Angular velocity of the pendulum (radians/s)
    
    Returns:
    tuple: Derivatives (dtheta_dt, domega_dt)
    """
    # Write your code here
    raise NotImplementedError("Function implementation is pending.")

# Test the dynamics function if available
try:
    dTheta_dt_quiver, dOmega_dt_quiver = inverted_pendulum_dynamics(Theta_quiver, Omega_quiver)
    dTheta_dt_stream, dOmega_dt_stream = inverted_pendulum_dynamics(Theta_stream, Omega_stream)
    can_plot = True
except NotImplementedError:
    print("Dynamics function is not implemented yet.")
    can_plot = False

# Plotting the phase portrait if dynamics are defined
if can_plot:
    plt.figure(figsize=(10, 8))
    # Stream plot
    plt.streamplot(Theta_stream, Omega_stream, dTheta_dt_stream, dOmega_dt_stream, color='lightblue')
    # Quiver plot
    plt.quiver(Theta_quiver, Omega_quiver, dTheta_dt_quiver, dOmega_dt_quiver, color='blue')
    plt.xlabel('Angle (θ) [rad]')
    plt.ylabel('Angular Velocity (ω) [rad/s]')
    plt.title('Phase Portrait of an Inverted Pendulum on a Cart')
    plt.grid(True)
    plt.xlim(-np.pi, np.pi)
    plt.ylim