from tkinter import messagebox
import pytube
from tkinter import *
import time
import os

window = Tk()
window.title('Youtube download')
window.resizable(height= True, width= True)
window.minsize(height= 500, width= 500)

img = PhotoImage(file = 's.png')
Label(window, image = img).place(x = 0, y = 0, relwidth= 1, relheight= 1)

text = Label(window, text= 'Hello keo', font= ('Arial', 20))
text.place(x= 0, y= 0)

text2 = Label(window, text= 'Nhập link youtube muốn download:', font= ('Arial', 12))
text2.place(x= 0, y= 35)

#Tạo một Textbox
txt = Entry(window, width= 50)
#Vị trí xuất hiện của Textbox
txt.place(x= 0, y= 62)

#Đặt vị trí con trỏ tại Textbox
txt.focus()

#Hàm khi nút được nhấn
def helloCall():
    try:
        # Lấy giá trị từ ô nhập liệu
        youtube_url = pytube.YouTube(txt.get())
        
        messagebox.showinfo("Message", 'Downloading video...')
        
        #download video từ link youtube_url và bỏ vào thư mục muốn
        stream = youtube_url.streams.get_highest_resolution()
        download_path = "E:\Youtube_download"
        stream.download(output_path= download_path)
        
        messagebox.showinfo("Message", 'Video has been downloaded')
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

#Gọi hàm helloCall khi nút được nhấn
btn = Button(window, text= "Download", command= helloCall)
btn.place(x= 0, y= 90)

window.mainloop()

'''
video_url = input("Write your video url: ")
yt = pytube.YouTube(video_url)

stream = yt.streams.get_highest_resolution()
stream.download()
print("Video has been downloaded")
'''
