from faker import Faker
faker = Faker()



class Payloads:

    # использовать методы для гибкости. можно юзать как свои значения, так и дефолтные (пример в принте)
    def create_user(self, email: str = faker.email(), nickname: str = faker.user_name() ):
        return {
            "email": email,
            "password": faker.password(),
            "name": faker.name(),
            "nickname": nickname
        }

#print(Payloads().create_user())  или print(Payloads().create_user(email = "olala@ya.ru"))