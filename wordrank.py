def words_or_text_to_CEFR(nlp,analyzer,word,levelorg):

    doc=nlp(word)
    
    tokens=analyzer.analize_doc(doc)
    finallist=[]
    for token in tokens:
        if token[2]==False and token[3]>levelorg:
            finallist.append(token[0])
    finallist= list(set(finallist)) # to remove duplicates
    return finallist