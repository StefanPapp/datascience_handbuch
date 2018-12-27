from person import Person
from datetime import date
import hashlib


def main():
    p = Person("Bill", "Gates", date(1955, 10, 28))
    print("Hello {}".format(p.first_name))
    p.last_name = hashlib.md5(p.last_name.encode()).hexdigest()
    print(p.last_name)

if __name__ == '__main__':
    main()
