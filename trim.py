# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:40:24 2021

@author: ahmet
"""

from scipy.io import wavfile


import wave
import contextlib
from pydub import AudioSegment

cs = "raws/cs/cs.wav"
mert = "raws/mert/mert.wav"


x_var = '{}'.format(mert)

sound = AudioSegment.from_wav(x_var)
sound = sound.set_channels(1)
sound.export(x_var, format="wav")


fname = x_var

with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = int(frames / float(rate))


def trim_wav( originalWavPath, newWavPath , start, end ):
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( newWavPath, sampleRate, waveData[startSample:endSample])
 

# fname2 = "ag.wav"
# trim_wav(fname2, fname2.replace(".wav", "_trimmed.wav"), 60,61)

for i in range(0,duration):
    trim_wav(fname, fname.replace(".wav", "_trimmed{}.wav".format(i)), i,i+1)
    print(i/duration*100)
    

