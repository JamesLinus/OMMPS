for p in psutil.process_iter():
...     print(p)
...
psutil.Process(pid=1, name='init')
psutil.Process(pid=2, name='kthreadd')
psutil.Process(pid=3, name='ksoftirqd/0')
...

def on_terminate(proc):
...     print("process {} terminated".format(proc))
...
# waits for multiple processes to terminate
gone, alive = psutil.wait_procs(procs_list, timeout=3, callback=on_terminate)