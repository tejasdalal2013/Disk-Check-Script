#!/usr/bin/env python3

import shutil
import sys
import os

def check_reboot():
    """Returns True If the computer has a Pending reboot."""
    return os.path.exists("/run/reboot-required")


def check_disk_usage(disk,min_gb, min_percent):

    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabyte_free = du.free / 2**30

    if percent_free <min_gb or gigabyte_free < min_percent:
        return True
    return False

def check_root_full():
    """Return True if the partion is full,False otherwisw."""
    return check_disk_usage(disk="/", min_gb=2, min_percent= 10)


def main():
    checks=[
        (check_reboot, "pending Reboot"),
        (check_root_full, "Root Partion is Full"),
    ]
    Everthing_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            Everthing_ok = False
        if not Everthing_ok:
            sys.exit(1)
    if check_reboot():
        print("reboot Pending.")
        sys.exit(1)
    if check_root_full():
        print("Root Is full.?")
        sys.exit(1)

    print("Everthing Ok..?")
    sys.exit(0)

main()