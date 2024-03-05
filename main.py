from group import Group, OverStudentError
from student import Student

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

try:
    for _ in range(11):
        gr.add_student(st1)
except OverStudentError as e:
    print(e)

gr.add_student(st2)

print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student