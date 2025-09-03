# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    Returns: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"

def display_students(student_list):
    """
    Display all student records.
    Loops through student_list and prints each formatted record.
    """
    for student in student_list:
        print(format_student_data(student))
