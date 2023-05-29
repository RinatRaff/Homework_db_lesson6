import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:Tremkazan/ruRafik@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name='Пушкин')
publisher2 = Publisher(name='Достоевский')
publisher3 = Publisher(name='Гоголь')
session.add_all([publisher1, publisher2, publisher3])

book1 = Book(title='Капитанская дочка', publisher_book=publisher1)
book2 = Book(title='Руслан и Людмила', publisher_book=publisher1)
book3 = Book(title='Евгений Онегин', publisher_book=publisher1)
book4 = Book(title='Мцыри', publisher_book=publisher2)
book5 = Book(title='Мертвые души', publisher_book=publisher3)
session.add_all([book1, book2, book3, book4, book5])

shop1 = Shop(name='Буквоед')
shop2 = Shop(name='Лабиринт')
shop3 = Shop(name='Книжный дом')
session.add_all([shop1, shop2, shop3])

stock1 = Stock(count=5, book_stock=book1, shop_stock=shop1)
stock2 = Stock(count=7, book_stock=book1, shop_stock=shop2)
stock3 = Stock(count=8, book_stock=book2, shop_stock=shop1)
stock4 = Stock(count=12, book_stock=book3, shop_stock=shop3)
stock5 = Stock(count=11, book_stock=book4, shop_stock=shop2)
stock6 = Stock(count=13, book_stock=book5, shop_stock=shop3)
session.add_all([stock1, stock2, stock3, stock4, stock5, stock6])

sale1 = Sale(price=600, data_sale='09.11.2022', count=1, stock_sale=stock1)
sale2 = Sale(price=500, data_sale='08.11.2022', count=1, stock_sale=stock3)
sale3 = Sale(price=580, data_sale='05.11.2022', count=1, stock_sale=stock2)
sale4 = Sale(price=490, data_sale='02.11.2022', count=1, stock_sale=stock4)
sale5 = Sale(price=600, data_sale='26.11.2022', count=1, stock_sale=stock1)
sale6 = Sale(price=611, data_sale='25.11.2022', count=1, stock_sale=stock5)
sale7 = Sale(price=612, data_sale='24.11.2022', count=1, stock_sale=stock6)
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7])

session.commit()


publisher = input('Имя издателя: ')
for c in session.query(Book.title, Shop.name, Sale.price, Sale.data_sale)\
        .join(Stock.sales_stock).join(Stock.shop_stock).join(Stock.book_stock).join(Book.publisher_book)\
        .filter(Publisher.name.like(f'{publisher}')):
     print(c)



session.close