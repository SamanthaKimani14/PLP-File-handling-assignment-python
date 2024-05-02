# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as f:
        f.write('Hello, my file!\n')
        f.write('This is line 2.\n')
        f.write('And this is line 3 with a number: 42\n')
except Exception as e:
    print(f"Error creating file: {e}")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as f:
        print("\nFile Contents:")
        for line in f:
            print(line.strip())
except Exception as e:
    print(f"Error reading file: {e}")

# File Appending
try:
    with open('my_file.txt', 'a') as f:
        f.write('\nThis is line 4.')
        f.write('\nThis is line 5 with a number: 13.')
        f.write('\nThis is line 6 with a string: "Python"')
except Exception as e:
    print(f"Error appending file: {e}")

# Error Handling
try:
    with open('my_file.txt', 'r') as f:
        print("\nFile Contents:")
        for line in f:
            print(line.strip())
except Exception as e:
    print(f"Error reading file: {e}")
finally:
    print("\nFile handling complete.")