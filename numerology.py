from datetime import datetime

class Person:
    def __init__(self, first_name , last_name , age , email , birth_day):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.email = email
        self.birth_day = birth_day

    #properties 
    def birth_day(self):
        return self.birth_day.day , self.birth_day.month , self.birthday.year
    
    def get_info(self):
        return f" Name : {self.first_name} {self.last_name}\n" \
               f" Age: {self.age} \n " \
               f" Email: {self.email} \n " \
               f" Birthday:{self.birth_day.strftime('%d/%m/%Y')} "
    def life_path_number(self):
        day = sum(int(digit) for digit in str(self.birth_day.day)) 
        month = sum(int(digit) for digit in str(self.birth_day.month)) 
        year = sum(int(digit) for digit in str(self.birth_day.year))
        total = day+month+year
        while total > 9:
            total = sum(int(digit) for digit in str(total))
        return total 
        
    def get_info_by_number(self, number):
        with open('numer.txt ', 'r') as file:
            content = file.read()
            start = content.find(f"#{number}")
            end = content.find("#", start + 1)
            if end == -1:  # If it's the last entry
                return content[start:].strip()
            return content[start:end].strip() 
        

if __name__ == "__main__":
    print("Enter your information:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))
    email = input("Email: ")
    birth_day = input("Birthday (DD/MM/YYYY): ")
    
    for fmt in ("%d.%m.%Y", "%d/%m/%Y"):
        try:
            birth_day = datetime.strptime(birth_day, fmt)
            break
        except ValueError:
            continue
    else:
        print("Invalid date format. Please use DD.MM.YYYY or DD/MM/YYYY.")
        exit()
    
    person = Person(first_name, last_name, age, email, birth_day)
    
    print("\n Person Information:")
    print(person.get_info())
    
    life_path_number = person.life_path_number()
    print(f"\n Life Path Number: {life_path_number}")
    
    print("\n Numerology Information:")
    print(person.get_info_by_number(life_path_number))
