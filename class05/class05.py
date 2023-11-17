data_base: list[tuple[str, str]] = [("Qasim", '123'),
                                    ("sir zia", '567'), ("ikhlas", '342')]
input_user: str = input("Enter user name")
input_password: str = input("Enter password")
for row in data_base:
    user, password = row
    if input_user == user and input_password == password:
        print("valid User")
        break
else:
    print("Invalid user name")
