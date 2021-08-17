import time
import subprocess

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106, ssd1306
from PIL import ImageFont, ImageDraw, Image

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)


#oled_font = ImageFont.truetype("DejaVuSerif.ttf", 14)
oled_font = ImageFont.load_default()

while True:

    cmd = "hostname -I | cut -d\' \' -f1 | awk '{printf \"IP: %s\", $0}'"
    IP = subprocess.check_output(cmd, shell=True)
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True)
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell=True)
    cmd = "awk '{printf \"Temp: %3.1fC\", $1/1000}' /sys/class/thermal/thermal_zone0/temp"
    Temp = subprocess.check_output(cmd, shell=True)
    cmd = "grep eth0 /proc/net/dev | awk '{printf \"RX/TX: %.2f/%.2f MB/s\",($2/1000000),($10/1000000)}'"
    Network = subprocess.check_output(cmd, shell=True)

    with canvas(device, dither=True) as draw:
        #draw.rectangle(device.bounding_box, outline = "white", fill = "black")
        draw.text((0, 0),  IP, font=oled_font, fill="white")
        draw.text((0, 10), CPU, font=oled_font, fill="white")
        draw.text((0, 20), MemUsage, font=oled_font, fill="white")
        draw.text((0, 30), Disk, font=oled_font, fill="white")
        draw.text((0, 40), Temp, font=oled_font, fill="white")
        draw.text((0, 50), Network, font=oled_font, fill="white")

    time.sleep(.1)
