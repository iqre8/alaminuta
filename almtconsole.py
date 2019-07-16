#!/usr/bin/env python3
#vim: set syntax=python
from pkg import install, remove
import os
from process import lst
from process import kill
import scriptsrc
import distro
from termcolor import cprint, colored
clear = lambda: os.system('clear')
import firewall

def defaultFirewall():
    firewall.enable()
    firewall.allow(22)
    firewall.allow(80)
    firewall.allow(443)
    firewall.allow(3306)
    firewall.allow(465)
    firewall.allow(587)
    firewall.allow(993)
    firewall.allow(995)

def showInitialLogo():
    print(colored(" __ _| |__ _ _ __ (_)_ _ _  _| |_ __ _ ", "yellow", attrs=['bold']))
    print(colored("/ _` | / _` | '  \| | ' \ || |  _/ _` |", "yellow", attrs=['bold']))
    print(colored("\__,_|_\__,_|_|_|_|_|_||_\_,_|\__\__,_|", "yellow", attrs=['bold']))    
def option():
    print(colored("Enter number of the operation you want:", "yellow", attrs=['bold']))
    cprint("[1] Process Management", "magenta")
    cprint("[2] Package management", "magenta")
    cprint("[3] Firewall management (UFW)", "magenta")
    cprint("[4] Clear thumbnail cache", "magenta")
    cprint("[5] Encrypt or Decrypt files", "magenta")
    cprint("[6] Get network information", "magenta")
    cprint("[7] User management", "magenta")
    cprint("[0] Exit alaminuta", "magenta")
def checkForUserOperationAndExecute():
    while True:
        option()
        userOperation = int(input("almf> "))
        if(userOperation == 1):
            clear()
            cprint("    [1] List processes", "magenta")
            cprint("    [2] Kill Process", "magenta")
            cprint("    [0] Return to main menu", "magenta")
            userSubOperation = int(input("almf> "))
            if(userSubOperation == 1):
                lst.listproc()
            if(userSubOperation == 2):
                pidtokill = int(input("PID of the process to kill: "))
                kill.kill(pidtokill)
            if(userSubOperation == 0):
                continue
        if(userOperation == 2):
            distro = distro.os_release_info()['id_like']
            if(distro == 'ubuntu' or distro == "debian"):
                clear()
                cprint("    [1] Install package", "magenta")
                cprint("    [2] Remove package", "magenta")
                cprint("    [3] Install essential packages", "magenta")
                cprint("    [0] Return to main menu", "magenta")
                userSubOperation = int(input("almf> "))
                if(userSubOperation == 1):
                    packagetoinstall = input("Package to install: ")
                    install.install(packagetoinstall)
                if(userSubOperation == 2):
                    packagetoremove = input("Package to remove: ")
                    remove.remove(packagetoremove)
                if(userSubOperation == 3):
                    scriptsrc.installEssential()
                if(userSubOperation == 0):
                    continue
            else:
                cprint("Your system doesn't support APT package manager!", "red")
                continue
        if(userOperation == 3):
            clear()
            cprint("    [1] Enable firewall (with default rules)", "magenta")
            cprint("    [2] Disable firewall", "magenta")
            cprint("    [0] Return to main menu", "magenta")
            userSubOperation = int(input("almf> "))
            if(userSubOperation == 1):
                defaultFirewall()
                cprint("Firewall started successfully", "green")
            if(userSubOperation == 2):
                firewall.disable()
                cprint("Firewall disabled successfully", "green")
            if(userSubOperation == 0):
                continue
        if(userOperation == 4):
            clear()
            scriptsrc.cleanCache()
            cprint("Thumbnail cache cleaned successfully", "green")
        if(userOperation == 5):
            clear()
            cprint("    [1] Encrypt", "magenta")
            cprint("    [2] Decrypt", "magenta")
            cprint("    [0] Return to main menu", "magenta")
            userSubOperation = int(input("almf> "))
            if(userSubOperation == 1):
                clear()
                inputf = input("Enter the input file path: ")
                outputf = input("Enter the output file path: ")
                scriptsrc.encrypt(inputf, outputf)
            if(userSubOperation == 2):
                clear()
                inputf = input("Enter the input file path: ")
                outputf = input("Enter the output file path: ")
                scriptsrc.decrypt(inputf, outputf)
            if(userSubOperation == 0):
                continue
        if(userOperation == 6):
            cprint("    [1] Get WAN IP", "magenta")
            cprint("    [2] Get LAN IP(s)", "magenta")
            cprint("    [3] Get router IP", "magenta")
            cprint("    [4] Get DNS Nameserver", "magenta")
            cprint("    [5] Get MAC Address for interface", "magenta")
            cprint("    [6] Get current IP Geodata", "magenta")
            cprint("    [0] Return to main menu", "magenta")
            userSubOperation = int(input("almf> "))
            if(userSubOperation == 1):
                scriptsrc.wanIp()
            if(userSubOperation == 2):
                scriptsrc.lanIp()
            if(userSubOperation == 3):
                scriptsrc.routerIp()
            if(userSubOperation == 4):
                scriptsrc.dnsNameserver()
            if(userSubOperation == 5):
                iface = input("Interface: ")
                scriptsrc.macAddress(iface)
            if(userSubOperation == 6):
                scriptsrc.ipGeodata()
            if(userSubOperation == 0):
                continue
        if(userOperation == 7):
            clear() 
            cprint("    [1] Create new user", "magenta")
            cprint("    [2] Delete user", "magenta")
            cprint("    [3] Set root password", "magenta")
            cprint("    [0] Return to main menu", "magenta")
            userSubOperation = int(input("almf> "))
            if(userSubOperation == 1):
                newusername = input("Name of the new user: ")
                scriptsrc.adduser(newusername)
            if(userSubOperation == 2):
                usertodel = input("Name of the user to delete: ")
                scriptsrc.deluser(usertodel)
            if(userSubOperation == 3):
                scriptsrc.rootpasswd()
            if(userSubOperation == 0):
                continue

        if(userOperation == 0):
            break
def main():
    showInitialLogo()
    checkForUserOperationAndExecute()

if __name__ == "__main__":
    main()