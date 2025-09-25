"""
system_info.py - Display system information and check user permissions
"""

import os
import platform
import getpass
import psutil

def system_info():
    print("=======================")
    print("   SYSTEM INFORMATION")
    print("=======================")
    
    # Hostname and OS info
    print(f"Hostname: {platform.node()}")
    print(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Kernel: {platform.release()}")
    
    # Uptime (in seconds)
    uptime_seconds = int(psutil.boot_time())
    from datetime import datetime
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    print(f"Boot Time: {boot_time}")
    
    # CPU info
    print(f"CPU: {platform.processor()} | Cores: {psutil.cpu_count(logical=True)}")
    
    # Memory info
    mem = psutil.virtual_memory()
    print(f"Memory: {round(mem.total/1e9,2)} GB total, "
          f"{round(mem.used/1e9,2)} GB used, "
          f"{round(mem.available/1e9,2)} GB available")
    
    # Disk info
    disk = psutil.disk_usage('/')
    print(f"Disk: {round(disk.total/1e9,2)} GB total, "
          f"{round(disk.used/1e9,2)} GB used, "
          f"{round(disk.free/1e9,2)} GB free")

def user_permissions():
    print("\n=======================")
    print("   USER PERMISSIONS")
    print("=======================")
    
    user = getpass.getuser()
    print(f"Current user: {user}")
    
    # Check for admin/root rights
    if os.name == "nt":  # Windows
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            is_admin = False
        print("Admin privileges: " + ("✅ Yes" if is_admin else "❌ No"))
    else:  # Linux/macOS
        is_root = (os.geteuid() == 0)
        print("Root privileges: " + ("✅ Yes" if is_root else "❌ No"))

if __name__ == "__main__":
    system_info()
    user_permissions()
