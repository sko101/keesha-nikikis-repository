days = [ 

"Monday", 

"Tuesday", 

"Wednesday", 

"Thursday", 

"Friday", 

"Saturday", 

"Sunday" 

] 

 

steps = [ 

6840, 

9125, 

7550, 

10420, 

8320, 

12110, 

5890 

]

total = 0
count = 0
getNumber =  int(input("Please enter a number: "))

for x in range(len(steps)):
    print(days[x] + " " + str(steps[x]))
    total = total + steps[x]
    if steps[x] >= getNumber:
        count = count + 1

print(total)
print(count)
average = total / len(days)
roundedAverage = round(average, 2)
print("Average = " + str(roundedAverage) + ". ")

