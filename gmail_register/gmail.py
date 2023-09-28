import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random
import pyautogui
import string

# Tạo một tên có 4 chữ cái ngẫu nhiên
random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(4))

# Tạo 4 chữ số ngẫu nhiên
random_numbers = ''.join(random.choice(string.digits) for _ in range(4))

#nối lại
random_result = random_letters + random_numbers

#tạo mật khẩu 12 kí tự
random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

# Chọn một ngày ngẫu nhiên từ 1 - 28
random_day = random.randint(1, 28)

# Tạo một số ngẫu nhiên từ 1 đến 12 để đại diện cho tháng
random_month = random.randint(1, 12)
# Chuyển đổi số tháng thành tên tháng
month_names = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
selected_month_name = month_names[random_month]

# Chọn một năm ngẫu nhiên từ 1990 đến 2002
random_year = random.randint(1990, 2002)

# Chọn giới tính ngẫu nhiên
random_sex = random.randint(1, 2)

#để chrome ko tự tắt sau khi code đã đc chạy
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

browser.get('https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp')
browser.maximize_window()

action = ActionChains(browser)

browser.find_element(By.NAME, 'firstName').send_keys(random_letters)
browser.find_element(By.ID, 'collectNameNext').click()

time.sleep(2)
browser.find_element(By.NAME, 'day').send_keys(str(random_day))

time.sleep(2)
browser.find_element(By.NAME, 'year').send_keys(str(random_year))

time.sleep(2)
month = browser.find_element(By.CSS_SELECTOR, '#month')
selectMonth = Select(month)
selectMonth.select_by_index(random_month)

time.sleep(2)
sex = browser.find_element(By.ID, 'gender')
selectSex = Select(sex)
selectSex.select_by_index(random_sex)

browser.find_element(By.ID, 'birthdaygenderNext').click()

time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '#selectionc2').click()

time.sleep(2)
browser.find_element(By.NAME, 'Username').send_keys(random_result)

time.sleep(2)
browser.find_element(By.CSS_SELECTOR, '#next > div > button > span').click()

time.sleep(2)
browser.find_element(By.NAME, 'Passwd').send_keys(random_password)
time.sleep(2)
browser.find_element(By.NAME, 'PasswdAgain').send_keys(random_password)

time.sleep(1)
browser.find_element(By.CSS_SELECTOR, '#createpasswordNext > div > button > span').click()

print(random_result)
print(random_password)

#mousePosition = pyautogui.displayMousePosition()