import show_particular_words

def s_r(words):
    """
    Displays a list of words and enters a loop allowing the user to 
    select a word by index to see its definition.
    
    Args:
        words (list): List of strings (vocabulary words).
    """
    while(True):
        print("-" * 50)
        print(f"\nnumber\t:word\n")
        # List all identified words with an index number
        for i in range(len(words)):
            print(f"{i}\t:{words[i]}")
        print("-" * 50)
        
        number = input("\nEnter the number to get the meaning of the word\nEnter -1 to go back to page selection\n\n")
        print("-" * 50)

        try:
            # Check if the user wants to go back
            number = int(number)
            if number == -1:
                print("-" * 50)
                return
            
            # If the number is a valid index, show the meaning
            elif number in range(len(words)):
                index = int(number)
                print(f"word[{index}]\t:{words[index]}\n")
                show_particular_words.wordmeaning(words[index])
            else:
                print("#### CHECK YOUR DAMN EYES #### number out of range.")
                
        except ValueError:
            # If user enters text instead of a number, treat it as a direct word search
            print(f"word\t:{number}\n")
            show_particular_words.wordmeaning(number)
        
        input("\nPress Enter to continue...")