import os, shutil

# the folder in which you want to delete files
folder = '/path/to/folder'

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('%s Failed to delete.  %s' % (file_path, e))    