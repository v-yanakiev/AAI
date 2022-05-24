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
signal=1*np.sin(2*np.pi*frequency*timeSteps)+1*np.sin(10*np.pi*frequency*timeSteps)

fftResult = FastFourierTransform(signal)
fftResult_mag=np.abs(fftResult)/len(signal)

f_plot = f[0:int(numberOfSamples/2+1)]
f_plot_mag = 2*fftResult_mag[0:int(numberOfSamples/2+1)]
f_plot_mag[0] = f_plot_mag[0]/2

fig, [ax1, ax2]=plt.subplots(nrows=2,ncols=1)
ax1.plot(timeSteps,signal,'.-')
ax2.plot(f_plot,f_plot_mag,'.-')
ax2.set_xlim([0, 1000])

plt.show()
