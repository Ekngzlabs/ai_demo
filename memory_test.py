# Demonstrates deliberate RAM allocation and measurement
 
import psutil
import time
 
def ram_used_gb():
    return psutil.virtual_memory().used / 1e9
 
print(f'RAM in use before allocation : {ram_used_gb():.2f} GB')
 
# Allocate a list of 100 million integers
# Python interns the integer 0, so only one integer object exists. 
# Memory cost is 100 million 8-byte pointers in the list structure. 
# Total: ~800 MB of RAM
 
# print(f'RAM in use after allocation  : {ram_used_gb():.2f} GB')

before = ram_used_gb()
large_list = [0] * 100_000_000

after = ram_used_gb()

print(f'RAM in use after allocation  : {after:.2f} GB')
print(f'Change: +{after - before:.2f} GB')
 
input('RAM is allocated. Open Task Manager now and observe. Press Enter to free memory.')
 
# Deleting the variable tells Python's garbage collector to free the memory
del large_list
import gc
gc.collect()   # force immediate garbage collection
 
print(f'RAM in use after deletion    : {ram_used_gb():.2f} GB')
print('Memory freed successfully.')
