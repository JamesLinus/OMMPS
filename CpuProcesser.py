#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C)  2015 By JamesLinus.  All rights reserved.

@author : JamesLinus (Email: www.1464217939@outlook.com)
@version: 1.0
@created: 2017-05-01
'''

import matplotlib.pyplot as plt
import psutil as ps
import os
import time
import random
import collections
import argparse

class ProcessMonitor(object):
    def __init__(self, key_name, fields, duration, interval):
        self.key_name = key_name
        self.fields = fields
        self.duration = float(duration)
        self.inveral = float(interval)

        self.CPU_COUNT = ps.cpu_count()
        self.MEM_TOTAL = ps.virtual_memory().total / (1024 * 1024)
        self.procinfo_dict = collections.defaultdict(dict)


    def _get_proc_info(self, pid):
        try:
            proc = ps.Process(pid)
            name = proc.name()
            # If not contains the key word, return None
            if name.find(self.key_name) == -1:
                return None
            pinfo = {
                    "name": name,
                    "pid" : pid,
                    }
            # If the field is correct, add it to the process information dictionary.
            for field in self.fields:
                if hasattr(proc, field):
                    if field == "cpu_percent":
                        pinfo[field] = getattr(proc, field)(interval = 0.1) / self.CPU_COUNT
                    elif field == "memory_percent":
                        pinfo[field] = getattr(proc, field)() * self.MEM_TOTAL / 100
                    else:
                        pinfo[field] = getattr(proc, field)()
            if pid not in self.procinfo_dict:
                self.procinfo_dict[pid] = collections.defaultdict(list)
                self.procinfo_dict[pid]["name"] = name
            for field in self.fields:
                self.procinfo_dict[pid][field].append(pinfo.get(field, 0))
            print(pinfo)
            return pinfo
        except:
            pass
        return None

    def monitor_processes(self):
        start = time.time()
        while time.time() - start < self.duration:
            try:
                pids = ps.pids()
                for pid in pids:
                    self._get_proc_info(pid)
            except KeyboardInterrupt:
                print("Killed by user keyboard interrupted!")
                return

    def _get_color(self):
        color = "#"
        for i in range(3):
            a = hex(random.randint(0, 255))[2:]
            if len(a) == 1:
                a = "0" + a
            color += a
        return color.upper()

    def draw_figure(self, field, pdf):
        # Draw each pid line
        for pid in self.procinfo_dict:
            x = range(len(self.procinfo_dict[pid][field]))
            #print x, self.procinfo_dict[pid][field]
            plt.plot(x, self.procinfo_dict[pid][field], label = "pid" + str(pid), color = self._get_color())
        plt.xlabel(time.strftime("%Y-%m-%d %H:%M:%S"))
        plt.ylabel(field.upper())
        plt.title(field + " Figure")
        plt.legend(loc = "upper left")
        plt.grid(True)
        plt.savefig(pdf, dpi = 200)
        plt.show()

def Main():
    parser = argparse.ArgumentParser(description='Monitor process CPU and Memory.')
    parser.add_argument("-k", dest='key', type=str, default="producer", 
                   help='the key word of the processes to be monitored(default is "producer")')
    parser.add_argument("-d", dest='duration', type=int, default=60,
                   help='duration of the monitor to run(unit: seconds, default is 60)')
    parser.add_argument('-i', dest='interval', type=float, default=1.0,
                   help='interval of the sample(unit: seconds, default is 1.0)')
    args = parser.parse_args()
    fields = ["cpu_percent", "memory_percent"]
    #print args.key, args.duration, args.interval
    pm = ProcessMonitor(args.key, fields, args.duration, args.interval)
    pm.monitor_processes()
    pm.draw_figure("cpu_percent", "cpu.pdf")
    pm.draw_figure("memory_percent", "mem.pdf")


if __name__ == "__main__":
    Main()