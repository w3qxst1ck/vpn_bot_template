from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship, backref

from admin.database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(String, unique=True, index=True)
    tg_nickname = Column(String, nullable=True)
    tg_firstname = Column(String, nullable=True)
    is_blocked = Column(Boolean, default=False)

    profile = relationship("Profile", backref=backref("user", uselist=False))

    operations = relationship("Operations", back_populates="user")

    def __repr__(self):
        return f'{self.id}. {self.tg_id} {self.tg_firstname}'


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    subscribe_expire_date = Column(DateTime)
    vpn_key = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)
    switched_off = Column(Boolean, default=False)
    free = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.id}. {self.user_id} {self.subscribe_expire_date} {self.is_active}'


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    amount = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'), unique=False, nullable=False)
    user = relationship("User", back_populates="operations", cascade="all,delete", lazy="dynamic")

    def __repr__(self):
        return f'{self.id}. {self.user_id} {self.date} {self.amount}'


class Server(Base):
    __tablename__ = 'servers'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    country = Column(String, nullable=False)
    ip_addr = Column(String, nullable=False)

    def __repr__(self):
        return f'{self.id}. {self.title} {self.country} {self.ip_addr}'
