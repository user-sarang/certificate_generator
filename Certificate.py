from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Certicicate:
	def __init__(self, title, name, date):
		self.template = '0.jpg'
		self.title = title
		self.name = name
		self.date = date

	def generate(self):
		footer = "attended the workshop on {} that was held on {}".format(self.title, self.date)
		img = Image.open(self.template,'r')
		img_width, img_height = img.size
		font_type = ImageFont.truetype("arial.ttf", 25)
		font_type_footer  = ImageFont.truetype("arial.ttf", 15)
		draw = ImageDraw.Draw(img)
		user_name = self.name
		text_size = draw.textsize(user_name, font_type)
		footer_size = draw.textsize(footer, font_type_footer)
		text_width = text_size[0]
		text_height = text_size[1]
		footer_width = footer_size[0]
		footer_height = footer_size[1]

		text_x = (img_width-text_width)*0.5
		text_y = (img_height-text_height)*0.5

		footer_x = (img_width-footer_width)*0.5
		footer_y = (img_height-footer_height)*0.6

		draw.text((text_x, text_y),user_name, font=font_type)
		draw.text((footer_x, footer_y),footer, font=font_type_footer)
		fname = self.name + '.jpg'
		fname = fname.lower().replace(' ','_')
		print(fname)
		img.save(fname, subsampling=0, quality=100, mode='RGB')

workshop_name = 'Advanced CFD workshop'
workshop_date = 'October 15, 2017'

for user in open('users.txt'):
	u =user.strip().replace('.','')

	c1 = Certicicate(workshop_name, u.upper(), workshop_date)
	c1.generate()
