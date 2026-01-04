import meaningretriever

def wordmeaning(word):
    word_data = meaningretriever.get_word_definitions(word)
    if not word_data:
        print(f"No meaning found for '{word}'.")
        return 

    for pos, definitions in word_data.items():
        print(f"partOfSpeech\t:{pos}")
        for d in range(len(definitions)):
            print(f"definition {d+1}\t:{definitions[d]}")
        print()