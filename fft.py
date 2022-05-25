import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;
def FastFourierTransform(vectorForWhichToCompute):
    vectorForWhichToCompute=np.asarray(vectorForWhichToCompute,dtype=float)
    vectorSize = vectorForWhichToCompute.shape[0]
    if vectorSize % 2 > 0:
        raise ValueError("Vector size must be a power of 2!")
    elif vectorSize <= 2:
        return DiscreteFourierTransform(vectorForWhichToCompute)
    else:
        even = FastFourierTransform(vectorForWhichToCompute[::2])
        odd = FastFourierTransform(vectorForWhichToCompute[1::2])
        terms = np.exp(-2j * np.pi * np.arange(vectorSize) / vectorSize)
        return np.concatenate([even + terms[:int(vectorSize/2)] * odd,
                               even + terms[int(vectorSize/2):] * odd])
def DiscreteFourierTransform(vectorForWhichToCompute):
    vectorForWhichToCompute=np.asarray(vectorForWhichToCompute,dtype=float)
    vectorSize = vectorForWhichToCompute.shape[0]
    generated = np.arange(vectorSize)
    new = generated.reshape((vectorSize, 1))
    toMultiply = np.exp(-2j * np.pi * new * generated / vectorSize)
    return np.dot(toMultiply, vectorForWhichToCompute)