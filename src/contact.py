class Contact:
    def __init__(self, name: str, phone: str, email: str, address: str = ""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self) -> str:
        return f"Contact(name={self.name!r}, phone={self.phone!r})"
