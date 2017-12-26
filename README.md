# PhonemeRecog
School project

For TIMIT nist to riff conversion ( windows ) : 

1- install sox.

2- add sox to path. Temporary solution : 
```bash
SET PATH=%PATH%;"C:\path to sox folder"
```
3- go to directory containing TIMIT data.

4- run this command. ( not he fastest but does the trick ) 
```bash
forfiles /s /m *.wav /c "cmd /c sox  @file @fnameRIFF.wav"
```
