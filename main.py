from knowledge_graph import *


documents = load_documents(query = "George Washington")
graph = convert_documents(documents)

export_graph_to_csv

create_vector_index()

chain = create_graph(graph, documents)


chat_history = []
while True:
    q = input("Enter a query: ")
    print("\n")
    print(structured_retriever(q, graph))
    print("\n")
    response = chain.invoke({"question": q, "chat_history": chat_history})
    print(response)
    print("\n\n")
    chat_history.append((q, response))
    print(chat_history)

