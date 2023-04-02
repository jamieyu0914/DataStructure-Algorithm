
Score=[87, 66, 90, 65, 70]

Total_Score=0

for i in range(5):
    print("第 %d 位學生的分數： %d" %(i+1,Score[i]))
    Total_Score+=Score[i]

print("------------------------")
print("5位學生的總分： %d" %Total_Score)