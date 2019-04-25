from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

 # 连接数据库
engine = create_engine('mysql+pymysql://root:682240@localhost/practice')

 # 映射到表boys
Base = automap_base()
Base.prepare(engine, reflect=True)
Boys = Base.classes.boys

session = Session(engine) # 设置session中间件

# ret = session.query(Boys).get(1)
# ret.boyName = '吴长城'
# session.add(ret)
# session.commit()

ret_more = session.query(Boys).filter(id != 0) # 取值

for data in ret_more:
    print(dir(data))