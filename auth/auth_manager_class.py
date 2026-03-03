from storage.storage_class import Storage
from auth.user_class import User


class AuthManager:

    def __init__(self, storage: Storage):
        self.storage = storage
        self.logged_in_user = None

    def register(self, name: str, email: str, password: str, role: str = "user") -> bool:
        users = self.storage.load_users()

        if any(u.email == email for u in users):
            print("Email already registered.")
            return False

        user = User(name=name, email=email, password=password, role=role)
        users.append(user)
        self.storage.save_users(users)
        print(f"User `{name}` registered successfully.")
        return True

    def login(self, email: str, password: str) -> bool:
        users = self.storage.load_users()

        for user in users:
            if user.email == email:
                if user.verify_password(password):
                    self.logged_in_user = user
                    print(f"User `{email}` successfully logged in.")
                    return True
                else:
                    print("Incorrect password.")
                    return False

        print("User does not exist.")
        return False

    def logout(self):
        self.logged_in_user = None
        print("Logged out.")

    def is_admin(self) -> bool:
        return self.logged_in_user and self.logged_in_user.role.lower() == "admin"