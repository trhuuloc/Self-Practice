from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, yob):
        self._type = None
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade
        self._type = 'Student'

    def describe(self):
        script = f'{self._type} - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}'
        print(script)

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject
        self._type = 'Teacher'

    def describe(self):
        script = f'{self._type} - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}'
        print(script)

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist
        self._type = 'Doctor'

    def describe(self):
        script = f'{self._type} - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}'
        print(script)

class Ward:
    def __init__(self, name):
        self.__ward_name = name
        self.__profiles = []

    def add_person(self, person):
        self.__profiles.append(person)

    def describe(self):
        print(f'Ward Name: {self.__ward_name}')
        for person in self.__profiles:
            person.describe()

    def count_doctor(self):
        doctors = [person for person in self.__profiles if person._type == 'Doctor']
        return len(doctors)

    def sort_age(self):
        self.__profiles.sort(key=lambda person: int(person._yob), reverse=True)

    def compute_average(self):
        teacher_age = [int(person._yob) for person in self.__profiles if person._type == 'Teacher']
        return float(sum(teacher_age) / len(teacher_age))

# Example
student1 = Student(name='studentA', yob=2010, grade='7')
student1.describe()

teacher1 = Teacher(name='teacherA', yob=1969, subject='Math')
teacher1.describe()

doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
doctor1.describe()

teacher2 = Teacher(name='teacherB', yob=1995, subject='History')
doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')

ward1 = Ward(name='Ward1')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")

print("\nAfter sorting the age of people in Ward1")
ward1.sort_age()
ward1.describe()

average_yob_teachers = ward1.compute_average()
print(f"\nAverage year of birth for teachers in the ward: {average_yob_teachers:.2f}")
