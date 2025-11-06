marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for course {i}: "))
    marks.append(mark)

print("\nFailed Courses:")
failed = False
for i, mark in enumerate(marks, start=1):
    if mark < 50:
        print(f"Course {i}: {mark}")
        failed = True

if not failed:
    print("None. All courses passed!")

total = sum(marks)
average = total / len(marks)

print(f"\nTotal Marks: {total}")
print(f"Average Mark: {average:.2f}")
