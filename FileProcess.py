'''
Load the file of names provided (names.txt) that is provided on Blackboard.
Then repeatedly prompt the user for a name. Search the loaded file.
If the name is found in the file then display a message.
If the name is not in the file, write it to an output file (nofound.txt) and display an appropriate message.
'''

'''
Example output: 
Enter a string (or type exit to quit): Denise
The string Denise is already in the file.
Enter a string (or type exit to quit): John
The string John is already in the file
Enter a string (or type exit to quit): Frank
The string Frank has been written to output.txt
Enter a string (or type exit to quit): 
'''
def promptUser():
    with open('names.txt', 'r') as file:
        content = file.read().lower()

    while True:
        name = input("Enter a string (or type exit to quit): ").strip().lower()

        if name == 'exit':
            print("Goodbye!")
            break

        if name in content:
            print("The name ", name, "is already in the file.")
        else:
            with open("output.txt", "a") as outputFile:
                outputFile.write(name + "\n")
            print("The name ", name, "has been written to output.txt")

promptUser()