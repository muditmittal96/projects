

from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy import ForeignKey
from task.base import Base


class Dictionary(Base):

    __tablename__ = 'dictionary'

    UID = Column(Integer(), primary_key=True, autoincrement=False)
    Ticker = Column(String(100), nullable=False, unique=False)
    Market = Column(String(15), default='Index')
    Field = Column(String(50), default='PX_LAST')
    Currency = Column(String(5), nullable=True, unique=False, default='USD')
    Periodicity = Column(String(20), nullable=True, unique=False, default='DAILY')
    Calendar = Column(String(50), nullable=False, unique=False, default='NYSE')
    DayCount = Column(String(20), nullable=False, unique=False, default='Business252')

    def __repr__(self):
        repr = (
            f'<Dictionary(UID={self.UID}, Ticker={self.Ticker}, '
            f'Market={self.Market}, Field={self.Field}, '
            f'Description={self.Description}, '
            f'Currency={self.Currency}, Periodicity={self.Periodicity}, '
            f'Calendar={self.Calendar}, DayCount={self.DayCount})>'
        )
        return repr


class Prices(Base):

    __tablename__ = 'prices'

    UID = Column(Integer(), ForeignKey('dictionary.UID'), primary_key=True)
    AsOfDateTime = Column(DateTime(), primary_key=True)
    Price = Column(Numeric(18, 6))

    def __repr__(self):
        return f'<Prices(UID={self.UID}, AsOfDateTime={self.AsOfDateTime}, Price={self.Price})>'