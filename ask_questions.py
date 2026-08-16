from sentence_transformers import util
import numpy as np

def ask_questions(embedded,model,chunks,k):
    question=input("Ask your question: ")
    q=model.encode(question)
    similarity=util.cos_sim(
        q,
        embedded

    )
    similarity=np.array(similarity)
    sorted=np.argsort(similarity.flatten())[::-1][:k]
    chosen_chunks=chunks[sorted]
    return chosen_chunks








