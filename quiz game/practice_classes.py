# class User:
#     pass


# user_1 = User()
# user_1.id = '001'
# user_1.username = 'David'


# print(user_1.username)


# user_2 = User()

# user_2.id  = '002'
# user_2.username = 'Solomon'
# print(user_2.username)


class User:
    """Blueprint for modeling website users"""
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        """increase following and user being followed follower count"""
        user.follower += 1
        self.following += 1

    def unfollow(self, user):
        """decrease following and user being followed follower count"""
        user.follow -= 1
        self.following -= 1



user_1 = User('001', 'Moses')
user_2 = User('002', 'Esther')

user_1.follow(user_2)


print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
