# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 00:42:07 2022

@author: ahmet
"""
import os
import wave
import os.path
import contextlib
import numpy as np
from PIL import Image
from pydub import AudioSegment
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
from matplotlib import pyplot as plt

def monomaker(x):
    sound = AudioSegment.from_wav(x)
    sound = sound.set_channels(1)
    sound.export(x, format="wav")
    

def trim_wav( originalWavPath, newWavPath , start, end ,kisi):
    with contextlib.closing(wave.open(originalWavPath,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        global duration
        duration = int(frames / float(rate))
    sampleRate, waveData = wav.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    if not os.path.exists("short/{}/".format(kisi)):
        os.makedirs("short/{}/".format(kisi))
    wav.write( newWavPath, sampleRate, waveData[startSample:endSample])



def stft(sig, frameSize, overlapFac=0.5, window=np.hanning):
    win = window(frameSize)
    hopSize = int(frameSize - np.floor(overlapFac * frameSize))
    samples = np.append(np.zeros(int(np.floor(frameSize/2.0))), sig)    
    cols = np.ceil( (len(samples) - frameSize) / float(hopSize)) + 1
    samples = np.append(samples, np.zeros(frameSize))
    frames = stride_tricks.as_strided(samples, shape=(int(cols), frameSize), strides=(samples.strides[0]*hopSize, samples.strides[0])).copy()
    frames *= win
    return np.fft.rfft(frames)    

def logscale_spec(spec, sr=44100, factor=20.):
    timebins, freqbins = np.shape(spec)
    scale = np.linspace(0, 1, freqbins) ** factor
    scale *= (freqbins-1)/max(scale)
    scale = np.unique(np.round(scale))
    newspec = np.complex128(np.zeros([timebins, len(scale)]))
    for i in range(0, len(scale)):        
        if i == len(scale)-1:
            newspec[:,i] = np.sum(spec[:,int(scale[i]):], axis=1)
        else:        
            newspec[:,i] = np.sum(spec[:,int(scale[i]):int(scale[i+1])], axis=1)
    allfreqs = np.abs(np.fft.fftfreq(freqbins*2, 1./sr)[:freqbins+1])
    freqs = []
    for i in range(0, len(scale)):
        if i == len(scale)-1:
            freqs += [np.mean(allfreqs[int(scale[i]):])]
        else:
            freqs += [np.mean(allfreqs[int(scale[i]):int(scale[i+1])])]
    return newspec, freqs

def plotstft(filepath, plotpath ,binsize=2**10, colormap="jet"):
    samplerate, samples = wav.read(filepath)
    s = stft(samples, binsize)
    sshow, freq = logscale_spec(s, factor=1.0, sr=samplerate)
    ims = 20.*np.log10(np.abs(sshow)/10e-6) 
    timebins, freqbins = np.shape(ims)
    plt.figure(figsize=(4.15, 8.30))
    plt.imshow(np.transpose(ims), origin="lower",aspect = "0.1897", cmap=colormap, interpolation="none")
    plt.savefig(plotpath, bbox_inches="tight",dpi = 60)
    plt.clf()
    
def resizem(spec):
  sizem = 224,224
  image1 = Image.open(spec)
  width1, height1 = image1.size
  new_image1 = image1.resize((sizem))
  new_image1.save(spec)
    
