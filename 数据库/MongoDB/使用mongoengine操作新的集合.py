from mongoengine import connect, Document, EmbeddedDocument
from mongoengine import StringField, IntField, FloatField, ListField, EmbeddedDocumentField

connect('runoob')

SEX_CHOICES = (
    ('male', '男'),
    ('famale', '女')
)

class Grade(EmbeddedDocument):
    ''' 成绩 '''
    subject = StringField(required=True)
    score = FloatField(required=True)


class Student(Document):
    ''' 学生 '''
    name = StringField(required=True, max_length=32)
    age= IntField(required=True)
    sex = StringField(required=True, choices=SEX_CHOICES)
    grade = FloatField()
    grades = ListField(EmbeddedDocumentField(Grade))
    address = StringField()

class Operations():
    def add_one(self):
        chinese = Grade(
            subject='语文',
            score=80)
        english = Grade(
            subject='英语',
            score=80)

        stu_obj = Student(
            name='hjt',
            age=20,
            sex='male',
            grades=[chinese,english])
        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()

    def get_more(self):
        return Student.objects.all()

    def get_one_form_name(self, name):
        return Student.objects.filter(name = name).first()

    def update_one(self):
        ''' 修改第一条数据 '''
        rest = Student.objects.filter(sex='male').update_one(inc__age=1)
        return rest

    def update_more(self):
        # rest = Student.objects.filter(name='hjt').update(name='hjt_改')
        rest = Student.objects.filter(name='hjt').update(inc__age=1)
        return rest

    def delete_one(self):
        rest = Student.objects.filter(sex='male').first().delete

    def delete_more(self):
        rest = Student.objects.filter(sex='male').delete
if __name__ == '__main__':
    o = Operations()
    # o.add_one()

    # stu = o.get_one()
    # print(dir(stu))

    # stu = o.get_more()
    # [print(data.name, data.grades[1].subject) for data in stu]

    # print(o.get_one_form_name('wcc').age)

    o.update_more()