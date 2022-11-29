from export_students import export_students
from print_data import print_data

def search_students(search, data):
    if len(data) > 0:
        for item in data:
            if search in item:
                return item
    else:
        return None