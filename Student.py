# classes define your data type when python doesn't have a default
class Student: # we want to represent the data type that a student is

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name # we need to take the values that I passed in and assign them to the correct attribute (e.g. "Jim" belongs to attribute name)
        self.major = major
        self.gpa = gpa
        self.is_on_probatioin = is_on_probation