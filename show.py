import show_particular_words
def s_r(words):
    while(True):
        print("-"*50)
        print(f"\nnumber\t:word\n")
        for i in range(len(words)):
            print(f"{i}\t:{words[i]}")
        print("-"*50)
        number=input("\nenter the number to get the meaning of the words \nenter -1 for going back to page selction section\n\n")
        print("-"*50)

        try:
            number=int(number)
            if int(number)==-1:
                print("-"*50)
                return
            elif number in range(len(words)):
                index=int(number)
                print(f"word[{index}]\t:{words[index]}\n")
                show_particular_words.wordmeaning(words[index])
            else:
                print("#### CHECK YOUR DAMN EYES #### number out of range.")
                
        except ValueError:
            print(f"word\t:{number}\n")
            show_particular_words.wordmeaning(number)
        
        input("\nPress Enter to continue...")