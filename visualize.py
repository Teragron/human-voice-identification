# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:29:20 2021

@author: ahmet
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks

""" short time fourier transform of audio signal """
def stft(sig, frameSize, overlapFac=0.5, window=np.hanning):
    win = window(frameSize)
    hopSize = int(frameSize - np.floor(overlapFac * frameSize))

    # zeros at beginning (thus center of 1st window should be for sample nr. 0)   
    samples = np.append(np.zeros(int(np.floor(frameSize/2.0))), sig)    
    # cols for windowing
    cols = np.ceil( (len(samples) - frameSize) / float(hopSize)) + 1
    # zeros at end (thus samples can be fully covered by frames)
    samples = np.append(samples, np.zeros(frameSize))

    frames = stride_tricks.as_strided(samples, shape=(int(cols), frameSize), strides=(samples.strides[0]*hopSize, samples.strides[0])).copy()
    frames *= win

    return np.fft.rfft(frames)    

""" scale frequency axis logarithmically """    
def logscale_spec(spec, sr=44100, factor=20.):
    timebins, freqbins = np.shape(spec)

    scale = np.linspace(0, 1, freqbins) ** factor
    scale *= (freqbins-1)/max(scale)
    scale = np.unique(np.round(scale))

    # create spectrogram with new freq bins
    newspec = np.complex128(np.zeros([timebins, len(scale)]))
    for i in range(0, len(scale)):        
        if i == len(scale)-1:
            newspec[:,i] = np.sum(spec[:,int(scale[i]):], axis=1)
        else:        
            newspec[:,i] = np.sum(spec[:,int(scale[i]):int(scale[i+1])], axis=1)

    # list center freq of bins
    allfreqs = np.abs(np.fft.fftfreq(freqbins*2, 1./sr)[:freqbins+1])
    freqs = []
    for i in range(0, len(scale)):
        if i == len(scale)-1:
            freqs += [np.mean(allfreqs[int(scale[i]):])]
        else:
            freqs += [np.mean(allfreqs[int(scale[i]):int(scale[i+1])])]

    return newspec, freqs

""" plot spectrogram"""
def plotstft(audiopath, plotpath ,binsize=2**10, colormap="jet"):
    samplerate, samples = wav.read(audiopath)

    s = stft(samples, binsize)

    sshow, freq = logscale_spec(s, factor=1.0, sr=samplerate)

    ims = 20.*np.log10(np.abs(sshow)/10e-6) # amplitude to decibel

    timebins, freqbins = np.shape(ims)


    """figsize 4.2x8,4 aspect0.1895, dpi 60"""
    plt.figure(figsize=(4.15, 8.30))
    plt.imshow(np.transpose(ims), origin="lower",aspect = "0.1897", cmap=colormap, interpolation="none")

    
    
    plt.savefig(plotpath, bbox_inches="tight",dpi = 60)

    plt.clf()

    return ims

import contextlib
from scipy.io import wavfile
import wave


import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile






cs = "raws/cs/cs.wav"
mert = "raws/mert/mert.wav"


trimmed_cs = "shorts/cs/cs_trimmed"
trimmed_mert = "shorts/mert/mert_trimmed"


mat_cs = "matrix/cs/cs{}.png"
mat_mert = "matrix/mert/mert{}.png"


x_var = '{}'.format(mert)


fname = x_var

with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = int(frames / float(rate))


for i in range(0,duration):
      print(i/duration*100)
      trimmed_x_var = "{}{}.wav".format(trimmed_mert,i)
      filepath = trimmed_x_var
      plopath = mat_mert.format(i)
      ims = plotstft(filepath,plopath)
    
# filepath = "cs_trimmed0.wav"
# plopath = "cs_trimmed1.png"
# ims = plotstft(filepath,plopath)
    
"""3 yer degistirmen gerek: x_var, trimmed_x_var, plopath """