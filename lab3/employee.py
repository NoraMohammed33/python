from person import Person
from car import Car


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 1000:
            raise ValueError("Salary must be 1000 or more")
        self._salary = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email")
        self._email = value

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        if value < 0 or value > 100:
            raise ValueError("Health rate must be between 0 and 100")
        self._healthRate = value

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "tired"
        elif hours > 8:
            self.mood = "lazy"

    def send_mail(self, to, subject, msg, receiver_name=None):
        if receiver_name:
            msg = f"Dear {receiver_name},\n\n{msg}"
        else:
            msg = f"{msg}"

        print(f"From: {self.email}\nTo: {to}\nSubject: {subject}\n\n{msg}")

    def drive(self, distance):
        time = distance / self.car.velocity
        self.car.run(self.car.velocity, distance)
        print(f"Arrived at ITI after {time:.2f} hours")

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def __str__(self):
        return f"Employee {self.name}, ID: {self.id}, Email: {self.email}, Salary: {self.salary}"
