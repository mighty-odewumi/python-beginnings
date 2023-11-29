class Student:

    def __init__(self, name, grade, exam_score):
        self.name = name
        self.grade = grade
        self.exam_score = exam_score

    def in_SSS3(self):
        if self.exam_score >= 70:
            return True
        else:
            return False
