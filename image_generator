from PIL import Image, ImageDraw, ImageFont

base = Image.open(r"C:\Users\Admin\Downloads\yes.png").convert("RGBA")

txt = Image.new("RGBA", base.size, (255,255,255,0))

fnt = ImageFont.truetype(r"C:\Users\Admin\Downloads\font.ttf", 106)
d = ImageDraw.Draw(txt)

d.text((614,842), "-12-16", font=fnt, fill=(49,62,63,255))

out = Image.alpha_composite(base, txt)

out.save(r'C:\Users\Admin\Downloads\ok.png')
