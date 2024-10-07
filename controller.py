import pygame
from pygame.locals import *
import requests

pygame.init()
pygame.joystick.init()

# Store the last command sent
last_command = {'pin': None, 'value': None}

def send_command(pin, value):
    global last_command
    # Check if the current command is the same as the last one
    if last_command['pin'] == pin and last_command['value'] == value:
        return  # Skip the request if it's the same as the last command
    
    # URL ของ Blynk API ที่จะทำการเรียก
    url = f'https://sgp1.blynk.cloud/external/api/update?token=ZRiWOcaUHqvET-v0i4KiSw-hwQBqIubT&{pin}={value}'

    try:
        # เรียก API ด้วย method GET
        response = requests.get(url)
        
        # ตรวจสอบสถานะการตอบกลับจาก API
        if response.status_code == 200:
            print(f"อัพเดตสำเร็จ: {pin} = {value}")
            # Update the last command
            last_command['pin'] = pin
            last_command['value'] = value
        else:
            print(f"เกิดข้อผิดพลาด: {response.status_code}")
    except Exception as e:
        print(f"ข้อผิดพลาดในการเชื่อมต่อ: {e}")

def stop_last_pin():
    # Set the last used pin to value 0
    if last_command['pin'] is not None:
        send_command(last_command['pin'], 0)
    else:
        print("ไม่มีคำสั่งล่าสุดให้หยุด")

# Initialize joysticks
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

clock = pygame.time.Clock()

while True:
    # Handle events, but no display or screen rendering
    for event in pygame.event.get():
        if event.type == JOYHATMOTION:
            # Print only the x, y values from the hat motion
            hat_x, hat_y = event.value
            print(f'Hat motion: x = {hat_x}, y = {hat_y}')
            if hat_y > 0:
                print('forward')
                send_command('v0', '1')
            elif hat_y < 0:
                print('backward')
                send_command('v1', '1')
            elif hat_x < 0:
                print('left')
                send_command('v2', '1')
            elif hat_x > 0:
                print('right')
                send_command('v3', '1')
            elif hat_x == 0 and hat_y == 0:
                print('stop')
                stop_last_pin()

    # No display, just handle input logic
    clock.tick(60)  # Control the frame rate without visual updates
