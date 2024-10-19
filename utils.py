import psutil
import os
import time

def analyze_disks():
    """
    Analyzes disk usage and returns information on total, used, free space, and usage percentage.
    """
    disk_info = []

    partitions = psutil.disk_partitions(all=False)
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                'mountpoint': partition.mountpoint,
                'total': usage.total / (1024 * 1024 * 1024),
                'used': usage.used / (1024 * 1024 * 1024),
                'free': usage.free / (1024 * 1024 * 1024),
                'percent': usage.percent
            })
        except PermissionError as e:
            print(f"Permission denied for partition {partition.mountpoint}: {e}")
        except OSError as e:
            print(f"Error accessing partition {partition.mountpoint}: {e}")

    return disk_info

def identify_old_files(directory="/", days_old=30):
    """
    Identifies old files based on their last access time.
    
    Args:
        directory (str): The root directory to start searching for old files.
        days_old (int): The number of days since last access to consider a file as old.

    Returns:
        list: A list of old file paths.
    """
    old_files = []
    current_time = time.time()
    cutoff = current_time - (days_old * 86400)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getatime(file_path) < cutoff:
                    old_files.append(file_path)
            except PermissionError:
                print(f"Permission denied for file {file_path}")
            except OSError as e:
                print(f"Error accessing file {file_path}: {e}")

    return old_files

def identify_unused_apps(days_unused=30):
    """
    Identifies unused applications based on last access time.
    
    Args:
        days_unused (int): The number of days since last use to be considered unused.

    Returns:
        list: A list of unused application paths.
    """
    unused_apps = []
    current_time = time.time()
    cutoff = current_time - (days_unused * 86400)  # 86400 seconds in a day

    # Example for Linux: Checking /usr/bin for installed applications
    app_directories = ['/usr/bin', '/usr/local/bin']

    for directory in app_directories:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        if os.path.getatime(file_path) < cutoff:
                            unused_apps.append(file_path)
                    except PermissionError:
                        print(f"Permission denied for file {file_path}")
                    except OSError as e:
                        print(f"Error accessing file {file_path}: {e}")

    return unused_apps
