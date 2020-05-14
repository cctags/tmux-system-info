#!/usr/bin/env python3

import datetime
import os
import sys
import time

try:
    import psutil
except ImportError as e:
    print('PLUGIN ERROR: {}'.format(e.msg))
    sys.exit(0)

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

if cpu_p > 80:
    cpu_color = '#[bg=red]#[fg=white]'
elif cpu_p > 30:
    cpu_color = '#[bg=yellow]#[fg=black]'
else:
    cpu_color = '#[bg=green]#[fg=white]'

if mem.percent > 80:
    mem_color = '#[bg=red]#[fg=white]'
elif mem.percent > 30:
    mem_color = '#[bg=yellow]#[fg=black]'
else:
    mem_color = '#[bg=green]#[fg=white]'

status_text += '{} {}{:.1f}Gx{} {}%{} {}{:.1f}G {:.1f}%{}'.format(
    default_color,
    cpu_color,
    psutil.cpu_freq().current / 1000, psutil.cpu_count(), cpu_p,
    default_color,
    mem_color,
    mem.total / 1000000000, mem.percent,
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
