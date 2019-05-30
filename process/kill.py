import psutil
def kill(pid):
    proc = psutil.Process(pid)
    proc.terminate()
