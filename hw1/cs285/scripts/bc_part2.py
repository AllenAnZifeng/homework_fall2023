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

