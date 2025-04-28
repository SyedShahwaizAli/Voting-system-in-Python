eligible_count = 0

for i in range(5):
    age = int(input("Enter age for person " + str(i+1) + ": "))
    
    if age >= 18:
        print("Eligible to Vote")
        eligible_count += 1
    else:
        print("Not Eligible")

print("Total number of eligible voters: " + str(eligible_count))