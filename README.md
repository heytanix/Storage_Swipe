# Storage Swipe

**Storage Swipe** is a comprehensive cross-platform system cleaner tool designed to analyze mounted disks, identify trash files, detect unused applications, and report on storage usage. This utility helps users optimize their system storage by providing insights into disk usage and enabling them to reclaim valuable space.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Requirements](#requirements)

## Features

- **Disk Analysis**: 
  - Scans all mounted disks in the system.
  - Reports total size, used space, and free space for each disk.

- **Old File Detection**: 
  - Identifies files that have not been accessed for a specified number of days.
  - Helps locate old files that may no longer be needed.

- **Unused Application Detection**: 
  - Detects applications that haven’t been launched in a user-defined time period.
  - Provides a list of unused applications to consider for uninstallation.

- **Trash Cleaner**: 
  - Compiles a list of files that may be candidates for deletion based on user-defined criteria.
  - Allows users to manage and remove unwanted files efficiently.

- **Cross-Platform Compatibility**: 
  - Works seamlessly on Linux, macOS, and Windows, making it accessible for a wide range of users.

## How It Works

1. **Disk Analysis**: 
   - The program analyzes mounted disks and displays their storage statistics, including total capacity, used space, and free space.

2. **Old Files Detection**: 
   - The tool scans the file system to identify files that have not been accessed for a user-defined number of days, defaulting to 30 days.

3. **Unused Applications Detection**: 
   - It examines common application directories and identifies applications that have not been executed within the specified time frame.

4. **Trash Cleaner**: 
   - Gathers potential trash files and presents them to the user for review and deletion.

## Requirements

Before running Storage Swipe, ensure you have Python 3 installed along with the required dependencies. You can install the necessary libraries using the provided `requirements.txt` file.

### Installation Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/username/storage-swipe.git
   cd storage-swipe
