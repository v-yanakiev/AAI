import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;
def FastFourierTransform(vectorForWhichToCompute):
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
    vectorSize = vectorForWhichToCompute.shape[0]
    generated = np.arange(vectorSize)
    new = generated.reshape((vectorSize, 1))
    toMultiply = np.exp(-2j * np.pi * new * generated / vectorSize)
    return np.dot(toMultiply, vectorForWhichToCompute)
def generateSeries(freq,vectorSize):
    return np.array([np.sin(2*np.pi*item*freq)+np.sin(2*np.pi*item*(freq+100)) for item in range(vectorSize)])
# randomArray = np.array([np.sin(2*np.pi*item*1/10)+np.sin(2*np.pi*item/3)+np.random.rand()-0.5 for item in range(1024)])
freq=1/100
vectorSize=128
randomArray = generateSeries(freq,vectorSize)
# result = np.sort(FastFourierTransform(randomArray));


plt.title("Before FFT")
plt.subplot(1, 2, 1)
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.plot(range(randomArray.shape[0]),randomArray)
fftResult = FastFourierTransform(randomArray)

plt.subplot(1, 3, 3)
# plt.xlim(0,20);
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
toPlot=(2.0/vectorSize)*np.abs(fftResult[:vectorSize//2]) 
plt.plot(range(fftResult.shape[0]),fftResult);

plt.show();
# print(np.allclose(FastFourierTransform(randomArray), np.fft.fft(randomArray)))