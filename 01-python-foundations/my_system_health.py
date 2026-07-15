## Practice
# 
# Write your own `system_health.py` from scratch:
# 
# 1. Ask the user for a CPU threshold with `input()` and cast it to a number.
# 2. Read current CPU usage with `psutil.cpu_percent(interval=1)`.
# 3. Print whether the CPU is healthy or over the threshold.
# 4. Bonus: also check memory (`psutil.virtual_memory().percent`) and disk
#    (`psutil.disk_usage("/").percent`).
# 5. Bonus: wrap the input in `try / except ValueError` so bad input doesn't crash it.

import psutil

try:
    cpu_threshold = int(input("What is the threshold: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

current_cpu = psutil.cpu_percent(interval=1)
current_memory = psutil.virtual_memory().percent
current_disk = psutil.disk_usage("/").percent

def check_cpu():
    if current_cpu > cpu_threshold:
        print("High CPU Alert, current CPU usage is: ", current_cpu)
    else:  
        print("CPU is in safe limit, current CPU usage is: ", current_cpu)

def check_memory():
    if current_memory > 80:  # Example threshold for memory
        print("High Memory Alert, current memory usage is: ", current_memory)
    else:
        print("Memory is in safe limit, current memory usage is: ", current_memory)

def check_disk():
    if current_disk > 80:  # Example threshold for disk
        print("High Disk Alert, current disk usage is: ", current_disk)
    else:
        print("Disk is in safe limit, current disk usage is: ", current_disk)

check_cpu()
check_memory()
check_disk()

# output:
# PS C:\Workspace\repos\python-for-devops\01-python-foundations> python .\my_system_health.py
# What is the threshold: 1
# High CPU Alert, current CPU usage is:  2.2
# Memory is in safe limit, current memory usage is:  34.6
# Disk is in safe limit, current disk usage is:  7.2