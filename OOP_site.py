class User:
    def __init__(self, first_name, last_name, email, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"Ім'я: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}, Вік: {self.age}, Місто: {self.city}")

    def greeting_user(self):
        print(f"Вітаємо, {self.first_name} {self.last_name}! Раді бачити вас на сайті.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Список привілеїв адміністратора:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, email, age, city, privileges=None):
        super().__init__(first_name, last_name, email, age, city)
        self.priv = Privileges(privileges)