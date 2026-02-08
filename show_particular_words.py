import meaningretriever

def wordmeaning(word):
    """
    Fetches and prints the meaning of a specific word to the console.
    
    Args:
        word (str): The word to look up.
    """
    # Fetch data from the dictionary API
    word_data = meaningretriever.get_word_definitions(word)
    
    if not word_data:
        print(f"No meaning found for '{word}'.")
        return 

    # Iterate through each part of speech and its associated definitions
    for pos, definitions in word_data.items():
        print(f"partOfSpeech\t:{pos}")
        for d in range(len(definitions)):
            # Print definitions with an index for readability
            print(f"definition {d+1}\t:{definitions[d]}")
        print()