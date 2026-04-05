import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000                  # Sampling frequency
t = np.arange(0, 1, 1/fs) # Time vector

# Input signal (with phase offset)
f_in = 5
phase_offset = np.pi / 4
input_signal = np.sin(2 * np.pi * f_in * t + phase_offset)

# PLL parameters
Kp = 0.1   # Proportional gain (loop filter)
Ki = 0.01  # Integral gain

# Initialize variables
phase = 0
freq = 5
integrator = 0

output_signal = []
phase_error_list = []

# DPLL loop
for i in range(len(t)):
    # NCO output
    vco = np.sin(2 * np.pi * freq * t[i] + phase)
    
    # Phase detector (multiplier)
    phase_error = input_signal[i] * vco
    
    # Loop filter (PI controller)
    integrator += Ki * phase_error
    control = Kp * phase_error + integrator
    
    # Update phase
    phase += control
    
    output_signal.append(vco)
    phase_error_list.append(phase_error)

# Convert to numpy arrays
output_signal = np.array(output_signal)
phase_error_list = np.array(phase_error_list)

# Plot results
plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.plot(t, input_signal)
plt.title("Input Signal")

plt.subplot(3,1,2)
plt.plot(t, output_signal)
plt.title("PLL Output Signal")

plt.subplot(3,1,3)
plt.plot(t, phase_error_list)
plt.title("Phase Error")

plt.tight_layout()
plt.savefig("results.png")
plt.show()