
# Case Study 17: Student Performance Trend Analysis

print("==========================================")
print("     STUDENT PERFORMANCE ANALYSIS")
print("==========================================")

# Subjects and examinations
subjects = ["Python", "Mathematics", "English", "Physics"]
exams = ["Exam 1", "Exam 2", "Exam 3"]

# Input number of students
n = int(input("Enter number of students: "))

if n <= 0:
    print("Invalid number of students!")

else:
    students = []
    all_marks = []

    # Collect student details and marks
    for i in range(n):
        print("\nEnter details for Student", i + 1)

        name = input("Enter student name: ")
        students.append(name)

        student_marks = []

        for exam in exams:
            print("\n", exam)
            exam_marks = []

            for subject in subjects:
                mark = float(input("Enter " + subject + " marks: "))

                while mark < 0 or mark > 100:
                    print("Enter marks between 0 and 100")
                    mark = float(input("Enter " + subject + " marks: "))

                exam_marks.append(mark)

            student_marks.append(exam_marks)

        all_marks.append(student_marks)

    # Analyse student performance
    print("\n==========================================")
    print("         PERFORMANCE REPORT")
    print("==========================================")

    for i in range(n):

        print("\nStudent Name:", students[i])

        total = 0
        count = 0

        # Calculate average marks
        for j in range(3):
            for k in range(4):
                total += all_marks[i][j][k]
                count += 1

        average = total / count

        print("Overall Average:", round(average, 2), "%")

        # Classify student
        if average >= 85:
            print("Performance: Excellent")
        elif average >= 70:
            print("Performance: Good")
        elif average >= 50:
            print("Performance: Average")
        else:
            print("Performance: Needs Improvement")

        # Compare first and last examination
        print("\nSubject-wise Performance Trend")

        for k in range(4):
            first = all_marks[i][0][k]
            last = all_marks[i][2][k]

            difference = last - first

            print("\nSubject:", subjects[k])
            print("First Exam:", first)
            print("Last Exam:", last)

            if difference > 0:
                print("Improvement:", difference, "marks")
            elif difference < 0:
                print("Decline:", abs(difference), "marks")
            else:
                print("Performance: No Change")

        # Identify consistently weak subjects
        print("\nConsistently Weak Subjects:")

        weak_found = False

        for k in range(4):
            if (all_marks[i][0][k] < 40 and
                all_marks[i][1][k] < 40 and
                all_marks[i][2][k] < 40):

                print(subjects[k])
                weak_found = True

        if not weak_found:
            print("No consistently weak subjects")

    print("\n==========================================")
    print("       ANALYSIS COMPLETED")
    print("==========================================")
