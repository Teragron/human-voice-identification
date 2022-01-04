# Human-Voice-Classification
Voice Identification and Labeling based on mono audio Spectrogram Data


## What is Human Voice Recognition?
Analyzing and learning the person's specific voice and using it to fine-tune the recognition of that person's speech.

You can visit [this page](https://www.macmillandictionary.com/dictionary/british/voice-recognition) for the dictionary definition.

## Installation
I would recommend to download this repository for better workspace in command-line.

## Demo
[![Watch the video](https://i9.ytimg.com/vi_webp/aJP5xogUpQg/mqdefault.webp?sqp=CNDU0Y4G&rs=AOn4CLBkAohqQ2RLUis8iC2rBZkgzOngnA)](https://www.youtube.com/watch?v=aJP5xogUpQg)

This demo is a demonstration for 2-Class speech-Recognition. 

It has been trained with total of 4 hours audio clip and 16300 spectrogram image data.

## How it works?
The model, which is a "Deep Residual Learning for Image Recognition" looks at the voice classes based on given spectrogram image datas, that has been preprocessed.

Then for the real test Phase, the model makes predictions for the given .wav file and overlays the prediction to the corresponding video.

![](gits/algorithm.png)

## How to run it?

Before running the scripts it is better to use the following directorial tree:

![](gits/gitdirs.png)

1. Since we will be running the scripts from command line, we should go to the directory of this repository on the computer. For me it was

```bash
cd desktop/proje
```

After that we can start off with converting the stereo .wav file to mono .wav file.

```bash
python modes.py -m voice/person1.wav
```

In this way we've halved the size of .wav file.

Besides that the parameters that give us spacial information are now eliminated, thus we have a better chance to prevent any overlocalization. (This is the part i'm not sure about if this kind of eliminition makes any sence)

2. Then we crop the mono .wav file to 1 second long audio clips

```bash
python modes.py -t voice/person1.wav -p person1
```
3. Now we create some visual data

```bash
python modes.py -v person1 -a voice/person1.wav

```
