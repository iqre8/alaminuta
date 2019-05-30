#ALAMINUTA: AN USEFUL SYSADMIN TOOL
Alaminuta is a sysadmin kit written in python programming
language


**But, what can alaminuta do?**

Alaminuta can:

Mnage processes with psutil

Manage packages with apt (only for debian-based systems)

Enable and disable UFW firewall

Clear thumbnail cache

Encrypt or Decrypt files

Get network information

Manage users


**How to install alaminuta?**

First, install dependencies:

On debian-based distros:
> sudo apt install ufw python3 python3-pip python-ufw git

On fedora :
> dnf install ufw python3 python3-pip python-ufw git

CentOS/RHEL:
> yum install ufw python3 python3-pip python-ufw git

Arch linux:
>pacman -S ufw python3 python3-pip python-ufw git

OpenSuse:
> zypper in ufw python3 python3-pip python-ufw git

Clone this repository:

> git clone https://github.com/useranonymous/alaminuta

Install python dependencies with pip3:
> cd alaminuta; pip3 install -r requirements.txt

And run alaminuta as root:

> sudo ./almtconsole
