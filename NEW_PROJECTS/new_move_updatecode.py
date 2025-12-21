import os
current_folder = os.getcwd()
new_folder_path = os.path.join(current_folder , "projects")

#function for decreage reuse code
def create_request_folder(dirname):
    destanation_folder = os.path.join(new_folder_path, dirname)
    if not os.path.exists(destanation_folder):
        os.makedirs(destanation_folder)
    return destanation_folder

for dir_path, dirnames, filenames in os.walk(new_folder_path):
    for fl in filenames:
        if os.path.splitext(fl)[-1] == ".jpeg":
            dirname = "jpeg_files"
            destanation_folder = create_request_folder(dirname)
            os.rename(os.path.join(dir_path, fl), f"{destanation_folder}/{fl}")

