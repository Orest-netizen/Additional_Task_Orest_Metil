from OOP_site import User,Admin

user1 = User("Володимир", "Золотий", "volodya@email.com", 25, "Тернопіль")
user2 = User("Тетяна", "Прібиткова", "tanya@email.com", 19, "Харків")
user3 = User("Данило", "Андрійчук", "danya@email.com", 32, "Садґора")

user1.describe_user()
user1.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()

test_user = User("Іван", "Іванов", "ivan@email.com", 28, "Харків")
test_user.increment_login_attempts()
test_user.increment_login_attempts()
test_user.increment_login_attempts()
print(test_user.login_attempts)

test_user.reset_login_attempts()
print(test_user.login_attempts)

admin = Admin("Орест", "Сидоренко", "admin@email.com", 40, "Дніпро")
admin.priv.show_privileges()
