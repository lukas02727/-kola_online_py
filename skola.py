def add_class(school):
    class_name = input("Zadej název třídy: ")
    school[class_name] = {}
    return school

def add_student(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu pro přidání studenta: ")
    student_name = input("Zadejte jméno studenta: ")
    school[selected_class][student_name] = {}
    return school

def add_subject(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu pro přidání předmětu: ")
    subject_name = input("Zadejte jméno předmětu: ")
    for student in school[selected_class]:
        school[selected_class][student][subject_name] = []
    return school

def add_grade(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu pro přidání známky: ")
    for student_name in school[selected_class]:
        print(student_name)
    selected_student = input("Zadejte studenta pro přidání známky: ")
    for subject_name in school[selected_class][selected_student]:
        print(subject_name)
    selected_subject = input("Zadejte předmět pro přidání známky: ")
    selected_grade = input("Zadejte známku: ")
    school[selected_class][selected_student][selected_subject].append(int(selected_grade))
    return school

def delete_class(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu, kterou chcete smazat: ")
    del school[selected_class]
    return school
    
def delete_student(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu studenta, kterého chcete smazat: ")
    for student_name in school[selected_class]:
        print(student_name)
    selected_student = input("Zadejte studenta, kterého chcete smazat: ")
    del school[selected_class][selected_student]
    return school

def delete_subject(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu předmětu, který chcete smazat: ")
    selected_subject = input("Zadejte předmět, který chcete smazat")
    for student_name in school[selected_class]:
        try:
            del school[selected_class][student_name][selected_subject]
        except IndexError:
            pass
    return school
    
def get_average_grade(school):
    for class_name in school:
        print(class_name)
    selected_class = input("Zadejte třídu pro výpis průměru známek: ")
    for student_name in school[selected_class]:
        print(student_name)
    selected_student = input("Zadejte studenta pro výpis průměru známek: ")
    for subject_name in school[selected_class][selected_student]:
        print(subject_name)
    selected_subject = input("Zadejte předmět pro výpis průměru známek: ")
    grades = school[selected_class][selected_student][selected_subject]
    print(f"Průměrná známka: {sum(grades)/len(grades)}")
    
    
    
def main():
    school = {}
    print("Konzolová aplikace Škola Online")
    print("Přidej třídu: [add_class]")
    print("Přidej studenta: [add_student]")
    print("Přidej předmět: [add_subject]")
    print("Přidej známku: [add_grade]")
    print("Smaž třídu: [del_class]")
    print("Smaž studenta: [del_student]")
    print("Smaž předmět: [del_subject]")
    print("Zobrazit průměr známek: [average_grade]")
  
    while True:
        command = input("Zadejte příkaz: ")
        if command == "add_class": 
            school = add_class(school)
        elif command == "add_student": 
            school = add_student(school)
        elif command == "add_subject": 
            school = add_subject(school)
        elif command == "add_grade": 
            school = add_grade(school)
        elif command == "del_class": 
            school = delete_class(school)
        elif command == "del_student": 
            school = delete_student(school)
        elif command == "del_subject": 
            school = delete_subject(school)
        elif command == "average_grade":
            get_average_grade(school)
main()