# RASPBERRYPI 1
[![N|Solid](https://www.raspberrypi.org/wp-content/uploads/2011/10/Raspi-PGB001.png)](https://www.raspberrypi.org)
## Features
## Initial Setup
### Connection
Enable SSH and VNC
### Resolution
Change reolution to 1080p
```sh
$ xrandr --output HDMI-1 --mode 1920x1080
```
### Mount Drive
Mounting drive is required to give a permanent name to the external drive for plex
```sh
$ sudo mkdir -p /mnt/extd1
$ sudo chown -R pi:pi /mnt/extd1
$ sudo blkid /dev/sda1
```
From the result from above blkd command replace UUID value with [UUID] and TYPE value with [TYPE] and copy it to the end of fstab file
UUID=[UUID] /mnt/usb1 [TYPE] defaults,auto,users,rw,nofail,noatime 0 0
```sh
$ sudo nano /etc/fstab
$ sudo umount /dev/sda1
$ sudo mount -a
$ sudo reboot
```
### Docker
Youc an choose to install it using IOTStack tools later
Install Docker (https://www.docker.com/blog/happy-pi-day-docker-raspberry-pi/)
```sh
$ sudo apt-get install apt-transport-https ca-certificates software-properties-common -y
$ curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
$ sudo usermod -aG docker pi
$ sudo curl https://download.docker.com/linux/raspbian/gpg
$ vim /etc/apt/sources.list
$ deb https://download.docker.com/linux/raspbian/ stretch stable
$ sudo apt-get update
$ sudo apt-get upgrade
$ systemctl start docker.service
$ docker info
```
### Required Containers
Git Clone from https://github.com/gcgarner/IOTstack.git
```sh
$ git clone https://github.com/gcgarner/IOTstack.git
$ cd ~/IOTstack
$ ./menu.sh
```
Select required services
- Install Docker
- Build Stack
    - portainer
    - openhab
    - pihole
    - plex
    - homebridge
    - qbittorrent
- Miscellaneous commands
    - Disable swap by setting swappiness to 0
    - Install log2ram to decrease load on sd card, moves /var/log into ram
### Update docker-compose.yml
Update docker-compose.yml to use volumes in root directory, replace ./volumes with /volumes
Also un comment lines for plex UMASK_SET, uncomment and replace ./mnt to /mnt and provide appropriate values
    - /mnt/extd1/TV Shows:/tv
    - /mnt/extd1/Movies:/movies
    - /mnt/extd1/Music:/music
Then run
```sh
$ docker-compose up -d
```
### Ports
- portainer: 9000
- openhab: 8080
- pihole: 8089
- plex: 32400
- homebridge: 8080
- qbittorrent: 15080
