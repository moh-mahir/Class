class Hospital:
    all_doctors = {}
    appointments_doctors = {}
    check_schedule=0
    def __init__ (self,name,spec):
        self.name = name
        self.spec = spec
        Hospital.appointments_doctors[self.name]="hasn't appointment"
        Hospital.all_doctors[self.name]=self.spec
    @classmethod
    def get_doctors_by_spec(cls,spec):
        doctors_by_spec = []
        for i in cls.all_doctors:
            if cls.all_doctors[i] == spec:
                doctors_by_spec.append(str(i))
        if doctors_by_spec == []:
            return f"The specialization is not found "
        return doctors_by_spec
    @classmethod
    def get_all_doctors (cls):
        for i in cls.all_doctors:
            print(f"{i} from {cls.all_doctors[i]}")
    @classmethod
    def get_schedule(cls,name):
        check_list=2
        for i in cls.appointments_doctors:
            if name == i:
                Hospital.check_schedule=1
                if cls.appointments_doctors[i]=="hasn't appointment":
                    print(f"{i} hasn't appointment")
                else:
                    print(f"This is {i} schedule : ")
                    for j in range((len(cls.appointments_doctors[i])-1)//2):
                        print(f"{cls.appointments_doctors[i][check_list]} has an appointment at {cls.appointments_doctors[i][check_list+1]} O'clock ")
                        check_list+=2
        if Hospital.check_schedule==0:
            print("Sorry the doctor is not found ")
                
print("Welcome to our hospital ( weirdo hospital)")
print("It's our pleasure to help you")
print("Please enter the number you would like to do")
print("1- add doctor")
print("2- get doctor by specialization")
print("3- book an appointment")
print("4- get list of all doctors")
print("5- get a doctor schedule")
print("If you want to exit the program, type the word (stop).")
print()
while True:
    try:
        commnd = input("How can I help you : ")
        if commnd == "add doctor" or commnd == "1":
            name_doctor = input("Please enter the doctors name : ")
            spec_doctor = input("Enter his specializion : ")
            new_doctor = Hospital(name_doctor,spec_doctor)
            print("The doctor has added successfully")
        
        elif commnd == "get doctor by specialization" or commnd == "2":
            spec_doctor = input("Enter the specialization you want : ")
            print(Hospital.get_doctors_by_spec(spec_doctor))
        
        elif commnd == "book an appointment" or commnd == "3":
            name_patient = input("Enter the patient name ")
            name_doctor = input("Which doctor you want to book with ")
            check_date=1
            check_doctor = 0
            for i in Hospital.appointments_doctors:
                if name_doctor == i :
                    check_doctor=1
                    date = int(input("Enter the time out of 24 hours "))
                    if date >=0 and date < 24 :
                        if Hospital.appointments_doctors[i] == "hasn't appointment":
                                Hospital.appointments_doctors[i]=['name','date ->']
                        for j in Hospital.appointments_doctors[i]:
                            if j == date:
                                check_date=0
                        if check_date==1:
                            Hospital.appointments_doctors[i].append(name_patient)
                            Hospital.appointments_doctors[i].append(date)
                            print("appointment has booked successfully ")
                        else:
                            print("The appointment is reserved ")
                    else:
                        print ("The time must be between 0 to 23")
            if check_doctor == 0:
                print("Sorry the doctor is not found ")
        
        elif commnd=="get list of all doctors" or commnd == "4":
            Hospital.get_all_doctors()
        
        elif commnd == "get a doctor schedule" or commnd == "5":
            name = input("What is name of doctor you want ")
            Hospital.get_schedule(name)

        elif commnd == "stop":
            break
        else :
            print("Commnd not found ")
    except ValueError:
        print("Date of an appointment must be a number only without any commas, signs or letters ")

