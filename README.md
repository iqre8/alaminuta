# ALAMINUTA: AN USEFUL SYSADMIN TOOL
Alaminuta is a sysadmin kit written in python programming
language


__What can alaminuta do?__

Alaminuta can:

Manage processes with psutil

Manage packages with apt (only for debian-based systems)

Enable and disable UFW firewall

Clear thumbnail cache

Encrypt or Decrypt files

Get network information

Manage users


__How to install alaminuta?__

First, install dependencies:

On debian-based distros:
> sudo apt install ufw python3 python3-pip python-ufw python3-distutils-extra git

On fedora :
> dnf install ufw python3 python3-distutils-extrapython3-pip python-ufw git

CentOS/RHEL:
> yum install ufw python3python3-distutils-extra python3-pip python-ufw git

Arch linux:
>pacman -S ufw python3 python3-pip python3-distutils-extra python-ufw git

OpenSuse:
> zypper in ufw python3 python3-pip python3-distutils-extra python-ufw git

Clone this repository:

> git clone https://github.com/useranonymous/alaminuta

Install python dependencies with pip3:
> cd alaminuta; pip3 install -r requirements.txt

And run alaminuta as root:

> sudo ./almtconsole
