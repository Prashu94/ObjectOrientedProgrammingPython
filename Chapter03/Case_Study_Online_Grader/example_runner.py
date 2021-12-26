from grader import Grader
from lessons import IntroToPython, Statistics

grader = Grader()
itp_id = grader.register(IntroToPython)
stat_id = grader.register(Statistics)

grader.start_assignment("John", itp_id)
print("John's Lesson: ", grader.get_lesson("John"))
print("John's check: ",
      grader.check_assignment("John", "a = 1 ; b = 'hello'"))
print("John's other check: ",
      grader.check_assignment("John", "a = 1\nb = 'hello'"))

print(grader.assignment_summary("John"))

grader.start_assignment("John", stat_id)
print("John's Lesson:", grader.get_lesson("John"))
print("John's check:", grader.check_assignment("John", "avg=5.25"))
print(
    "John's other check:",
    grader.check_assignment(
        "John", "avg = statistics.mean([1, 5, 18, -3])"
    ),
)

print(grader.assignment_summary("John"))
