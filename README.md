# PhonemeRecog
School project. This work is a proof of concept on using pure neural networks ( with MFCC ) for phoneme recognition. So far only the BGRU model was test, we achieve a 57% ( but training was stopped while it was still getting better ) accuracy on the whole TIMIT Test set after roughly 16hours of training on a GTX 950M GPU. We will conduct more structured tests in the future. 





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
