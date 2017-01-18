class person:
    def __init__(self,name,age,DoB,address,contact,gender):
        self.name=name
        self.age=age
        self.DoB=DoB
        self.address=address
        self.contact=contact
        self.gender=gender
class employee(person):
    def __init__(self,occupation,workDepartment,job,salary):
        self.occupation=occupation
        self.workDepartment=workDepartment
        self.job=job
        self.salary=salary
class teacher(employee):
    def __init__(self,subject,teachingClass):
        self.subject=subject
        self.teachingClass=teachingClass
    def teach():
        print 'i am teaching'

class cook(employee):
    def __init__(self,position):
        self.position=position
    def cook():
        print 'i am cookin'
class student(person):
    def __init__(self,parentName,parentNumber,parentContact):
        self.parentName=parentName
        self.parentNumber=parentNumber
        self.parentContact=parentContact
        
        
        
