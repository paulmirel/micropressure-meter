import board
import time
import busio
import adafruit_mprls

import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_sh1107
displayio.release_displays()
# oled_reset = board.D9

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

mpr_sensor = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle in black
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw some label text
text1 = "Detector Chamber"  
text_area = label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=8, y=8)
splash.append(text_area)
text2 = "Gage Pressure"
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF, x=8, y=18)
splash.append(text_area2)

text3 = "No Reading"
text_area3 = label.Label(terminalio.FONT, text=text3, scale=2, color=0xFFFFFF, x=9, y=44)
splash.append(text_area3)

while True:
    pressure_mbar = mpr_sensor.pressure
    print( pressure_mbar ) 
    time.sleep(0.5)
    if False: 
        time.sleep(1)
        text3 = "                        "
        text_area3 = label.Label(terminalio.FONT, text=text3, scale=2, color=0xFFFFFF, x=9, y=44)
        splash.append(text_area3)
        time.sleep(1)
        text3 = "SH1107"
        text_area3 = label.Label(terminalio.FONT, text=text3, scale=2, color=0xFFFFFF, x=9, y=44)
        splash.append(text_area3)