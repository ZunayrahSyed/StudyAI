import pdfplumber
import numpy as np
import string
from sentence_transformers import SentenceTransformer
from sentence_transformers import util
def extract_text(path,chunk_size,overlap):
    with pdfplumber.open(path) as pdf:
        text=''
        words_per_page=[]
        for i in pdf.pages:
            text+=i.extract_text()
            words_per_page.append(len(i.extract_words()))
        text=text.lower()
        useful=""
        for i in text:
            if i not in string.punctuation and i!='\n':
                useful+=i

        words=useful.split(' ')
        chunks=[]
        sentence=''
        for i in range(0,len(words)):
            sentence+=words[i]+' '
            if i%chunk_size==0 and i!=0:
                chunks.append(sentence)
                sentence=''
                for j in range(overlap):
                    sentence+=words[i-50+j]+' '                                              
    no_of_chunks=len(chunks)
    chunks=np.array(chunks)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedded=model.encode(chunks)
    return embedded,model,chunks



