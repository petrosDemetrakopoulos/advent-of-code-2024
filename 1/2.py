from collections import Counter
column1 = []
column2 = []

# Read the file line by line
with open('input.txt', 'r') as file:
    for line in file:
        # Split each line into columns (assuming whitespace-separated)
        values = line.split()
        # Convert the values to float and append to respective lists
        column1.append(int(values[0]))
        column2.append(int(values[1]))

column1.sort()
column2.sort()
right_freqs = Counter(column2)
sim_score = 0
for i in range(len(column1)):
    if column1[i] in column2:
        sim_score += column1[i] * right_freqs[column1[i]]
print(sim_score)