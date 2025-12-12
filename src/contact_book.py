from typing import Dict, List, Optional
from contact import Contact


class ContactBook:
    """
    ContactBook stores contacts using two main approaches:
      - A hash table (Python dictionary) for O(1) average lookup by phone.
      - A dynamic list when alphabetical sorting is required.
    This matches the requirements of the coursework and demonstrates
    algorithmic performance clearly.
    """

    def __init__(self):
        # Dictionary for fast access by phone number
        self._contacts_by_phone: Dict[str, Contact] = {}

    # ------------------------------------------------------------
    # INSERT CONTACT
    # O(1) average time
    # ------------------------------------------------------------
    def add_contact(self, contact: Contact) -> None:
        """
        Add or update a contact based on phone number.
        If the phone already exists, the contact is overwritten.
        """
        self._contacts_by_phone[contact.phone] = contact

    # ------------------------------------------------------------
    # SEARCH BY PHONE
    # O(1) average time
    # ------------------------------------------------------------
    def find_by_phone(self, phone: str) -> Optional[Contact]:
        """Return the contact with that phone number, or None if not found."""
        return self._contacts_by_phone.get(phone)

    # ------------------------------------------------------------
    # SEARCH BY NAME
    # O(n) time - linear search
    # ------------------------------------------------------------
    def find_by_name_linear(self, name: str) -> List[Contact]:
        """
        Linear search by name (case-insensitive).
        This demonstrates O(n) scanning over the data structure.
        """
        name_lower = name.lower()
        matches = [
            c for c in self._contacts_by_phone.values()
            if c.name.lower() == name_lower
        ]
        return matches

    # ------------------------------------------------------------
    # DELETE CONTACT
    # O(1) average time
    # ------------------------------------------------------------
    def delete_contact(self, phone: str) -> bool:
        """
        Delete a contact by phone number.
        Returns True if the contact existed and was deleted.
        Returns False if the contact was not found.
        """
        if phone in self._contacts_by_phone:
            del self._contacts_by_phone[phone]
            return True
        return False

    # ------------------------------------------------------------
    # SORTED LIST OF CONTACTS
    # O(n log n) time (Timsort)
    # ------------------------------------------------------------
    def get_all_sorted_by_name(self) -> List[Contact]:
        """
        Returns all contacts sorted alphabetically by name.
        Sorting uses Python's Timsort with O(n log n) complexity.
        """
        return sorted(
            self._contacts_by_phone.values(),
            key=lambda c: c.name.lower()
        )
