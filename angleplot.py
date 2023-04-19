import numpy as np
import plotly.graph_objs as go

# Arm Lengths
l1 = 1.0 # length of the first arm segment
l2 = 0.8 # length of the second arm segment
l3 = 0.6 # length of the third arm segment
l4 = 0.4 # length of the fourth arm segment

# Generate data
t = np.linspace(-np.pi, np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# Calculate joint angles
theta1 = np.arctan2(y, x)
d = np.sqrt(x**2 + y**2)
D = (d**2 + (z-l1)**2 - l2**2 - l3**2 - l4**2) / (2*l2*l4)
theta4 = np.arctan2(-np.sqrt(1-D**2), D)
theta2_num = z - l1 + l4*np.sin(theta4)
theta2_den = d + l4*np.cos(theta4)
theta2 = np.arctan2(theta2_num, theta2_den) - np.arctan2(l3, l2)
theta3_num = (z - l1 - l2*np.sin(theta2)) / l4
theta3_den = np.cos(theta2)
theta3 = np.arctan2(theta3_num, theta3_den)

# Convert angles to degrees
theta1_deg = np.rad2deg(theta1)
theta2_deg = np.rad2deg(theta2)
theta3_deg = np.rad2deg(theta3)
theta4_deg = np.rad2deg(theta4)

# Create trace for 3D scatter plot
trace = go.Scatter3d(x=x, y=y, z=z, mode='markers')

# Add joint angles to the hover text
hover_text = []
for i in range(len(x)):
    hover_text.append('Theta1: {:.2f}<br>Theta2: {:.2f}<br>Theta3: {:.2f}<br>Theta4: {:.2f}'.format(
        theta1_deg[i], theta2_deg[i], theta3_deg[i], theta4_deg[i]))
trace.hovertext = hover_text

# Create layout for 3D plot
layout = go.Layout(title='Robotic Arm Path')

# Create figure for 3D plot
fig = go.Figure(data=[trace], layout=layout)

# Export data to HTML file
fig.write_html('arm_path.html')
