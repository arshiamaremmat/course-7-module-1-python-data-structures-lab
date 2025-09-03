# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    - Case-insensitive match on the major (tuple index 2).
    """
    if major is None:
        return []
    target = str(major).strip().lower()
    return [s for s in student_list if len(s) >= 3 and str(s[2]).lower() == target]
