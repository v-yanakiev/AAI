import numpy as np
import matplotlib.pyplot as plt

from fft import FastFourierTransform

samplingFrequency =2**20
tstep=1/samplingFrequency
frequency=128
numberOfSamples=int(samplingFrequency/frequency)
timeSteps=np.linspace(0,(numberOfSamples-1)*tstep,numberOfSamples)
fstep=samplingFrequency/numberOfSamples
f=np.linspace(0,(numberOfSamples-1)*fstep,numberOfSamples)
signal=1*np.sin(2*np.pi*frequency*timeSteps)+1*np.sin(4*np.pi*frequency*timeSteps)+1*np.sin(28*np.pi*frequency*timeSteps)

fftResult = FastFourierTransform(signal);

fftResult_mag=np.abs(fftResult)/len(signal)

f_plot = f[0:int(numberOfSamples/2+1)]
f_plot_mag = 2*fftResult_mag[0:int(numberOfSamples/2+1)]
f_plot_mag[0] = f_plot_mag[0]/2
identifiedFrequencies=[];
for i,magnitude in enumerate(f_plot_mag):
  if magnitude>0.8:
    identifiedFrequencies.append([f_plot[i],magnitude])



fig, subplotsUsed=plt.subplots(nrows=len(identifiedFrequencies)+1,ncols=1)
subplotsUsed[0].plot(timeSteps,signal,'.-')
for i,signalInformation in enumerate(identifiedFrequencies):
  decodedFrequency=identifiedFrequencies[i][0]
  decodedMagnitude=identifiedFrequencies[i][1]
  decodedSignal=decodedMagnitude*np.sin(2*np.pi*decodedFrequency*timeSteps)
  subplotsUsed[i+1].plot(timeSteps,decodedSignal,'.-')
plt.show()
