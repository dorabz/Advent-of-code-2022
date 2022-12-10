"""
Advent of code - 2022 - day 1 

Description of code:

PART 1:
This code opens the input file for reading, then reads each line from the file and parses the calories from the line. 
It uses an empty line to indicate the end of one elf's inventory and the start of the next. 
It stores the total calories for each elf in a list, then finds the maximum value in that list and prints it.

PART 2:
This code opens the input file for reading, then reads each line from the file and parses the calories from the line.
It uses an empty line to indicate the end of one elf's inventory and the start of the next. 
It stores the total calories for each elf in a list, then sorts the list in descending order and takes the top three values. 
Finally, it prints the total calories carried by the top three elves.


"""
# PART 1
#
# Open the input file for reading
with open("input.txt") as file:
    calories = []
    current_elf = []

    # Read each line from the file
    for line in file:
        line = line.strip()

        # If line is empty, store current elf's calories and reset current elf's list
        if not line:
            calories.append(sum(current_elf))
            current_elf = []
            continue

        # Parse calorie from line and append to current elf's list
        current_elf.append(int(line))

    # Store current elf's calories
    calories.append(sum(current_elf))

    # Find the elf with the most calories
    max_calories = max(calories)

    # Print the number of calories carried by the elf with the most calories
    print(max_calories)
#
# ans: 69501


# PART2
#
# Open the input file for reading
with open("input.txt") as file:
    calories = []
    current_elf = []

    # Read each line from the file
    for line in file:
        line = line.strip()

        # If line is empty, store current elf's calories and reset current elf's list
        if not line:
            calories.append(sum(current_elf))
            current_elf = []
            continue

        # Parse calorie from line and append to current elf's list
        current_elf.append(int(line))

    # Store current elf's calories
    calories.append(sum(current_elf))

    # Sort the list of calories in descending order
    calories.sort(reverse=True)

    # Take the top three values from the list
    top_calories = calories[:3]

    # Print the total calories carried by the top three elves
    print(sum(top_calories))

# ans: 202346