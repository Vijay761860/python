import os
current_folder = os.getcwd()
new_folder_path = os.path.join(current_folder) 

#txt file move code here
destionaction_folder = os.path.join(new_folder_path, "text_file_only") #new txt move hogi here
if not os.path.exists(destionaction_folder):
    os.mkdir(destionaction_folder)

#mp4 file move code here
destionaction_folder_mp4 = os.path.join(new_folder_path, "mp4_files_only") #new txt move hogi here
if not os.path.exists(destionaction_folder_mp4):
    os.mkdir(destionaction_folder_mp4)


#jpg file code here
destionaction_folder_jpg = os.path.join(new_folder_path, "jpg_files_only") #new txt move hogi here
if not os.path.exists(destionaction_folder_jpg):
    os.mkdir(destionaction_folder_jpg)

#pdf file code here
destionaction_folder_pdf = os.path.join(new_folder_path, "pdf_files_only") #new txt move hogi here
if not os.path.exists(destionaction_folder_pdf):
    os.mkdir(destionaction_folder_pdf)

for dir_paths, dir_names, file_names in os.walk(new_folder_path): #new_folder_path ki numder check kartaha
    #txt file move code here
    for fl in file_names:
        # print(fl)
        if os.path.splitext(fl)[-1] == ".txt":
            os.rename(os.path.join(dir_paths, fl), f"{destionaction_folder}//{fl}")

    #mp4 file code here
    for fl in file_names:
        if os.path.splitext(fl)[-1] == ".mp4":
            os.rename(os.path.join(dir_paths, fl), f"{destionaction_folder_mp4}//{fl}")

    #jpg file code here
    for fl in file_names:
        if os.path.splitext(fl)[-1] == ".jpg":
            os.rename(os.path.join(dir_paths, fl), f"{destionaction_folder_jpg}//{fl}")

    #pdf file code here
    for fl in file_names:
        if os.path.splitext(fl)[-1] == ".pdf":
            os.rename(os.path.join(dir_paths, fl), f"{destionaction_folder_pdf}//{fl}")