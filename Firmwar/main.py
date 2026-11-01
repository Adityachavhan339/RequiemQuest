import machine
import time
from machine import Pin, SPI
import st7735

#Button Inputs

btn_up = Pin(0, Pin.IN, Pin.PULL_UP)
btn_left = Pin(1, Pin.IN, Pin.PULL_UP)
btn_right = Pin(2, Pin.IN, Pin.PULL_UP)
btn_down = Pin(3, Pin.IN, Pin.PULL_UP)
btn_act = Pin(4, Pin.IN, Pin.PULL_UP)

#Sound
buzzer = machine.PWM(Pin(15))
buzzer.duty_u16(0) #start with sound off

#Display
spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
display = st7735.ST7735(spi, tf_dc=16, tf_reset=20, tf_cs=17, width=128, height=160)
display.init()

#Color Definitions
BLACK = 0x0000
GREEN = 0x07E0
RED = 0xF800
WHITE = 0xFFFF

display.fill(BLACK)

#Audio
def play_tone(frequency, duration_ms):
    if frequency == 0:
        buzzer.duty_u16(0)
    else:
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)
    time.sleep_ms(duration_ms)
    buzzer.duty_u16(0) #Sound OFF


#Game
game_running = True
player_x = 64
player_y = 100

print("RequiemQuest Game Loaded")
play_tone(880, 150) #Sound to indicate game start

while game_running:
    #Check button presses
    if not btn_up.value():
        player_y -= 2
        play_tone(440, 20)
    if not btn_down.value():
        player_y += 2
        play_tone(440, 20)
    if not btn_left.value():
        player_x -= 2
        play_tone(440, 20)
    if not btn_right.value():
        player_x += 2
        play_tone(440, 20)
    if not btn_act.value():
        display.fill(RED)
        play_tone(220, 100)


    #Keep Player Within Screen Limits
    player_x = max(4, min(player_x, 120))
    player_y = max(4, min(player_y, 152))

    display.fill_rect(player_x, player_y, 8, 8, GREEN)

    time.sleep_ms(33) # ~30FPS

