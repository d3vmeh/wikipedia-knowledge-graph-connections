from knowledge_graph import *


documents = load_documents(query = "George Washington")
graph = convert_documents(documents)
create_vector_index()

chain = create_graph(graph, documents)


while True:
    q = input("Enter a query: ")
    print("\n")
    print(structured_retriever(q, graph))
    print("\n")
    print(chain.invoke({"question": q}))
    print("\n\n")

