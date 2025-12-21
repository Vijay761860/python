'''this is a os module i can use this for os related work doing like file manuplaction
and file creating and other system file related work'''
import os

print(os.getcwd()) #cutternt working dir
print(os.name) # "nt " its provide so name nt for windows
print(os.sep) # "\" this is a slcae lunix for \ win for /
# print(os.makedirs("new_dir")) # for creating dir
# os.chdir("new_dir") # chand current working dir
print(os.getcwd())# chand current working dir
# print(os.stat("redmi.md"))

"""os.walik()
cutrrent_folder = os.getcwd()
for item in os.walk(cutrrent_folder):
    print(item) 
for root , dirname , filesname in os.walk(cutrrent_folder):
    print(root)
    print(filesname)
    print(dirname)"""

# path importend Module
# path join and reading
"""current_folder = os.getcwd()
new_folder_path = os.path.join(current_folder , "new_dir")  # os.path.join()  change path 
print(new_folder_path)"""

#i can create a file suing os.path.join()
"""file_name = os.path.join(new_folder_path , "sample.txt") #join a file
with open(file_name , "w") as f: #open a file
    f.write("it's a simple os.path.join modeule and simple file method") # write a file 
"""
# print(os.path.split(new_folder_path)) # diconnect a file and folder ro other sources
# print(os.path.splitext("redmi.md")) # file extenction diconnect like .txt , .mo4 etc 
# print(os.rename("redmi.md" , "readmi.md")) # file rename 


# cut and past and copy file
"""current_folder = os.getcwd()
new_folder_path = os.path.join(current_folder, "new_dir")
source_folder = os.path.join(current_folder, "read_me.txt") 
print(os.rename(source_folder, f"{new_folder_path}\\read_me.txt")) #/
 """

"""current_folder = os.getcwd()
new_folder_path = os.path.join(current_folder , "new_dir")

source_folder = os.path.join(current_folder , "read_me.txt")
desnactiuon_folder = os.path.join(new_folder_path ,"read_me.txt")

os.rename(source_folder ,desnactiuon_folder)
print(source_folder,desnactiuon_folder)"""


# os.remove("read_me.txt") 
os.remove("md")