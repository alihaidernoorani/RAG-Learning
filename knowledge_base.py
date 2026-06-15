def search_documents(query, documents):
    stop_words = ["what", "is", "in", "the", "a", "an"]
    query_words = [word for word in query.lower().split() if word not in stop_words]
    best_score = 0
    best_document = None
    results = []
    
    for document in documents:
        count = 0
        for word in query_words:
            if word in document.lower():
                count += 1
        if count > best_score:
            best_score = count
            best_document = document
        results.append((document,count))

    results.sort(key=lambda x: x[1], reverse=True)
    print("\nTop results:")
    for doc, score in results[:3]:
        print(score, "->", doc)
    if best_document:
        print(f"The best match is {best_document}")     
    else:
        print("Not found")   


documents = [
    "Python classes are blueprints used to create objects.",
    "An object is an instance of a class.",
    "Inheritance allows child classes to reuse code from parent classes.",
    "Lists store multiple values in a single variable.",
    "Dictionaries store data as key-value pairs."
]

query = input("Ask a question: ")
search_documents(query, documents)
