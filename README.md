### Pi Stats with OLED SD1106

![Pi Stats OLED SD1106](https://raw.githubusercontent.com/X-c0d3/pi-stats-monitor-oled-sh1106/main/screenshot/IMG_20210816_231547.jpg)

```
Login to Raspberry Pi and Enable I2C with raspi-config command
# sudo raspi-config => Interfacing Options => I2C

Optionally, to improve performance
increase the I2C baudrate from the default of 100KHz to 400KHz by altering /boot/config.txt to include:
$ vim /boot/config.txt
dtparam=i2c_arm=on,i2c_baudrate=400000

$ sudo apt-get install i2c-tools

$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y
$ sudo -H pip3 install luma.oled

Ref : https://luma-oled.readthedocs.io/en/latest/

```

![Pi Stats OLED SD1106 - 2](https://raw.githubusercontent.com/X-c0d3/pi-stats-monitor-oled-sh1106/main/screenshot/IMG_20210815_202546.jpg)

![Pi Stats OLED SD1106 - 3](https://raw.githubusercontent.com/X-c0d3/pi-stats-monitor-oled-sh1106/main/screenshot/IMG_20210816_231758.jpg)
