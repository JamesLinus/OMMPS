import psutil

psutil.disk_partitions()

[sdiskpart(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,nosuid'),
 sdiskpart(device='/dev/sda2', mountpoint='/home', fstype='ext, opts='rw')]

psutil.disk_usage('/')

sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)

psutil.disk_io_counters(perdisk=False)

sdiskio(read_count=719566, write_count=1082197, read_bytes=18626220032, 

write_bytes=24081764352, read_time=5023392, write_time=63199568, 

read_merged_count=619166, write_merged_count=812396, busy_time=4523412)