from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открываем браузер
browser = webdriver.Edge()

# Переходим на страницу авторизации Twitch
browser.get('https://www.twitch.tv/login')

# Ждем, чтобы страница загрузилась полностью
time.sleep(3)

# Находим поле для ввода имени пользователя
username_field = browser.find_element(By.ID, 'login-username')

# Вводим имя пользователя
username_field.send_keys('ivan100055')

# Находим поле для ввода пароля
password_field = browser.find_element(By.ID, 'password-input')

# Вводим пароль
password_field.send_keys('47c-yth-Hwe-Cfi')

# Нажимаем клавишу Enter для отправки формы (вместо кнопки "Войти")
password_field.send_keys(Keys.ENTER)

# Ждем несколько секунд, чтобы браузер успел обработать запрос
time.sleep(5)

# Находим и кликаем на первый стрим
stream_element = browser.find_element(By.CSS_SELECTOR, 'a[data-a-target="preview-card-image-link"]')
stream_element.click()

# Ждем, чтобы стрим загрузился
time.sleep(5)

# Находим поле ввода чата
chat_input = browser.find_element(By.CSS_SELECTOR, 'textarea[data-a-target="chat-input"]')

# Вводим сообщение в чат
chat_input.send_keys('Hello world!!')

# Нажимаем Enter для отправки сообщения
chat_input.send_keys(Keys.RETURN)

# Ждем некоторое время, чтобы сообщение было отправлено
time.sleep(3)

# Закрываем браузер после выполнения всех действий
browser.quit()
