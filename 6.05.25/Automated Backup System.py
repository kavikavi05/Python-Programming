import shutil

source = "important_file.txt"
backup = "backup_file.txt"

shutil.copy(source, backup)
print("Backup created successfully!")
