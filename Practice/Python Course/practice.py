import pickle
import json

str1='''
Hello I am Wahaj            
and Currently I am learning Python Course 
and this is a practice file 
I am doing this practice file to learn the basics of Python
I am learning Python from Udemy
I will complete this course and will become a Pythona Developer
This is my first practice file I hope I will learn a lot from this course
from Udemy
'''
print(str1)
num=10.5j
print(num,type(num))

num2=10.5
print(num2,type(num2))

num3=complex(10,20)
print(num3,type(num3))

dict_example = {'name': ['Wahaj', 'Ali'], 'course': ['Python','Js'], 'progress': ['learning','completed']}
print(dict_example['course'][1], type(dict_example))
del dict_example['progress'][0]
print(dict_example)


list_example = ['Wahaj', 'Ali', 'Python', 'JavaScript']
list_example.append('Java')
print(list_example, type(list_example))
set_example = {'Wahaj', 'Ali', 'Python', 'JavaScript'}
print(set_example, type(set_example))
tuple_example = ('Wahaj', 'Ali', 'Python', 'JavaScript')
print(tuple_example, type(tuple_example))
str='hy'
str2='hy'
print(str is  str2)  # This checks if both variables point to the same object in memory

print(str1.index('h'))
firstName = 'Wahaj'
course= 'Python'
string='My Name is {} and I am learning {}'.format(firstName,course)
print(string)
List=[['Hello Word','No Hello World'],['Hey','No Hey']]
print(List[0][1][3:8:1])
List1=[10,20,30,40,50,30]
List2=[11,22,33,44,55,66]
#List.remove(30)
print(List)
for a,b in zip(List1,List2):
    print(a,b)
set={10,20,30,40,50,60}
set.discard(22)
print(set)
set.update([11,22,33,44,55,66])
print(set)

data={
    'name': 'Wahaj',
    'age': 21,
    'courses': ['Python', 'JavaScript'],
    'is_student': True
}
with open('data.txt','wb') as file:
    pickle.dump(data, file)
with open('data.txt','rb') as file:
    data = pickle.load(file)
print(data)



serialized = pickle.dumps(data)
deserialized = pickle.loads(serialized)
print(deserialized)

# Serialize data to JSON and write to file
with open('data.json','w') as f:
    json.dump(data, f, indent=4)
print('Data has been written to data.json using json.dump')

# Read data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
print('Data loaded from data.json using json.load:', data)

# Serialize data to JSON string and write to file
with open('data.json','w') as f:
    json_string=json.dumps(data, indent=4)
    f.write(json_string)
print('Data has been written to data.json using json.dumps')

# Read JSON string from file and deserialize
with open('data.json', 'r') as f:
    json_string = f.read()
    data = json.loads(json_string)
print('Data loaded from data.json using json.loads:', data)
