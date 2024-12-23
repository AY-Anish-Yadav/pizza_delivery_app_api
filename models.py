from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy_utils import ChoiceType
from database import Base

# User Model
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    
    # Relationship to Order
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"

# Order Model
class Order(Base):
    __tablename__ = 'orders'
    
    # Choices for order statuses
    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'delivered')
    )

    # Choices for pizza sizes
    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large')
    )
    
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="SMALL")
    user_id = Column(Integer, ForeignKey('user.id'))
    
    # Relationship to User
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"

