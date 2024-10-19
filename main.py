from utils import analyze_disks, identify_old_files, identify_unused_apps

def main():
    print("Analyzing mounted disks...")
    disks = analyze_disks()
    
    for disk in disks:
        print(f"Disk {disk['mountpoint']}: {disk['free']:.2f} GB free out of {disk['total']:.2f} GB ({disk['percent']}% used)")
    
    print("\nIdentifying old files (older than 30 days)...")
    old_files = identify_old_files("/")
    
    if old_files:
        print("Old files identified:")
        for file in old_files[:10]:
            print(file)
        print(f"\nTotal old files: {len(old_files)}")
    else:
        print("No old files found.")
    
    print("\nIdentifying unused applications (not used for 30 days)...")
    unused_apps = identify_unused_apps()
    
    if unused_apps:
        print("Unused applications identified:")
        for app in unused_apps[:10]:
            print(app)
        print(f"\nTotal unused applications: {len(unused_apps)}")
    else:
        print("No unused applications found.")

if __name__ == "__main__":
    main()
