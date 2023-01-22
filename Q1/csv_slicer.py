import csv
num = []
value_dict = {}
name  = ""
read_file= open("names_1.csv",'r')
csvFile = csv.DictReader(read_file)

for key in csvFile:
 keys, values = list(key.keys()),list(key.values())
 value_dict[values[0]] = values[1]
 num.append(values[0])
 name += "".join(values[1].split(" "))
name = "".join(set(name))
num_sort = sorted(list(map(int,num)))

row_dict = []
count = 1
for i in num_sort:
 count ^=1
 row_dict.append({keys[0]:str(i),keys[1]:value_dict[str(i)]}) if count else 0


write_file= open("names_2.csv",'w')
newFile = csv.DictWriter(write_file,fieldnames=keys,delimiter=',')
newFile.writeheader()
newFile.writerows(row_dict)


min = 255
for i in name:
 for j in name:
    diff = abs(ord(i)-ord(j)) if i != j else 0
    min = diff if (i != j and min>diff) else min
print(min)

