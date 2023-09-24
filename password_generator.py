import random
import string

'''
password_len = int(input("Nhập độ dài mật khẩu: "))
required_digits = 2  # Số lượng ký tự số yêu cầu
my_password = ''

# Tạo mật khẩu ban đầu chỉ bằng chữ cái
for i in range(password_len - required_digits):
    my_password += random.choice(string.ascii_letters)
    
# Thêm ít nhất 2 ký tự số vào mật khẩu ban đầu
digits = "".join(random.choice(string.digits) for _ in range(required_digits))
final_password = my_password + digits

# Trộn mật khẩu cuối cùng để đảm bảo tính ngẫu nhiên
final_password = ''.join(random.sample(final_password, len(final_password)))

print("Mật khẩu mới của bạn: ", final_password)
'''


#hoặc dùng đoạn code này cũng ok
password_len = int(input("Nhập độ dài mật khẩu: "))
my_password = ''

# Tạo mật khẩu chỉ bằng chữ cái và số
for i in range(password_len):
    my_password += random.choice(string.ascii_letters + string.digits)

print("Mật khẩu mới của bạn:", my_password)
