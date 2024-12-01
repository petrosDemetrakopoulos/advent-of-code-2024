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
diff_sum = 0
for i in range(len(column1)):
    diff_sum += abs(column1[i] - column2[i])
print(diff_sum)