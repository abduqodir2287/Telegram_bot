# import requests
# from PIL import Image, ImageFont, ImageDraw
# from textwrap import wrap
#
# font = ImageFont.truetype("arial.ttf", size=30)
# comm = int(input("Suraning raqami: "))
#
# url = f"https://al-quran1.p.rapidapi.com/{comm}"
#
# headers = {
#   "X-RapidAPI-Key": "48ec87fe45mshecb35adf6cb2136p11cf43jsn838685d94fd2",
#   "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers)
# data = response.json()
#
#
# def justify(line, width):
#     gap_width, max_replace = divmod(width - len(line) + line.count(' '), line.count(' '))
#     return line.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)
#
# def lines_formatter(a, width):
#     lines = wrap(a, width, break_long_words=False)
#     for j, line in enumerate(lines[:-1]):
#         if len(line) <= width and line.count(' '):
#             lines[j] = justify(line, width).rstrip()
#     n = '\n'.join(lines)
#     img = Image.new("RGB", (1000, 1000), "black")
#     draw = ImageDraw.Draw(img)
#     draw.text((250, 250), f"{n}", fill="white", font=font)
#     img.show()
#
#
# info = ""
#
# for i in data["verses"]:
#     info += data["verses"][i]["content"]
#
# lines_formatter(info, 30)
#
#
#
# print(info[::-1])

import requests
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap

comm = int(input("Sura raqamini kiriting: "))

url = f"https://al-quran1.p.rapidapi.com/{comm}"

headers = {
  "X-RapidAPI-Key": "48ec87fe45mshecb35adf6cb2136p11cf43jsn838685d94fd2",
  "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

font = ImageFont.truetype("arial.ttf", 40)

def justify(line, width):
    gap_width, max_replace = divmod(width - len(line) + line.count(' '), line.count(' '))
    return line.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)

def lines_formatter(a, width):
    lines = wrap(a, width, break_long_words=False)
    for j, line in enumerate(lines[:-1]):
        if len(line) <= width and line.count(' '):
            lines[j] = justify(line, width).rstrip()
    n = '\n'.join(lines)
    return n


info = ""

for i in data["verses"]:
    info += data['verses'][i]["content"]

l = lines_formatter(info, 40)

img = Image.new("RGB", (1000, 1000), "black")
draw = ImageDraw.Draw(img)
draw.text((250, 250), f"{l[::-1]}", fill="white", font=font)
img.show()

print(l)

