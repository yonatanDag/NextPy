# 6.1.3

# import tkinter as tk
# from tkinter import PhotoImage
#
# root = tk.Tk()
#
# question_label = tk.Label(root, text="Who is the GOAT???")
# question_label.pack()
#
#
# def show_saba_Image():
#     image = PhotoImage(file="saba.png")
#     image_label = tk.Label(root, image=image)
#     image_label.image = image
#     image_label.pack()
#
#
# def show_sigit_Image():
#     image = PhotoImage(file="guyg.png")
#     image_label = tk.Label(root, image=image)
#     image_label.image = image
#     image_label.pack()
#
#
# saba_answer_button = tk.Button(root, text="Show all time answer", command=show_saba_Image)
# saba_answer_button.pack()
#
# sigit_answer_button = tk.Button(root, text="Show sigit answer", command=show_sigit_Image)
# sigit_answer_button.pack()
#
# root.mainloop()

# 6.1.4


# import base64
#
# encoded_message = """
# CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo=
# """
#
# decoded_bytes = base64.b64decode(encoded_message)
# decoded_message = decoded_bytes.decode('utf-8')
#
# print(decoded_message)


# 6.3.3

from gtts import gTTS
import os

# text = "first time i'm using a package in next.py course"
text = "Tomer Elmaliach and Guy G are the GOATED"
language = 'en'

speech = gTTS(text=text, lang=language, slow=False)

speech.save("output.mp3")

os.system("start output.mp3")
