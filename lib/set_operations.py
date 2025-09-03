# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extracts the major field (tuple index 2) from each student record.
    """
    return {s[2] for s in student_list if len(s) >= 3}
