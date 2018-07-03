class Person(object):
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.total_greeting_count = 0
        self.people_greeted = []
        self.unique_people_greeted_count = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.total_greeting_count += 1
        if other_person not in self.people_greeted:
            self.people_greeted.append(other_person)

    def contact_info(self):
        print "%s's contact info is: \nemail: %s \nphone: %s\n"%(self.name, self.email, self.phone)
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def num_friends(self):
        len(self.friends)

    def __repr__(self):
        print "%s" %self.name
    
    def num_unqiue_people_greeted(self):
        self.unique_people_greeted_count = len(self.people_greeted)
        print self.unique_people_greeted_count

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948", "")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456", "")
sonny.greet(jordan)
jordan.greet(sonny)
sonny.contact_info()
jordan.contact_info()
sonny.greet(jordan)
jordan.add_friend(sonny)
print sonny.total_greeting_count
sonny.num_unqiue_people_greeted()


# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def print_info(self):
#         print "%s %s %s" %(self.year, self.make, self.model)

# my_vehicle = Vehicle("Ford", "Focus", 2012)
# my_vehicle.print_info()