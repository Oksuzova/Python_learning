#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "r") as f:
    starting_letter = f.read()

with open("Input/Names/invited_names.txt", "r") as f:
    invited_names = f.readlines()
    for line in invited_names:
        new_name = line.strip()
        new_letter = starting_letter.replace("[name]", new_name)
        with open(f"Output/ReadyToSend/Letter_for_{new_name}.txt", mode="w") as file:
            file.write(new_letter)
