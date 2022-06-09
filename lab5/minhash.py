import numpy as np

def minhash(doc2term):
    i = np.argmax(doc2term)
    