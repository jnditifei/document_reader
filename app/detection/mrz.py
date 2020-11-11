from passporteye import read_mrz

class Mrz:

	def __init__(self, image):
		self.image = image
		self.mrz_data = None

	def detection(self):
		mrz = read_mrz(self.image, save_roi=True)
		# Obtain image
		self.mrz_data = mrz.to_dict()
		return self.mrz_data