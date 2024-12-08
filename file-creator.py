# i use this for creating and deleting a folder and subfolder

import os
import shutil

basePath = "./1ST YEAR/2ND SEM"
os.makedirs(basePath, exist_ok=True)
condition = True

# delete in cmd folder sub for /d %i in (*) do rmdir /s /q "%i"

fname = [
    "NSTP 2",
    "Operating System",
    "PE-2 Fitness Exercises",
    "Intro to Web Design",
    "The Contemporary World",
    "Art Appreciation",
    "Computer Programming 2",
    "Fundamentals of Information Management"
]

sname = [
    "ACT",
    "FINALS",
    "MIDTERM",
    "PRELIM",
    "PROJECT",
    "REVIEWER",
    "SEMI-FINALS"
]

for i in range(len(fname)):
    fpath = os.path.join(basePath, f"{fname[i]}")
    os.makedirs(fpath, exist_ok=True)

    for j in range(len(sname)):
        spath = os.path.join(fpath, f"{sname[j]}")
        os.makedirs(spath, exist_ok=True)
if condition:
    print("Na create na JB")
else: 
    for root, dirs, files in os.walk(basePath, topdown=False):
        for name in dirs: 
            dir_path = os.path.join(root, name)
            shutil.rmtree(dir_path)
    print("Na delete na JB")






