# import necessary libraries
import matplotlib.pyplot as plt

# these are dummy values, replace these lists with your actual data

returns_5_1 = []  # Fill this list with your Eval_AverageReturn for each iteration
returns_5_2 = []
returns_5_3 = []
returns_5_4 = []
returns_5_5 = []

env_steps_5_1 = []
env_steps_5_2 = []
env_steps_5_3 = []
env_steps_5_4 = []
env_steps_5_5 = []


for line in open('5-1.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_5_1.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_5_1.append(score)

for line in open('5-2.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_5_2.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_5_2.append(score)


for line in open('5-3.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_5_3.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_5_3.append(score)


for line in open('5-4.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_5_4.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_5_4.append(score)


for line in open('5-5.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_5_5.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_5_5.append(score)


plt.figure(figsize=(12,7))

# Plotting with adjusted linewidth
plt.plot(env_steps_5_1, returns_5_1, label='lambda = 0', color='blue', alpha=0.5, linewidth=2)
plt.plot(env_steps_5_2, returns_5_2, label='lambda = 0.95', color='red', alpha=0.5, linewidth=2)
plt.plot(env_steps_5_3, returns_5_3, label='lambda = 0.98', color='orange', alpha=0.5, linewidth=2)
plt.plot(env_steps_5_4, returns_5_4, label='lambda = 0.99', color='green', alpha=0.5, linewidth=2)
plt.plot(env_steps_5_5, returns_5_5, label='lambda = 1', color='black', alpha=0.5, linewidth=2)

# Adjusting font sizes and adding grid
plt.xlabel('Env Steps', fontsize=14)
plt.ylabel('Eval_AverageReturn', fontsize=14)
plt.title('Eval_AverageReturn vs Env Steps for LunarLander-v2 with different lambda values', fontsize=16)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Ensuring the layout is not cramped
plt.tight_layout()

plt.show()
