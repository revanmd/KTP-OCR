class Person:
	nama = ""
	nik = ""
	tempat = ""
	tgl_lahir = ""
	kec = ""
	kel = ""
    
	def to_list(self):
		return [self.nama,self.nik,self.tempat,self.tgl_lahir,self.kec,self.kel]

	def to_dict(self):
		return {
			'nama':self.nama,
			'nik':self.nik,
			'tempat':self.tempat,
			'tgl_lahir':self.tgl_lahir,
			'kec':self.kec,
			'kel':self.kel
		}
		
	def get_index():
		return ["nama","nik","tempat","tgl_lahir","kec","kel"]