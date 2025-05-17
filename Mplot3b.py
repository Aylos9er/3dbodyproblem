import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# --- Simulation Parameters ---
G = 1.0  # Gravitational constant
DT = 0.001  # Time step for simulation
N_STEPS_PER_FRAME = 10 # Number of simulation steps per animation frame for smoother physics
TRAIL_LENGTH = 300    # Max number of points in a trail (reduced for Matplotlib performance)

# --- Body Initial Conditions ---
# Masses
m1 = 10.0
m2 = 10.0
m3 = 10.0

# Initial positions (x, y, z)
pos1_init = np.array([-1.0, 0.0, 0.0])
pos2_init = np.array([1.0, 0.0, 0.0])
pos3_init = np.array([0.0, 1.5, 0.0]) # Slightly offset to break perfect symmetry

# Initial velocities (vx, vy, vz)
vel1_init = np.array([0.0, 0.5, 0.0])
vel2_init = np.array([0.0, -0.5, 0.0])
vel3_init = np.array([-0.75, 0.0, 0.0])


class Body:
    def __init__(self, mass, pos_init, vel_init, color_str, marker_size_base=50, radius_scale=0.05):
        self.mass = mass
        self.pos = np.array(pos_init, dtype=float)
        self.vel = np.array(vel_init, dtype=float)
        self.color_str = color_str # Matplotlib color string
        # Visual marker size scaled by mass for scatter plot
        self.marker_size = marker_size_base * (mass**0.33) * radius_scale 
        self.trail = [] # List to store trail points (collections.deque could be more efficient)

    def update_trail(self):
        self.trail.append(self.pos.copy())
        if len(self.trail) > TRAIL_LENGTH:
            self.trail.pop(0)

# --- Physics Calculation (remains the same) ---
def calculate_forces(bodies_list):
    num_bodies = len(bodies_list)
    forces = [np.zeros(3) for _ in range(num_bodies)]
    for i in range(num_bodies):
        for j in range(i + 1, num_bodies):
            body_i = bodies_list[i]
            body_j = bodies_list[j]

            delta_pos = body_j.pos - body_i.pos
            distance_sq = np.sum(delta_pos**2)
            
            # Add a small softening factor to prevent division by zero or extreme forces
            # This is a common technique in N-body simulations.
            softening_factor_sq = 0.01 # square of softening length
            distance_sq_softened = distance_sq + softening_factor_sq
            distance = np.sqrt(distance_sq_softened)

            if distance < 0.001: # Effectively zero distance, should not happen with softening
                force_magnitude = 0
            else:
                force_magnitude = (G * body_i.mass * body_j.mass) / distance_sq_softened
            
            force_vector = force_magnitude * (delta_pos / distance) # delta_pos is already (pos_j - pos_i)
            
            forces[i] += force_vector
            forces[j] -= force_vector # Newton's third law
    return forces

def update_physics(bodies_list, dt_sim):
    forces = calculate_forces(bodies_list)
    for i, body in enumerate(bodies_list):
        acceleration = forces[i] / body.mass
        body.vel += acceleration * dt_sim
        body.pos += body.vel * dt_sim

# --- Matplotlib Scene Setup ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor((0.05, 0.05, 0.1)) # Dark blue background

# Create bodies
bodies = [
    Body(m1, pos1_init, vel1_init, color_str='orange', radius_scale=0.5),
    Body(m2, pos2_init, vel2_init, color_str='skyblue', radius_scale=0.5),
    Body(m3, pos3_init, vel3_init, color_str='lightgrey', radius_scale=0.4)
]

# Matplotlib plot objects for bodies and trails
# We will initialize these as empty and update them in the animation
body_plots = [ax.scatter([], [], [], s=body.marker_size, color=body.color_str, depthshade=True) for body in bodies]
trail_plots = [ax.plot([], [], [], color=body.color_str, linewidth=1.0, alpha=0.7)[0] for body in bodies]


# Create Particle Dust (static)
N_DUST_PARTICLES = 2000 # Reduced for Matplotlib performance
dust_positions = (np.random.rand(N_DUST_PARTICLES, 3) - 0.5) * 30 # Spread over a cube
ax.scatter(dust_positions[:, 0], dust_positions[:, 1], dust_positions[:, 2],
           s=0.5, color='grey', alpha=0.2, marker='.')

# Set plot limits (adjust as needed based on simulation dynamics)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3-Body Simulation (Matplotlib)")

# --- Animation Function ---
def animate(frame):
    # Update physics
    for _ in range(N_STEPS_PER_FRAME):
        update_physics(bodies, DT)

    # Update plot elements
    for i, body in enumerate(bodies):
        # Update body position (scatter plot)
        # For scatter, we update the '_offsets3d' private member.
        # Note: This is a bit of a hack for scatter plots. A more robust way might involve
        # clearing and re-plotting, or using a single scatter plot for all bodies and updating its data.
        # For simplicity with individual styling, we update each scatter plot.
        body_plots[i]._offsets3d = ([body.pos[0]], [body.pos[1]], [body.pos[2]])
        
        # Update trail
        body.update_trail()
        if len(body.trail) > 1:
            trail_arr = np.array(body.trail)
            trail_plots[i].set_data(trail_arr[:, 0], trail_arr[:, 1]) # For 2D lines
            trail_plots[i].set_3d_properties(trail_arr[:, 2])      # For 3D lines
    
    # Dynamically adjust plot limits if bodies go too far
    # This can be computationally intensive and make the view jumpy
    # For now, we'll use fixed limits set earlier, but this is where you'd add auto-scaling
    # current_lims_x = list(ax.get_xlim())
    # for body in bodies:
    #     current_lims_x[0] = min(current_lims_x[0], body.pos[0] - 1)
    #     current_lims_x[1] = max(current_lims_x[1], body.pos[0] + 1)
    # ax.set_xlim(current_lims_x)
    # (repeat for Y and Z)


    # Return a list of artists that have been modified
    return body_plots + trail_plots

# --- Initial View and Start Animation ---
ax.view_init(elev=30., azim=30) # Set initial camera angle

print("Starting Matplotlib 3-Body Simulation...")
print("This might take a moment to initialize the animation window.")
print("Animation will run for a fixed number of frames (200).")

# Create animation
# interval is delay between frames in milliseconds
# frames is the number of frames to run; set to None for indefinite (but can be slow to stop)
ani = animation.FuncAnimation(fig, animate, frames=400, interval=30, blit=False)
# blit=True can improve performance but can be tricky with 3D plots and changing artists.
# Setting blit=False is often more robust for 3D.

plt.show()

print("Simulation finished or window closed.")
