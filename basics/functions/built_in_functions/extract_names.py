names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

# def extract_full_name(list):
#     full_names = []
#     for dict in list:
#         name = dict['first']  + " " + dict['last']
#         full_names.append(name)
#     return full_names

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

extract_full_name(names)
