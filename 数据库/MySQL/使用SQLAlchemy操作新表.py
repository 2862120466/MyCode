"""
SQLAlchemy是一个用来连接数据库的模块，它对数据的操作十分简单
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,Integer,String,Boolean,DateTime # 导入字段类
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_engine('mysql+pymysql://root:682240@localhost:3306/practice?charset=utf8') # 建立连接
Base = declarative_base() # 创建模型的基类
# Session = sessionmaker(bind=engine)

class News(Base):
    __tablename__ = 'news' # 表名为news

    # 字段
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300), )
    author= Column(String(10), )
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

class OrmTest(object):

    def __init__(self):
        self.session = Session(engine)

    def add_one(self):
        new_obj = News(
            title='标题5',
            content='内容5',
            types='happy',
            author='wcc',
            view_count=1,
            is_valid=True,
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        return self.session.query(News).get(1)

    def get_more(self):
        return  self.session.query(News).filter_by(view_count=1)

    def update_data(self):
        data = self.session.query(News).get(1)
        data.title = '修改后的标题'
        self.session.add(data)
        self.session.commit()

    def delete_data(self):
        data = self.session.query(News).get(2)
        self.session.delete(data)
        self.session.commit()

def main():
    obj = OrmTest()

    # rest = obj.add_one()
    # print(rest.id)

    # obj.update_data()

    # obj.delete_data()

    # rest2 = obj.get_one()
    # if rest2:
    #     print(rest2.id,rest2.title)
    # else:
    #     print("Not exist.")

    data = obj.get_more()
    print('查询出了%s条数据'%data.count())
    for i in data:
        print(i.id, i.title, i.content, i.is_valid)


if __name__ == '__main__':
    # News.metadata.create_all(engine)  # 创建表
    main()