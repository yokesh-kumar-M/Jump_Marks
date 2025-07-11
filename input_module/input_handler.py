import pandas as pd

def get_student_data():
    data = []
    num_subjects = int(input("Enter number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Subject Name: ")
        credit = float(input("Credit: "))
        marks = float(input("Marks (0-100): "))
        data.append({'Subject': subject, 'Credit': credit, 'Marks': marks})
    return pd.DataFrame(data)
