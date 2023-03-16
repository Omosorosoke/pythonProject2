# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello")
print("my name is kolawole Ojo")

print("Hello")
print("How are you doing")

profile = {}
while True:
    name = input("Write your name: ")
    if name.lower() == 'quit':
        break
    else:
        profile['name'] = name
    sex = input("Your gender: ")
    if sex.lower() == 'quit':
        break
    else:
        profile['sex'] = sex
    country = input("Your country:  ")
    if country.lower() == 'quit':
        break
    else:
        profile['country'] = country
    flat_number = input("What flat do you live? ")
    if str(flat_number.lower()) == 'quit':
        break
    else:
        profile['flat'] = flat_number
    room_number = input("Your room number: ")
    if str(room_number.lower()) == 'quit':
        break
    else:
        profile['room'] = room_number
        print(profile)
    break

class Resident():
    """ an attempt to retrieve information about a resident of dormitory"""
    def __init__(self, name, flat, room, sex, country):
        """ initialise the attributes of the class"""
        self.name = profile['name']
        self.flat = profile['flat']
        self.room = profile['room']
        self.sex = profile['sex']
        self.country = profile['country']

    def student_info(self):
        """ prints the basic information about the students"""

        if self.sex == "male":
            print(self.name.title() + " is a male student from " + self.country.title())
        else:
            print(self.name.title() + " is a female students from " + self.country.title())
        location = " Flat " + str(self.flat) + ", Room " + str(self.room)
        return print("location :" + location)

kola = Resident(**profile)
kola.student_info()


