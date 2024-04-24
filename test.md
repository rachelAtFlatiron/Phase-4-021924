reviews

id (int)
year
summary
employee_id



employee

id (int)
name
hire_date

-----


Employee1: Alison
Review1: refers to Employee1
Review2: refers to Employee1
Review3: refers to Employee1

------


ORM

class Employee:
    self.id = id
    self.name = name
    self.hire_date = hire_date

    - iterating over all reviews
    - return reviews with matching employee id
    def all_reviews(self):
        return [review for review in Review.all where review.employee_id == self.id]

class Review:
    self.id
    self.year = year
    self.summary = summary
    self.employee_id = employee_id

    def employee(self):
        return [employee for employee in Employee.all where employee.id == self.employee_id][0]



employee1: alice
employee1.all_reviews -> [<Review />, <Review />, <Review />]

review1: test
review1.employee -> <Employee />

---------------------------------------

class Employee 
    self.id = id
    self.name = name

    def rsvps(self):
        return [rsvp for rsvp in Rsvp.all if rsvp.employee_id == self.id]

    def meetings(self):
        return [rsvp.meeting() for rsvp in self.rsvps()]


class Meeting
    self.id = id
    self.topic = topic

    - return a LIST OF INSTANCES of all rsvps for this meeting
    def rsvps(self):
        return [rsvp for rsvp in Rsvp.all if rsvp.meeting_id == self.id]

    - iterate over all rsvps
    - extract the employee instance
    - return A LIST OF EMPLOYEE INSTANCES for that meeting via .rsvps()
    def employees(self):
        return [rsvp.employee() for rsvp in self.rsvps()]

Meeting -> rsvps (aka employee_meetings) -> employee

- intermediate
class Rsvp
    self.id = id
    self.employee_id = employee_id
    self.meeting_id = meeting_id

    - return A SINGLE INSTANCE of an employee
    def employee(self):
        return [employee for employee in Employee.all if employee.id == self.employee_id][0]

    - return A SINGLE INSTANCE of a meeting
    def meeting(self):
        return [meeting for meeting in Meeting.all if meeting.id == self.meeting_id][0]
    


