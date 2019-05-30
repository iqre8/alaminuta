import psutil
def listproc():
    print("PID        NAME")
    for pid in psutil.pids():
        proc = psutil.Process(pid)
        print("{0}        {1}".format(pid, proc.name()))
