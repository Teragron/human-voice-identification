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


![](gits/gitdirs.png)
