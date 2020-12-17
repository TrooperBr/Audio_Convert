import os
class ConvertAudioUseFFmpeg:
	obj = {}
	"""docstring for ConvertAudioUseFFmpeg"""
	def __init__(self, path=None,_format='m4a',_all=True, filenames=[]):
		self._format = _format
		if path == None:
			path = str(input('Cole o path onde estao os audios :'))
		if _all==True:
			self.get_files(path)
		if _all==False:
			self.get_unique_files(filesnames)
		if str(input('Deseja converter agora(y/n) :')).lower() == 'y':
			for i in self.obj:
				self.convert(file=i, path=self.obj[i])


	def convert(self, file, path):
		new_name = ''
		c=0
		p = file.split(".")
		for i in p:
			if i != self._format:
				new_name += i + '.'
			else:
				new_name +='mp3'

		command = f'''ffmpeg -i "{path}/{file}" "{path}/{new_name}" '''
		os.system(command)


	def get_unique_files(self, filesnames, path):
		for _path, sub, files in os.walk(os.path.join(r'{}'.format(path))):
			if len(files) != 0:
				for file in files:
					if file in filesnames:
						self.obj[file] = _path

	def get_files(self, path):
		for _path, subpath, files in os.walk(os.path.join(r'{}'.format(path))):
			if len(files) != 0:
				for file in files:
					l = file.split('.')
					if l[-1] == self._format:
						self.obj[file] = _path
