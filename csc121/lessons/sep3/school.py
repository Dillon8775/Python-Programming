"""
school.py: define classes in a school
By: D. Strickland
9/3/26
"""

__author__ = "Dillon Strickland"

class Course:
    """
    Class to represent a course with code, description, and number of credit hours
    """
    def __init__(self, code, description, credit_hours):
        self.code = code
        self.description = description
        self.credit_hours = credit_hours

    def get_code(self):
        return self.__code

    def get_description(self):
        return self.__description

    def get_credit_hours(self):
        return self.__credit_hours

    def set_code(self, new_code):
        self.__code = new_code

    def set_description(self, description):
        self.__description = description

    def set_credit_hours(self, credit_hours):
        self.__credit_hours = credit_hours

    def __str__(self):
        """
        return a string representation of the class
        :return: str
        """
        return (
            f"Course Code: {self.code}\n"
            f"Course Description: {self.description}\n"
            f"Course Credit Hours: {self.credit_hours}"
        )

csc121 = Course("CSC121", "Python Programming", 3)

# print(csc121) - prints object in memory
print(csc121)