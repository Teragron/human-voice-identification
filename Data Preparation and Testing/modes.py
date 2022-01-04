# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:02:58 2022

@author: ahmet
"""

import os
import wave
import argparse
import contextlib
from aio import *
from ipynb.fs.full.laber import *


parser = argparse.ArgumentParser(description= "Convert stereo audio files to mono")
parser.add_argument("-p","--person",type=str, help="Give the name of person, you can Write person1")
parser.add_argument("-m","--mono",type=str, help="makes the audio mono")
parser.add_argument("-t","--trim",type=str, help="Trimms the audio file, you should give the file location ")
parser.add_argument("-v","--visual",type=str, help="makes the audio visual")
parser.add_argument("-a","--audio",type=str, help="directory of voice file")
parser.add_argument("-r","--resize",type=str, help="Resizing spectrogram data to 224x224")
parser.add_argument("-l","--labelvideo",type=str, help="give the directory of video")
parser.add_argument("-lt","--labeltext",type=str, help="give the directory of txt")
parser.add_argument("-ld","--labelduration",type=int, help="give the duration of video")


args = parser.parse_args()

if args.trim!=None:
    with contextlib.closing(wave.open(args.trim,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = int(frames / float(rate))
elif args.visual!=None:
    with contextlib.closing(wave.open("{}".format(args.audio),'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = int(frames / float(rate))
    

if __name__ == "__main__":
    if type(args.mono)==str:
        monomaker(args.mono)
    elif type(args.trim)==str and type(args.person)==str:
        for i in range(0,duration):
            trim_wav(args.trim, args.trim.replace("{}".format(args.trim), "short/{}/{}_trimmed{}.wav".format(args.person,args.person,i)), i,i+1, args.person)
            print(i*100/duration)
    elif type(args.visual)==str:
        if not os.path.exists("spectrogram/{}/".format(args.visual)):
            os.makedirs("spectrogram/{}/".format(args.visual))
        for i in range(0,duration):
          print(i/duration*100)
          trimmed_x_var = "short/{}/{}_trimmed{}.wav".format(args.visual,args.visual,i)
          plotpath = "spectrogram/{}/spec{}.png".format(args.visual,i)
          plotstft(trimmed_x_var,plotpath)
    elif type(args.resize)==str:
        l1 = len([name for name in os.listdir("spectrogram/{}/".format(args.resize)) if os.path.isfile(os.path.join("spectrogram/{}/".format(args.resize), name))])
        for i in range(0,l1):
            resizem("spectrogram/{}/spec{}.png".format(args.resize,i))
            print(i*100/l1)
    elif type(args.labelvideo)==str:
        labeler(args.labelvideo, args.labeltext, args.labelduration)
        liste3 = []
        clips = []
        videos = []
        rekur(args.labelduration-1).ipython_display(width = 720, maxduration=200)