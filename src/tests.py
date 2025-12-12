from contact import Contact
from contact_book import ContactBook


def run_all_tests():
    book = ContactBook()

    assert book.find_by_phone("000") is None
    assert book.delete_contact("000") is False

    c1 = Contact("Alice", "111", "alice@example.com")
    c2 = Contact("Bob", "222", "bob@example.com")
    c3 = Contact("Alice", "333", "alice2@example.com")

    book.add_contact(c1)
    book.add_contact(c2)
    book.add_contact(c3)

    assert book.find_by_phone("111") is c1
    assert len(book.find_by_name_linear("alice")) == 2

    assert book.delete_contact("222") is True
    assert book.find_by_phone("222") is None

    sorted_contacts = book.get_all_sorted_by_name()
    names = [c.name for c in sorted_contacts]
    assert names == sorted(names, key=str.lower)

    print("All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()
