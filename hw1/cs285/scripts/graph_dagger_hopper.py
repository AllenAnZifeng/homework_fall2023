import matplotlib.pyplot as plt

# Extracted data from the provided information
eval_average_return_2 = [
    859.4658203125, 2460.3857421875, 2757.228515625, 2246.484130859375,
    3722.78662109375, 3331.9482421875, 3709.797607421875, 3722.21337890625,
    3718.906982421875, 3716.93701171875
]
eval_std_return_2 = [
    201.13388061523438, 661.7655639648438, 791.1864624023438, 1140.1722412109375,
    2.25459361076355, 899.5781860351562, 4.663782596588135, 2.7733983993530273,
    4.656719207763672, 3.8774051666259766
]
initial_data_collection_average_return_2 = 3717.5129936182307  # Performance of the expert policy

# The performance of the behavioral cloning agent can be taken as the mean return at Iteration 0
behavioral_cloning_performance_2 = eval_average_return_2[0]

iterations = list(range(10))  # 10 iterations from 0 to 9

# Set up the figure
plt.figure(figsize=(10, 6))

# Plot the learning curve with error bars
plt.errorbar(iterations, eval_average_return_2, yerr=eval_std_return_2, fmt='-o', capsize=5, label='DAgger Policy')

# Plot the performance of the expert policy and the behavioral cloning agent as horizontal lines
plt.axhline(y=initial_data_collection_average_return_2, color='r', linestyle='--', label='Expert Policy')
plt.axhline(y=behavioral_cloning_performance_2, color='g', linestyle='--', label='Behavioral Cloning Agent')

# Setting title and labels
plt.title("DAgger Learning Curve (2nd Dataset)")
plt.xlabel("Number of DAgger Iterations")
plt.ylabel("Policy’s Mean Return")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Display the plot
plt.show()
