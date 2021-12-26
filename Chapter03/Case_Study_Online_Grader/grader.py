import abc
import uuid

# This is like an abstract class
class Assignment(metaclass=abc.ABCMeta):
    """Assignment class is a type of Abstract class that will have methods which needs to be implemented by the class extending the same."""
    # Abstract Method
    @abc.abstractmethod
    def lesson(self, student):
        pass

    # Abstract Method
    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class Grader:
    """Grader Class: maintains the dictionary of student_graders
    and assignment_classes.
    1. register function to register the assignment
    2. start_assignment method to start the grading of student's assignment
    3. get_lesson function to return the assignment_lesson
    4. check_assignments function to check the assignment.
    5. assignment_summary function returns the assignment summary for a student."""
    def __init__(self):
        self.student_graders = {}
        self.assignment_classes = {}

    def register(self, assignment_class):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError('Your Class does not have right methods.')
        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id

    def start_assignment(self, student, id):
        self.student_graders[student] = AssignmentGrader(student, self.assignment_classes[id])

    def get_lesson(self, student):
        assignment = self.student_graders[student]
        return assignment.lesson()

    def check_assignment(self, student, code):
        assignment = self.student_graders[student]
        return assignment.check(code)

    def assignment_summary(self, student):
        grader = self.student_graders[student]
        return f"""
        {student}'s attempt at {grader.assignment.__class__.__name__}:
        
        attempts: {grader.attempts}
        correct: {grader.correct_attempts}
        
        passed: {grader.correct_attempts > 0}
        """


class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1
        return result

    def lesson(self):
        return self.assignment.lesson()