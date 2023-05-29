import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)
    books_pub = relationship("Book", back_populates="publisher_book")

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    publisher_book = relationship('Publisher', back_populates="books_pub")
    stocks_book = relationship('Stock', back_populates="book_stock")

    def __str__(self):
        return f'{self.id}: {self.title}, {self.id_publisher}'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)
    stocks_shop = relationship('Stock', back_populates="shop_stock")

    def __str__(self):
        return f'{self.id}: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    book_stock = relationship('Book', back_populates="stocks_book")
    shop_stock = relationship('Shop', back_populates="stocks_shop")
    sales_stock = relationship('Sale', back_populates="stock_sale")

    def __str__(self):
        return f'{self.id}: {self.id_book}, {self.id_shop}, {self.count}'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    data_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    stock_sale = relationship('Stock', back_populates="sales_stock")

    def __str__(self):
        return f'{self.id}: {self.price}, {self.data_sale}, {self.id_stock}, {self.count}'

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

