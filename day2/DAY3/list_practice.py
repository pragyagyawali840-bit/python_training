grades = [85,92,78]
grades.append(95)
grades.remove(78)
if 92 in grades:
    print("92 is in the list")

total_count = len(grades) 
total_sum = sum(grades) 
lowest = (grades)
highest = max(grades)
print("total count,total sum,lowest, highest=",total_count ,total_sum ,lowest ,highest)