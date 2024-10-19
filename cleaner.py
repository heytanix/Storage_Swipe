from utils import analyze_disks, identify_old_files, identify_unused_apps

class Cleaner:
    def run(self):
        print("Analyzing mounted disks...")
        analyze_disks()

        print("\nIdentifying old files...")
        old_files = identify_old_files(directory='/', days=30)
        print(f"\nOld files ({len(old_files)}):")
        for file in old_files:
            print(file)

        print("\nIdentifying unused apps...")
        unused_apps = identify_unused_apps()
        print(f"\nUnused apps ({len(unused_apps)}):")
        for app in unused_apps:
            print(app)
