import psutil
psutil.pids()
[1, 2, 3, 4, 5, 6, 7, 46, 48, 50, 51, 178, 182, 222, 223, 224, 268, 1215, 1216, 1220, 1221, 1243, 1244,
 1301, 1601, 2237, 2355, 2637, 2774, 3932, 4176, 4177, 4185, 4187, 4189, 4225, 4243, 4245, 4263, 4282,
 4306, 4311, 4312, 4313, 4314, 4337, 4339, 4357, 4358, 4363, 4383, 4395, 4408, 4433, 4443, 4445, 4446,
 5167, 5234, 5235, 5252, 5318, 5424, 5644, 6987, 7054, 7055, 7071]

p = psutil.Process(7055)
p.name()
'python'
p.exe()
'/usr/bin/python'
p.cwd()
'/home/giampaolo'
p.cmdline()
['/usr/bin/python', 'main.py']

p.pid
7055
p.ppid()
7054
p.parent()
<psutil.Process(pid=7054, name='bash') at 140008329539408>
p.children()
[<psutil.Process(pid=8031, name='python') at 14020832451977>,
 <psutil.Process(pid=8044, name='python') at 19229444921932>]

p.status()
'running'
p.username()
'giampaolo'
p.create_time()
1267551141.5019531
p.terminal()
'/dev/pts/0'

p.uids()
puids(real=1000, effective=1000, saved=1000)
p.gids()
pgids(real=1000, effective=1000, saved=1000)

p.cpu_times()
pcputimes(user=1.02, system=0.31, children_user=0.32, children_system=0.1)
p.cpu_percent(interval=1.0)
12.1
p.cpu_affinity()
[0, 1, 2, 3]
p.cpu_affinity([0, 1])  # set
p.cpu_num()
1

p.memory_info()
pmem(rss=10915840, vms=67608576, shared=3313664, text=2310144, lib=0, data=7262208, dirty=0)
p.memory_full_info()  # "real" USS memory usage (Linux, OSX, Win only)
pfullmem(rss=10199040, vms=52133888, shared=3887104, text=2867200, lib=0, data=5967872, dirty=0, uss=6545408, pss=6872064, swap=0)
p.memory_percent()
0.7823
p.memory_maps()
[pmmap_grouped(path='/lib/x8664-linux-gnu/libutil-2.15.so', rss=32768, size=2125824, pss=32768, shared_clean=0, shared_dirty=0, private_clean=20480, private_dirty=12288, referenced=32768, anonymous=12288, swap=0),
 pmmap_grouped(path='/lib/x8664-linux-gnu/libc-2.15.so', rss=3821568, size=3842048, pss=3821568, shared_clean=0, shared_dirty=0, private_clean=0, private_dirty=3821568, referenced=3575808, anonymous=3821568, swap=0),
 pmmap_grouped(path='/lib/x8664-linux-gnu/libcrypto.so.0.1', rss=34124, rss=32768, size=2134016, pss=15360, shared_clean=24576, shared_dirty=0, private_clean=0, private_dirty=8192, referenced=24576, anonymous=8192, swap=0),
 pmmap_grouped(path='[heap]',  rss=32768, size=139264, pss=32768, shared_clean=0, shared_dirty=0, private_clean=0, private_dirty=32768, referenced=32768, anonymous=32768, swap=0),
 pmmap_grouped(path='[stack]', rss=2465792, size=2494464, pss=2465792, shared_clean=0, shared_dirty=0, private_clean=0, private_dirty=2465792, referenced=2277376, anonymous=2465792, swap=0),
 ...]

p.io_counters()
pio(read_count=478001, write_count=59371, read_bytes=700416, write_bytes=69632, read_chars=456232, write_chars=517543)

p.open_files()
[popenfile(path='/home/giampaolo/svn/psutil/setup.py', fd=3, position=0, mode='r', flags=32768),
 popenfile(path='/var/log/monitd', fd=4, position=235542, mode='a', flags=33793)]

p.connections()
[pconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 48776), raddr=('93.186.135.91', 80), status='ESTABLISHED'),
 pconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 43761), raddr=('72.14.234.100', 80), status='CLOSING'),
 pconn(fd=119, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 60759), raddr=('72.14.234.104', 80), status='ESTABLISHED'),
 pconn(fd=123, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=('10.0.0.1', 51314), raddr=('72.14.234.83', 443), status='SYN_SENT')]

p.num_threads()
4
p.num_fds()
8
p.threads()
[pthread(id=5234, user_time=22.5, system_time=9.2891),
 pthread(id=5235, user_time=0.0, system_time=0.0),
 pthread(id=5236, user_time=0.0, system_time=0.0),
 pthread(id=5237, user_time=0.0707, system_time=1.1)]

p.num_ctx_switches()
pctxsw(voluntary=78, involuntary=19)

p.nice()
0
p.nice(10)  # set

p.ionice(psutil.IOPRIO_CLASS_IDLE)  # IO priority (Win and Linux only)
p.ionice()
pionice(ioclass=<IOPriority.IOPRIO_CLASS_IDLE: 3>, value=0)

p.rlimit(psutil.RLIMIT_NOFILE, (5, 5))  # set resource limits (Linux only)
p.rlimit(psutil.RLIMIT_NOFILE)
(5, 5)

p.environ()
{'LC_PAPER': 'it_IT.UTF-8', 'SHELL': '/bin/bash', 'GREP_OPTIONS': '--color=auto',
'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg', 'COLORTERM': 'gnome-terminal',
 ...}

p.as_dict()
{'status': 'running', 'num_ctx_switches': pctxsw(voluntary=63, involuntary=1), 'pid': 5457, ...}
p.is_running()
True
p.suspend()
p.resume()

p.terminate()
p.wait(timeout=3)
0

psutil.test()
USER         PID %CPU %MEM     VSZ     RSS TTY        START    TIME  COMMAND
root           1  0.0  0.0   24584    2240            Jun17   00:00  init
root           2  0.0  0.0       0       0            Jun17   00:00  kthreadd
root           3  0.0  0.0       0       0            Jun17   00:05  ksoftirqd/0

giampaolo  31475  0.0  0.0   20760    3024 /dev/pts/0 Jun19   00:00  python2.4
giampaolo  31721  0.0  2.2  773060  181896            00:04   10:30  chrome
root       31763  0.0  0.0       0       0            00:05   00:00  kworker/0:1