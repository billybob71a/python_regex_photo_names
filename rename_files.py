from os import listdir
import shutil


source_dir = "C:\\Users\\yungp_000\\OneDrive\\Pictures\\astrophotography\\20210302_aurora_between_airdrie_and_calgary"
dest_dir = "c:\\Users\\yungp_000\\OneDrive\\Pictures\\astrophotography\\20210302_aurora_between_airdrie_and_calgary\\sequenced\\"

files = [f for f in listdir(source_dir)]

print(files)

for eachitem in files:
    shutil.copyfile(source_dir+"\\"+eachitem, dest_dir+str(files.index(eachitem))+".jpg")