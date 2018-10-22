# PhonemeRecog
School project. This work is a proof of concept for end to end phoneme recognition using Reccurent Neural Networks ( without MFCC ). So far only the bi-directional Gated Reccurent unit (BGRU) model was tested, we achieve a 57% on 10k batchs accuracy on the whole TIMIT Test set after roughly 16hours of training on a GTX 950M GPU. A paper already studied the use of Convolutional Neural Networks ( https://arxiv.org/pdf/1312.2137.pdf ) achieving up to 70% accuracy.





For TIMIT nist to riff conversion ( windows ) : 
 
1- install sox.

2- add sox to path. Temporary solution : 
```bash
SET PATH=%PATH%;"C:\path to sox folder"
```
3- go to directory containing TIMIT data.

4- run this command. ( not the fastest but does the trick ) 
```bash
forfiles /s /m *.wav /c "cmd /c sox  @file @fnameRIFF.wav"
```
