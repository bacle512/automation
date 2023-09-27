import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip

screen = Tk()
screen.title('Password generator')
screen.resizable(height= True, width= True)
screen.minsize(height= 500, width= 500)

text = Label(screen, text= 'Input your password length:', font= ('Arial', 25))
text.place(x= 0, y= 0)

#Tạo một Textbox
txt = Entry(screen, width= 8, font=('Arial', 16))
#Vị trí xuất hiện của Textbox
txt.place(x= 0, y= 48)
#Đặt vị trí con trỏ tại Textbox
txt.focus()

# Label để hiển thị mật khẩu
result_label = Label(screen, text= '', font= ('Arial', 16))
result_label.place(x= 0, y= 90)

# Entry widget để hiển thị và chỉnh sửa mật khẩu
password_entry = Entry(screen, width= 30, font=('Arial', 16))  # show='*' để ẩn mật khẩu
password_entry.place(x= 0, y= 115)

#Hàm khi nút được nhấn
def generatePassword():
    try:
        # Lấy giá trị số từ ô nhập liệu
        passwordLen = int(txt.get())
        my_password = ''
        
        # Kiểm tra xem độ dài mật khẩu hợp lệ (lớn hơn 0)
        if passwordLen <= 7:
            messagebox.showerror("Error", "Please enter a valid password length (greater than 7).")
            return

        # Tạo mật khẩu chỉ bằng chữ cái và số
        for i in range(passwordLen):
            my_password += random.choice(string.ascii_letters + string.digits)

        # Hiển thị mật khẩu trên Label
        result_label.config(text= "Your new password is:")
        
        # Hiển thị mật khẩu trong Entry widget
        password_entry.delete(0, END)  # Xóa mật khẩu cũ (nếu có)
        password_entry.insert(0, my_password)
        
        messagebox.showinfo("Message", f"Your password is: {str(my_password)}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        

#hàm copy mật khẩu        
def copy_password():
    # Lấy mật khẩu từ Entry widget
    password = password_entry.get()
    
    # Sao chép mật khẩu vào clipboard
    pyperclip.copy(password)
    messagebox.showinfo("Message", "Password has been copied to clipboard.")

# Button để tạo mật khẩu
btn = Button(screen, text= "Generate", command= generatePassword)
btn.place(x= 100, y= 48)

# Button để sao chép mật khẩu
copy_button = Button(screen, text= "Copy", command= copy_password)
copy_button.place(x= 360, y= 115)

screen.mainloop()