from sqlalchemy import String ,Integer,Column,Boolean


from database import Base,engine

def create_table():
    Base.metadata.create_all(engine)
    

class users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(15),nullable=False)
    fullname=Column(String(30),nullable=False)
    is_franchiser=Column(Boolean,default=False)#sami
    is_deler=Column(Boolean,default=False)#humayun,sami,talha,
    area_name=Column(String(40),nullable=False)
    password=Column(String(200),nullable=False)
    
class customer(Base):
    __table_name__='customers'
    id=Column(Integer,primary_key=True)
    customer_code=Column(Integer,unique=True),range(1000-9999)
    deler_customer=Column(Integer,users.id.append_foreign_key)
    customer_fullname=Column(String(30),nullable=False)
    customer_area=Column(String(30),nullable=False)
    customer_address=Column(String(200),nullable=False)
    customer_phone=Column(Integer(13),nullable=True)



class SubAreas(Base):
    __table_SubAreas__='SubAres'
    id=Column(Integer,primary_key=True)
    area_name=Column(Integer,users.id.append_foreign_key)
    SubAreas_name=Column(String(30),nullable=False)

class employee(Base):
    id=Column(Integer,primary_key=True)
    deler_employee=Column(Integer,users.id.append_foreign_key)  
    employee_name=Column(String(30),nullable=False)
    employee_phone=Column(Integer(13),nullable=True)








