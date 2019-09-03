import os
import shutil
def search(name):
    for root,dirs,files in os.walk("C:\\"):
        if name in files:
            print(root, name)
    shutil.copy(name, r"C:\Users\Pranav\Desktop\new")
    input()

try:
    name = input("Enter name of file :")
    search(name)
    print("success")
except:
    print("no file found")
