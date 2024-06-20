from PIL import Image, ImageDraw

# Create Dino Image (50x50)
dino_img = Image.new('RGB', (50, 50), color = 'green')
dino_draw = ImageDraw.Draw(dino_img)
dino_draw.rectangle([10, 10, 40, 40], fill='darkgreen')
dino_img.save('dino.png')

# Create Cactus Image (30x60)
cactus_img = Image.new('RGB', (30, 60), color = 'green')
cactus_draw = ImageDraw.Draw(cactus_img)
cactus_draw.rectangle([10, 10, 20, 50], fill='darkgreen')
cactus_img.save('cactus.png')

# Create Background Image (800x400)
background_img = Image.new('RGB', (800, 400), color = 'skyblue')
background_draw = ImageDraw.Draw(background_img)
background_draw.rectangle([0, 300, 800, 400], fill='lightgreen')  # Ground
background_img.save('background.png')
