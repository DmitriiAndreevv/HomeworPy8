
def import_students(data, sep = None):
    with open('phonebook.csv', 'a+', encoding='utf-16') as pb:
        if sep == None:
            for i in data:
                pb.write(f'{i}\n')
            pb.write(f'\n')
        else:
            pb.write(sep.join(data))
            pb.write(f'\n')