import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;
def FastFourierTransform(vectorForWhichToCompute):
    vectorSize = vectorForWhichToCompute.shape[0]
    if vectorSize % 2 > 0:
        raise ValueError("Vector must be a power of 2!")
    elif vectorSize <= 2:
        return DiscreteFourierTransform(vectorForWhichToCompute)
    else:
        even = FastFourierTransform(vectorForWhichToCompute[::2])
        odd = FastFourierTransform(vectorForWhichToCompute[1::2])
        terms = np.exp(-2j * np.pi * np.arange(vectorSize) / vectorSize)
        return np.concatenate([even + terms[:int(vectorSize/2)] * odd,
                               even + terms[int(vectorSize/2):] * odd])
def DiscreteFourierTransform(vectorForWhichToCompute):
    vectorSize = vectorForWhichToCompute.shape[0]
    generated = np.arange(vectorSize)
    new = generated.reshape((vectorSize, 1))
    toMultiply = np.exp(-2j * np.pi * new * generated / vectorSize)
    return np.dot(toMultiply, vectorForWhichToCompute)
# randomArray = np.array([np.sin(item)+np.sin(item+0.5) for item in range(128)])
randomArray = np.array([np.sin(item/10)+np.sin(item/5)+np.random.rand()-0.5 for item in range(256)])
plt.title("Before FFT")
plt.subplot(1, 2, 1)
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.plot(range(randomArray.shape[0]),randomArray)

plt.subplot(1, 3, 3)
plt.xlabel('Frequency')
plt.ylabel('Intensity')
plt.plot(range(randomArray.shape[0]),FastFourierTransform(randomArray))

plt.show();
# print(np.allclose(FastFourierTransform(randomArray), np.fft.fft(randomArray)))