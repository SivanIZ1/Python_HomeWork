numbers = []
for i in range(4):
    num = int(input(f"הכנס מספר {i+1}: "))
    numbers.append(num)
print("המספרים השליליים הם:")
for num in numbers:
    if num < 0:
        print(num)

words = ["apple", "banana", "cherry", "date"]
print("הרשימה המקורית:", words)
temp = words[0]
words[0] = words[-1]
words[-1] = temp
print("הרשימה לאחר ההחלפה:", words)

grades = [65, 85, 72, 60, 95, 70, 55]
passed_count = 0
for grade in grades:
    if grade >= 70:
        passed_count += 1
print(f"מספר התלמידים שעברו את המבחן הוא: {passed_count}")