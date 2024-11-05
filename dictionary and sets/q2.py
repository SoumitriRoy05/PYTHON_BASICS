marks={
    "Soumitri":90,
    "Tua":85
}
print(marks["Soumitri"])
# print(marks,type(marks))   #{'Soumitri': 90, 'Tua': 85} <class 'dict'>
# print(marks.items())    #dict_items([('Soumitri', 90), ('Tua', 85)])
# print(marks.keys())        #dict_keys(['Soumitri', 'Tua'])
# print(marks.values())       #dict_values([90, 85])
marks.update({"Soumitri":99})
print(marks)