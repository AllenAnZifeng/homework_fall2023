# import necessary libraries
import matplotlib.pyplot as plt

# these are dummy values, replace these lists with your actual data

returns_3_1 = []  # Fill this list with your Eval_AverageReturn for each iteration
returns_3_2 = []

env_steps_3_1 = []
env_steps_3_2 = []

#
# for line in open('4-1data.txt'):  # adjust with your log file
#
#
#     if "Train_EnvstepsSoFar" in line:
#         parts = line.split()
#         step = float(parts[-1])
#         env_steps_3_1.append(step)
#
#     if "Eval_AverageReturn" in line:
#         parts = line.split()
#
#         score = float(parts[-1])
#         returns_3_1.append(score)
#
#
#
#
#
for line in open('4-2data.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_3_2.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_3_2.append(score)

# for line in open('4-2mdata.txt'):  # adjust with your log file
#
#     if "Eval_AverageReturn" in line:
#         parts = line.split()
#         step = float(parts[-1])
#         env_steps_3_2.append(step)
#
#     if "Baseline Loss" in line:
#         parts = line.split()
#
#         score = float(parts[-1])
#         returns_3_2.append(score)
#


plt.figure(figsize=(10,6))
# plt.plot(env_steps_3_1, returns_3_1,label='HalfCheetah', color='blue', alpha=0.8)
plt.plot(env_steps_3_2, returns_3_2,label='HalfCheetah Eval_AverageReturn', color='blue', alpha=0.8)

plt.xlabel('Env Steps')
plt.ylabel('Eval_AverageReturn')
plt.title('Eval_AverageReturn vs Env Steps for HalfCheetah with decreased bgs & blr')
plt.legend()
plt.show()
