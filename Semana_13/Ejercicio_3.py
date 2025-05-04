from datetime import date

def decorator (func):
    def wrapper (user):
        # is_adult = True
        try:
            if (user.age > 18):
                # is_adult = True
                print ('Person is of legal age')
                user_age = func(user)
                print (f'His/Her age is: {user_age}')
                return user_age
            else:
                # is_adult = False
                raise ValueError()
        except ValueError:
            print ('Person is minor')
            return

        # if (is_adult):
        #     user_age = func(user)
        #     print (f'Your age is: {user_age}')
        # func(user)

    return wrapper

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):

        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


@decorator
def print_user_age (user):
    return user.age
    # print (f"Age: {user.age}")


my_user = User(date(1990, 1, 1))

print('\n')
print_user_age (my_user)

my_user_2 = User(date(2015, 1, 1))

print('\n')
print_user_age (my_user_2)