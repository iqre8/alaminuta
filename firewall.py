import easyufw.easyufw as ufw
def enable():
    ufw.enable()
    is_enabled = True
def allow(protocol):
    ufw.allow(protocol)
def deny(protocol):
    ufw.deny(protocol)
def delete(port):
    ufw.delete(port)
def disable():
    ufw.disable()
    is_enable = False
