# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageOps
from easygui import fileopenbox
import os


def generate(photo_name, upper_text, lower_text):
    first_line_text = upper_text
    second_line_text = ""
    image = Image.open(f'{photo_name}')
    image = ImageOps.expand(image, border=6, fill="black")
    image = ImageOps.expand(image, border=4, fill="white")

    old_width, old_height = image.size[0], image.size[1]
    new_width = int(old_width*1.2) if old_height < old_width else int(old_width*1.35)
    new_height = int(old_height*1.33)
    second_image_height = new_height

    upper_font_size = int(new_height/9)
    lower_font_size = int(new_height/16)

    if len(upper_text) >= 12 and new_width < new_height:
        upper_font_size -= 15
    
    upper_text_font = ImageFont.truetype("times.ttf", upper_font_size)
    lower_text_font = ImageFont.truetype("arial.ttf", lower_font_size)
    uw, uh = upper_text_font.getsize(upper_text)
    lw, lh = lower_text_font.getsize(lower_text)
    flw = uw
    slw = uw
    
    if uw > new_width:
        second_image_height = int(new_height + uh*1.2)
        upper_text_list = upper_text.split(" ")
        half_index = int(len(upper_text_list)/2)
        first_line_text = " ".join(upper_text_list[0:half_index])
        second_line_text = " ".join(upper_text_list[half_index::])
        flw = upper_text_font.getsize(first_line_text)[0]
        slw = upper_text_font.getsize(second_line_text)[0]

    new_image = Image.new("RGB", (new_width, second_image_height))
    new_image.paste(image, (int((new_width-old_width)/2), int((new_height-old_height)/2-(old_height/10))))
    
    draw = ImageDraw.Draw(new_image)
    draw.text((int((new_width-flw)/2), int(old_height+uh/3)), first_line_text, font=upper_text_font)
    draw.text((int((new_width-slw)/2), int(old_height+uh*1.25)), second_line_text, font=upper_text_font)
    draw.text((int((new_width-lw)/2), int(second_image_height-lh*1.5)), lower_text, font=lower_text_font)
    
    file_name = f"{os.path.splitext(os.path.basename(photo_name))[0]}_demotivator.png"
    new_image.show()
    #new_image.save(file_name)


if __name__ == "__main__":
    # photo_link = fileopenbox(filetypes=["*.jpg", "*.jpeg", "*.png"])
    # upper_text = input("Enter upper text: ")
    # lower_text = input("Enter lower text: ")
    generate("artur.jpg", "влад", "бумага")
    # generate(photo_link, upper_text, lower_text)