"# Convert Audio" 
You can pass a path from the files and the type from file, defaut is m4a


to get all intens the variable _all is True
```py

ConvertAudioUseFFmpeg(path=None,_format='m4a',_all=True, filenames=[])
```
if you need only expesific files use
```py
files = ['audio1.m4a', 'audio2.m4a'] #list a files name
ConvertAudioUseFFmpeg(path=None,_format='m4a',_all=False, filenames=files)
```
