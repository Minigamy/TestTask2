from sqlalchemy import Integer, BigInteger, VARCHAR, Text
from sqlalchemy.sql.schema import Column, ForeignKey
from database import Base


class Anagram(Base):
    __tablename__ = "anagram"

    id = Column(Integer, primary_key=True)
    count = Column(Integer)


class Devices(Base):
    __tablename__ = "devices"

    id = Column(BigInteger, primary_key=True)
    dev_id = Column(VARCHAR(200), nullable=False)
    dev_type = Column(VARCHAR(120), nullable=False)


class Endpoints(Base):
    __tablename__ = "endpoints"

    id = Column(BigInteger, primary_key=True, nullable=False)
    device_id = Column(Integer, ForeignKey('devices.id', ondelete="cascade", onupdate="cascade"), default=None)
    comment = Column(Text, default=None)
