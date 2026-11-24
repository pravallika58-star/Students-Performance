# Students-Performance
# Case Study 17: Student Performance Trend Analysis

## Python Activity-Based Learning

### Student Details
- **Name:**DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

Student Performance Trend Analysis is a Python-based program used to analyse students' marks across multiple examinations.

The program compares assessment scores, calculates overall average marks, identifies improvements and declines, finds consistently weak subjects, and classifies students according to their academic performance.

## 2. Objectives

- To analyse student marks across multiple examinations.
- To calculate the overall average percentage.
- To identify improvements and declines in subject-wise marks.
- To find consistently weak subjects.
- To classify students based on their performance.
- To understand the use of nested lists and loops in Python.

## 3. Assumptions

1. The program considers four subjects: Python, Mathematics, English and Physics.
2. Three examinations are considered for each student.
3. Marks must be between 0 and 100.
4. A subject is considered consistently weak if marks are below 40 in all three examinations.
5. Student classification is based on overall average marks.

### Performance Classification

| Average Marks | Classification |
|---|---|
| 85–100 | Excellent |
| 70–84.99 | Good |
| 50–69.99 | Average |
| Below 50 | Needs Improvement |

## 4. Algorithm

1. Start the program.
2. Initialize the subject names and examination names.
3. Enter the number of students.
4. Enter each student's name.
5. Read marks for all subjects in three examinations.
6. Validate the marks.
7. Store marks using nested lists.
8. Calculate the overall average marks.
9. Classify the student's performance.
10. Compare first and third examination marks.
11. Identify improvements and declines.
12. Identify consistently weak subjects.
13. Display the complete performance report.
14. Repeat the process for all students.
15. Stop the program.

## 5. Pseudocode

```text
START

INITIALIZE subjects
INITIALIZE examinations

INPUT number_of_students

IF number_of_students <= 0
    DISPLAY invalid input
ELSE

    FOR each student

        INPUT student_name

        FOR each examination

            FOR each subject

                INPUT marks

                WHILE marks < 0 OR marks > 100
                    INPUT valid marks
                END WHILE

                STORE marks

            END FOR
        END FOR

        CALCULATE total marks
        CALCULATE average marks

        IF average >= 85
            DISPLAY Excellent
        ELSE IF average >= 70
            DISPLAY Good
        ELSE IF average >= 50
            DISPLAY Average
        ELSE
            DISPLAY Needs Improvement
        END IF

        FOR each subject

            COMPARE first exam and third exam marks

            IF last marks > first marks
                DISPLAY Improvement
            ELSE IF last marks < first marks
                DISPLAY Decline
            ELSE
                DISPLAY No Change
            END IF

            CHECK whether marks are below 40
            in all three examinations

        END FOR

        DISPLAY performance report

    END FOR

END IF

STOP
```

## 6. Python Source Code

**File name:** `student_performance.py`

The complete Python program is included in this folder.

## 7. Test Cases

| Test Case | Exam 1 | Exam 2 | Exam 3 | Expected Result |
|---|---|---|---|---|
| 1 | 60 | 70 | 80 | Improvement |
| 2 | 80 | 70 | 60 | Decline |
| 3 | 50 | 50 | 50 | No Change |
| 4 | 35 | 38 | 39 | Consistently Weak |

*The table shows example marks for an individual subject.*

## 8. Expected Output

```text
STUDENT PERFORMANCE ANALYSIS

Student Name: Pravallika

Overall Average: 64.33%
Performance: Average

Subject-wise Performance Trend

Python:
Improvement: 20 marks

Mathematics:
Improvement: 4 marks

English:
Decline: 10 marks

Physics:
Improvement: 10 marks

Consistently Weak Subjects:
Mathematics

ANALYSIS COMPLETED
```

## 9. Conclusion

The Student Performance Trend Analysis program successfully analyses students' examination marks using Python. It calculates average marks, compares examination results, identifies improvements and declines, and detects consistently weak subjects.

This project helps us understand variables, data types, operators, conditional statements, loops and nested lists. It also demonstrates how Python can be used to analyse student academic performance.

---

**Project:** Python Activity-Based Learning  
**Case Study Number:** 17  
**Topic:** Student Performance Trend Analysis
