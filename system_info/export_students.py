def export_students():
    with open('phonebook.csv', 'r', encoding='utf-16') as pb:
        data = []
        t = []
        for line in pb:
            if ' ' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ',' in line:
                temp = line.split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
                return data