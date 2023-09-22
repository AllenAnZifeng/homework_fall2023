
Command for running the behavioral cloning agent on the Ant-v4 environment.
```bash
python --expert_policy_file ..\policies\experts\Ant.pkl
--env_name Ant-v4
--exp_name bc_ant
--n_iter 1
--expert_data ..\expert_data\expert_data_Ant-v4.pkl
--video_log_freq -1
```

Command for running the behavioral cloning agent on the Hopper-v4 environment.
```bash
python --expert_policy_file ..\policies\experts\Hopper.pkl
--env_name Hopper-v4
--exp_name bc_hopper
--n_iter 1
--expert_data ..\expert_data\expert_data_Hopper-v4.pkl
--video_log_freq -1
```

Command for running the dagger on the Ant-v4 environment.
```bash
python --expert_policy_file ..\policies\experts\Ant.pkl
--env_name Ant-v4
--exp_name bc_ant_dagger
--n_iter 10
--do_dagger
--expert_data ..\expert_data\expert_data_Ant-v4.pkl
--video_log_freq -1
```

Command for running the dagger on the Hopper-v4 environment.
```bash
python --expert_policy_file ..\policies\experts\Hopper.pkl
--env_name Hopper-v4
--exp_name bc_hopper_dagger
--n_iter 10
--do_dagger
--expert_data ..\expert_data\expert_data_Hopper-v4.pkl
--video_log_freq -1
```


Python code for generating figure 1.
```python
import matplotlib.pyplot as plt

# Data
learning_rates = [5e-0, 5e-1, 5e-2, 5e-3, 5e-4, 5e-5]
eval_average_returns = [
    -6.7248335103847804e+22,
    -7997854.0,
    252.25587463378906,
    4588.30078125,
    -353.7942199707031,
    -355.70086669921875
]

# Adjusting the scale for the y-axis to better visualize the differences among learning rates
plt.figure(figsize=(10, 6))
plt.semilogx(learning_rates, eval_average_returns, marker='o')
plt.title('Performance of Behavioral Cloning Agent vs. Learning Rate')
plt.xlabel('Learning Rate')
plt.ylabel('Evaluation Average Return')
plt.grid(True, which="both", ls="--", c='0.7')
plt.ylim(-10000, 5000)  # Adjusted scale for y-axis
plt.tight_layout()
plt.show()
```

Python code for generating figure 2.
```python
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
```

Python code for generating figure 3.
```python
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
```