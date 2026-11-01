import machine
import time
import ustruct

class ST7735:
    def __init__(self, spi, tf_dc, tf_reset, tf_cs, width=128, height=160):
        self.spi = spi
        self.dc = machine.Pin(tf_dc, machine.Pin.OUT)
        self.rst = machine.Pin(tf_reset, machine.Pin.OUT)
        self.cs = machine.Pin(tf_cs, machine.Pin.OUT)
        self.width = width
        self.height = height

    def write_cmd(self, cmd):
        self.dc.value(0)
        self.cs.value(0)
        self.spi.write(b'%c' % cmd)
        self.cs.value(1)

    def write_data(self, data):
        self.dc.value(1)
        self.cs.value(0)
        self.spi.write(data)
        self.cs.value(1)

    def init(self):
        self.rst.value(1)
        time.sleep_ms(5)
        self.rst.value(0)
        time.sleep_ms(20)
        self.rst.value(1)
        time.sleep_ms(150)

        for cmd, delay, in [(0x11, 120), (0x3A, 0), (0x26, 0), (0x29, 0)]:
            self.write_cmd(cmd)
            if cmd == 0x3A: self.write_data(b'\x05') #16-bit color
            if cmd == 0x26: self.write_data(b'\x01')
            if delay: time.sleep_ms(delay)
        self.set_window(0, 0, self.width - 1, self.height - 1)

    def set_window(self, x0, y0, x1, y1):
        self.write_cmd(0x2A)
        self.write_data(ustruct.pack('>HH', x0, x1))
        self.write_cmd(0x2B)
        self.write_data(ustruct.pack('>HH', y0, y1))
        self.write_cmd(0x2C)

    def fill(self, color):
        self.set_window(0, 0, self.width -1, self.height - 1)
        pixel = ustruct.pack('>H', color)
        buffer = pixel * 256 #speed up by sending 256 pixels at a time
        self.dc.value(1)
        self.cs.value(0)
        for _ in range(self.width * self.height // 256):
            self.spi.write(buffer)
        self.cs.value(1)

    def fill_rect(self, x, y, w, h, color):
        self.set_window(x, y, x + w - 1, y + h - 1)
        pixel = ustruct.pack('>H', color)
        self.dc.value(1)
        self.cs.value(0)
        for _ in range(w * h):
            self.spi.write(pixel)
        self.cs.value(1)
    
