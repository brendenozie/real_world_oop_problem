#Registration problem solved using OOP

class person:
    def __init__(self,name,age,DoB,address,contact,gender):
        self.name=name
        self.age=age
        self.DoB=DoB
        self.address=address
        self.contact=contact
        self.gender=gender
    def __str__(self):
        return "Title:%s , author:%s, pages:%s " (self.title, self.author, self.pages)
    def walk():
        return 'i am walking "
              
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
        return 'i am teaching'
    def walk:
        return 'i am walking to the staffroom'

class cook(employee):
    def __init__(self,position):
        self.position=position
    def cook():
        return 'i am cookin'
    def walk():
        return 'i am walking to the kitchen'
    
class student(person):
    def __init__(self,parentName,parentNumber,parentContact):
        self.parentName=parentName
        self.parentNumber=parentNumber
        self.parentContact=parentContact
    def walk():
        return 'i am walking to class'
        
        
        
