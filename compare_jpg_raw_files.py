from os import listdir

import re

source_jpg = "C:\\Users\\yungp_000\\OneDrive\\Pictures\\astrophotography\\20210302_aurora_between_airdrie_and_calgary"
source_raw = "C:\\Users\\yungp_000\\OneDrive\\Pictures\\astrophotography\\20210302_aurora_between_airdrie_and_calgary\\raw"
list_prefix_jpg = []
list_prefix_raw = []
#regex expression to get a match for everything before the .CR3 part of of the file name
pattern = r'(.*)(?=\.CR3)'

#list comprehension to put directory files into an list
files_jpg = [f for f in listdir(source_jpg)]
files_raw = [f for f in listdir(source_raw)]

for f in files_jpg:
    file_prefix = re.search(r'(.*)(?=\.JPG)', f)
    if file_prefix:
        list_prefix_jpg.append(file_prefix.group(0))
        print("the file is {}".format(file_prefix.group(0)))

for f in files_raw:
    files_prefix = re.search(pattern, f)
    if files_prefix:
        list_prefix_raw.append(files_prefix.group(0))
        print("the raw file is {}".format(files_prefix.group(0)))

# files_raw = [f for f in listdir(source_raw)]

# print(files_jpg)
list_prefix_raw.append("hi")
print(list_prefix_jpg)
print(list_prefix_raw)

set_list_jpg = set(list_prefix_jpg)
set_list_raw = set(list_prefix_raw)
difference_jpg_raw = set_list_raw.difference(set_list_jpg)
print("the differences are {}".format(difference_jpg_raw))

#missing_files = set(files_raw) - set(files_jpg)

#print(missing_files)






