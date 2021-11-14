import discord
import os
import discord.ext
import keep_alive
from replit import db
from PIL import Image, ImageDraw
from config import colors
from discord.utils import get
from discord.ext import commands, tasks

client = discord.Client()

client = commands.Bot(command_prefix = '.')

const = 23.5

class Cell:
	def __init__(self, x, y, map):
			self.x = x
			self.y = y
			self.point = db[map][30 - x][y - 1]

	def __setitem__(self, key, value):
		self.point[key] = value 

	def __getitem__(self, key):
		return self.point[key] if key in self.point else None

	def cords(self):
		return (30 - self.x, self.y - 1)
	
	def realCords(self):
		return (self.x, self.y)

def update_under():
	image = Image.open('map.png')
	draw = ImageDraw.Draw(image)
	for y, j in enumerate(db["MAP_UNDER"]):
		for x, i in enumerate(j, 1):
			if "team" in i.value:
				draw.rectangle(((const * x + 1, const * y + 1), (const * (x + 1) + 1, const * (y + 1) + 1)),
                               fill=colors[j])
	image.save('map2.png')
	file = discord.File("map2.png")
	return file
		

@client.event
async def on_ready():
    print("bot online")
    
    
@client.command()
async def test(ctx, *, arg):
    await exec(arg)



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))