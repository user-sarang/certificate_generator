from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from datetime import datetime
import os

class Certicicate:
	def __init__(self, title, name, date):
		self.template = 'certificate_template/0.jpg'
		self.title = title
		self.name = name
		self.date = date

	def generate(self):
		img = Image.open(self.template,'r')
		draw = ImageDraw.Draw(img)

		name_font_object = ImageFont.truetype("arial.ttf", 64)
		footer_font_object  = ImageFont.truetype("arial.ttf", 35)
		
		name = self.name.upper()
		footer = "{} that was held on {}".format(self.title, self.date)

		# Settings from sketch
		scale_factor = 1.5
		name_x = 101*scale_factor
		name_y = 467*scale_factor

		footer_x = 101*scale_factor
		footer_y = 640*scale_factor

		"""
		text_width = text_size[0]
		text_height = text_size[1]
		footer_width = footer_size[0]
		footer_height = footer_size[1]


		text_x = (img_width-text_width)*0.5
		text_y = (img_height-text_height)*0.5

		footer_x = (img_width-footer_width)*0.5
		footer_y = (img_height-footer_height)*0.6
		"""

		draw.text((name_x, name_y),name, font=name_font_object, fill=(0,0,0,0))
		draw.text((footer_x, footer_y),footer, font=footer_font_object, fill=(0,0,0,0))
		t = datetime.today()
		date = t.strftime('%Y-%m-%d')
		fdir = self.title + '_' + date
		fdir = os.path.join(os.getcwd(), fdir)
		if not os.path.isdir(fdir): os.mkdir(fdir)

		fname = self.name + '.jpg'
		fname = fname.lower().replace(' ','_')
		fname = os.path.join(fdir, fname)
		
		img.save(fname, subsampling=0, quality=100, mode='RGB')


workshop_name = 'Advanced Crash worthiness'
workshop_date = 'November 19, 2017'

for user in open('users.txt'):
	u =user.strip().replace('.','')
	if len(u)>0:
		c1 = Certicicate(workshop_name, u, workshop_date)
		c1.generate()





