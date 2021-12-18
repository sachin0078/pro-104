import csv
from collections import Counter

with open("p-104.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
mean_data=[]
median_data=[]
mode_data=[]
for i in range(len(file_data)):
    num=file_data[i][2]
    mean_data.append(float(num))
    median_data.append(float(num))
    mode_data.append(float(num))

sum=0
m=len(mean_data)

n=len(median_data)
median_data.sort()

o=len(mode_data)
data=Counter(mode_data)

for i in mean_data:
    sum=sum+i
mean=sum/m
print("mean=",mean) 

if n%2==0:
    m1=float(median_data[n//2])
    m2=float(median_data[n//2-1])
    median=(m1+m2)/2
else:
    median=float(median_data[n//2])
print("median=",median)

mode_data_for_range = {
                        "100-110": 0,
                        "110-120": 0,
                        "120-130": 0
                    }
for weight, occurence in data.items():
    if 100 < float(weight) < 110:
        mode_data_for_range["100-110"] += occurence
    elif 110 < float(weight) < 120:
        mode_data_for_range["110-120"] += occurence
    elif 120 < float(weight) < 130:
        mode_data_for_range["120-130"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print("mode=",mode)



