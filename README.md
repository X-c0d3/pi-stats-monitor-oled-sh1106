### Chia Hpool Checker

![Hpool Checker](https://github.com/X-c0d3/pi-stats-monitor-oled-sh1106/main/screenshot/IMG_20210816_231547.jpg)

```
Login to Raspberry Pi
# sudo raspi-config and Enable I2C


Optionally, to improve performance, increase the I2C baudrate from the default of 100KHz to 400KHz by altering /boot/config.txt to include:

vim /boot/config.txt
dtparam=i2c_arm=on,i2c_baudrate=400000

$ sudo apt-get install i2c-tools

$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y
$ sudo -H pip3 install luma.oled

Ref : https://luma-oled.readthedocs.io/en/latest/
```
