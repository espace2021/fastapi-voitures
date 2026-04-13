from beanie import Document

class User(Document):
    name: str
    email: str
    password: str
    role: str = "user"
    

    class Settings:
        name = "users"          # nom de la collection dans MongoDB