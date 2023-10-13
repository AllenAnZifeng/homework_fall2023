# import necessary libraries
import matplotlib.pyplot as plt

# these are dummy values, replace these lists with your actual data

returns_3_1 = []  # Fill this list with your Eval_AverageReturn for each iteration
returns_3_2 = []
returns_3_3 = []
returns_3_4 = []

env_steps_3_1 = []
env_steps_3_2 = []
env_steps_3_3 = []
env_steps_3_4 = []




# for line in open('3-1data.txt'):  # adjust with your log file
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
# for line in open('3-2data.txt'):  # adjust with your log file
#
#     if "Train_EnvstepsSoFar" in line:
#         parts = line.split()
#         step = float(parts[-1])
#         env_steps_3_2.append(step)
#
#     if "Eval_AverageReturn" in line:
#         parts = line.split()
#
#         score = float(parts[-1])
#         returns_3_2.append(score)
#
# for line in open('3-3data.txt'):  # adjust with your log file
#
#     if "Train_EnvstepsSoFar" in line:
#         parts = line.split()
#         step = float(parts[-1])
#         env_steps_3_3.append(step)
#
#     if "Eval_AverageReturn" in line:
#         parts = line.split()
#
#         score = float(parts[-1])
#         returns_3_3.append(score)
#
# for line in open('3-4data.txt'):  # adjust with your log file
#
#     if "Train_EnvstepsSoFar" in line:
#         parts = line.split()
#         step = float(parts[-1])
#         env_steps_3_4.append(step)
#
#     if "Eval_AverageReturn" in line:
#         parts = line.split()
#
#         score = float(parts[-1])
#         returns_3_4.append(score)



for line in open('3-5data.txt'):  # adjust with your log file


    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_3_1.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_3_1.append(score)





for line in open('3-6data.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_3_2.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_3_2.append(score)

for line in open('3-7data.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_3_3.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_3_3.append(score)

for line in open('3-8data.txt'):  # adjust with your log file

    if "Train_EnvstepsSoFar" in line:
        parts = line.split()
        step = float(parts[-1])
        env_steps_3_4.append(step)

    if "Eval_AverageReturn" in line:
        parts = line.split()

        score = float(parts[-1])
        returns_3_4.append(score)


plt.figure(figsize=(10,6))
plt.plot(env_steps_3_1, returns_3_1,label='vanilla pg', color='blue', alpha=0.5)
plt.plot(env_steps_3_2, returns_3_2,label='-rtg pg', color='red', alpha=0.5)
plt.plot(env_steps_3_3, returns_3_3,label='-na pg', color='green', alpha=0.5)
plt.plot(env_steps_3_4, returns_3_4,label='-na -rtg pg', color='black', alpha=0.5)
plt.xlabel('Env Steps')
plt.ylabel('Eval Average Return')
plt.title('Eval Average Return vs Env Steps for 4000 samples')
plt.legend()
plt.show()
