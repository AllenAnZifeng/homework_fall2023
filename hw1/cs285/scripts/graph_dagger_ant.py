import matplotlib.pyplot as plt

# Extracted data from the provided information
iterations = list(range(10))  # 10 iterations from 0 to 9
eval_average_return = [
    4608.9072265625, 4659.16796875, 4620.01416015625, 4703.55078125,
    4639.9404296875, 4668.5576171875, 4681.94921875, 4743.7607421875,
    4732.9580078125, 4693.35693359375
]
eval_std_return = [
    60.12022018432617, 65.70421600341797, 67.31063079833984, 119.31056213378906,
    30.863231658935547, 124.18997955322266, 80.97986602783203, 74.4588394165039,
    103.07255554199219, 97.17868041992188
]
initial_data_collection_average_return = 4681.891673935816  # Performance of the expert policy

# The performance of the behavioral cloning agent can be taken as the mean return at Iteration 0
behavioral_cloning_performance = eval_average_return[0]


# Set up the figure
plt.figure(figsize=(10, 6))

# Plot the learning curve with error bars
plt.errorbar(iterations, eval_average_return, yerr=eval_std_return, fmt='-o', capsize=5, label='DAgger Policy')

# Plot the performance of the expert policy and the behavioral cloning agent as horizontal lines
plt.axhline(y=initial_data_collection_average_return, color='r', linestyle='--', label='Expert Policy')
plt.axhline(y=behavioral_cloning_performance, color='g', linestyle='--', label='Behavioral Cloning Agent')

# Setting title and labels
plt.title("DAgger Learning Curve")
plt.xlabel("Number of DAgger Iterations")
plt.ylabel("Policy’s Mean Return")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Display the plot
plt.show()
