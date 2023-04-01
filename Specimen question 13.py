ClassSize = 5
SubjectNo = 3

StudentName = ["Emma", "Noah", "Olivia", "Liam", "Ava"]

StudentMark = [[60, 75, 65], [45, 80, 60], [90, 85, 95], [60, 55, 80], [75, 100, 75]]



DISTINCTION = 70 # integer
MERIT = 55 # integer
PASS = 40 # integer

Total = [] # array of integer
Average = [] # array of integer

DistinctionNo = 0 # integer
MeritNo = 0 # integer
PassNo = 0 # integer
FailNo = 0 # integer

# Initialise total and average arrays with zeros
for i in range(0, ClassSize):
  Total.append(0)

for i in range(0, ClassSize):
  Average.append(0)

# Iterate through each student in the class
for StudentCounter in range(0, ClassSize):
  # Calculate total and average marks for the student
  for SubjectCounter in range(0, SubjectNo):
    Total[StudentCounter] += StudentMark[StudentCounter][SubjectCounter]
  Average[StudentCounter] = int((Total[StudentCounter] / SubjectNo) + 0.5)

  print("Name:", StudentName[StudentCounter])
  print("Combined total mark:", Total[StudentCounter])
  print("Average mark:", Average[StudentCounter])

  # Check average against grade thresholds and increment corresponding grade category
  if Average[StudentCounter] >= DISTINCTION:
    DistinctionNo += 1
    print("Grade Distinction")
  elif Average[StudentCounter] >= MERIT:
    MeritNo += 1
    print("Grade Merit")
  elif Average[StudentCounter] >= PASS:
    PassNo += 1
    print("Grade Pass")
  else:
    FailNo += 1
    print("Grade Fail")

  print()

print("Number of distinctions:", DistinctionNo)
print("Number of merits:", MeritNo)
print("Number of passes:", PassNo)
print("Number of fails:", FailNo)
