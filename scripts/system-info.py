#!/usr/bin/env python3

import datetime
import os
import psutil
import time

status_text = str()

default_color = '#[bg=default]#[fg=default]'

# ----------------------------------------------------------------
# uptime
# ----------------------------------------------------------------

n = int(time.time() - psutil.boot_time())
day = n // (24 * 3600)
n %= (24 * 3600)
hour = n // 3600
n %= 3600
minute = n // 60

text = '{} #[bg=white]#[fg=black]'.format(default_color)
if day > 0:
    text += '{}d{},'.format(day, '!' if day >= 100 else '')
text += '{}h{}m'.format(hour, minute)
text += default_color

status_text += text

# ----------------------------------------------------------------
# cpu and mem info
# ----------------------------------------------------------------

cpu_p = psutil.cpu_percent(interval=1)

mem = psutil.virtual_memory()
mem_p = mem.used / mem.total * 100

if cpu_p > 80:
    cpu_color = '#[bg=red]#[fg=white]'
elif cpu_p > 30:
    cpu_color = '#[bg=yellow]#[fg=black]'
else:
    cpu_color = '#[bg=black]#[fg=blue]'

if mem_p > 80:
    mem_color = '#[bg=red]#[fg=white]'
elif mem_p > 30:
    mem_color = '#[bg=yellow]#[fg=black]'
else:
    mem_color = '#[bg=black]#[fg=blue]'

status_text += '{} {}{}% {:.1f}Gx{}{} {}{:.1f}G {:.2f}%{}'.format(
    default_color,
    cpu_color,
    cpu_p, psutil.cpu_freq().current / 1000, psutil.cpu_count(),
    default_color,
    mem_color,
    mem.total / 1000000000, mem_p,
    default_color)

# ----------------------------------------------------------------
# ip address
# ----------------------------------------------------------------

status_text += '{} #[bg=white]#[fg=black]{}{}'.format(
    default_color,
    os.environ['SSH_CONNECTION'].split()[2],
    default_color)

# ----------------------------------------------------------------
# time
# ----------------------------------------------------------------

status_text += '{} #[bg=black]#[fg=white]{}'.format(
    default_color,
    datetime.datetime.now().strftime('%Y-%m-%d %a %H:%M %Z'))

print(status_text)