def thesaurus(*args):
    list1 = [*args]
    d = {}
    for name in list1:
        name.capitalize()
        c = name[0]
        if c in d.keys():
            d[c].append(name)
        else: dict_1 = [name]
        d[c] = dict_1
        return d

print(thesaurus("Иван"))
print(thesaurus("Мария"))
print(thesaurus("Петр"))
print(thesaurus("Илья"))