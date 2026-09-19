scores= [72, 45, 90, 61, 38]
for score in scores:
    if score >=80:
        print(f"{score}:A")
    elif score >= 70:
        print(f"{score}:B")
    elif score >=50:
        print(f"{score}:C")
    else:
        print(f"{score}:F")
# Count number of learners who passed the exam # 
count = 0
for score in scores:
    if score >=50:
        print(f"{score}:Pass")
        count += 1
    else:
        print(f"{score}:Fail")
print(f"count of passing scores: {count}")
print(f"count of failing scores: {len(scores) - count}")

# Addition of all scores #
total = sum(scores)
print(f"Total: {total}")

# Average #
avg = total/len(scores)
print(f"Average: {round(avg, 1)}")