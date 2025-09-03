# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator (generator expression).
    """
    if major is None:
        # Return an empty iterator if no major provided
        return iter(())

    target = str(major).strip().lower()
    return (
        student
        for student in student_list
        if len(student) >= 3 and str(student[2]).strip().lower() == target
    )
