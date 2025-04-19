from datetime import date

def decorator (func):
    def wrapper (user):
        try:
            if (user.age > 18):
                print ('Person is of legal age')
            else:
                raise ValueError()
        except ValueError:
            print ('Person is minor')

        func(user)

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
    print (f"Age: {user.age}")


my_user = User(date(1990, 1, 1))

print_user_age (my_user)