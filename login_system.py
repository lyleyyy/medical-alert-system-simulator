from login_system_base import LoginSystemBase


class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password


class LoginSystem (LoginSystemBase):

    def __init__(self):
        super().__init__()
        self.user = None
        # self.hash_table = HashTable(101)
        self.size = 101
        self.users = [None for i in range(self.size)]
        self.counter = 0

    """
        Implement the described functions here !
    """

    def __len__(self):
        """
        Returns the actual size of the data structure, including empty elements
        :return: the size of the data structure
        """
        # raise NotImplementedError('must be implemented by subclass')
        return self.size

    def get_num_of_users(self):
        """
        Returns the number of users currently in the system
        :return: integer, representing the number of users
        """
        # raise NotImplementedError('must be implemented by subclass')
        num_of_users = 0
        for i in self.users:
            if isinstance(i, User):
                num_of_users += 1
        return num_of_users

    @staticmethod
    def hash_codes(key: str):
        """
        Calculates the hashcode based on the key
        :param key:
        :return: hashcode integer
        """
        c = 31
        string_value = 0
        for i in key:
            string_value = (string_value + ord(i)) * c
        string_value = string_value / c
        return string_value

    def add_user(self, email, password):
        """
        Adds a new user to the system.
        :return: False if the user is already in the system
                 True if the user was not in the system and has been successfully added
        """
        # raise NotImplementedError('must be implemented by subclass')

        # False if already in the system
        for i in self.users:
            if isinstance(i, User) and i.email == email:
                return False

        # get the hash codes and calculate the index
        index = int(self.hash_codes(email) % self.size)

        # if the index position is not yet taken, add user
        if self.users[index] == None:
            self.users[index] = User(email, int(self.hash_codes(password)))

        else:
            # if the index position is already taken
            while self.users[index]:
                index += 1
                if index == self.size - 1:
                    index = 0

            # add the user and counter + 1
            self.users[index] = User(email, int(self.hash_codes(password)))
            self.counter += 1

            # if the array if full then need to triple resize
            if self.counter == self.size:
                self.new_users = [None for i in range(self.size * 3)]
                for i in range(self.size):
                    self.new_users[i] = self.users[i]

                self.users = self.new_users
                self.size = self.size * 3

        return True

    def remove_user(self, email, password):
        """
        Removes a user from the system.
        :return: True if the user was successfully removed
                 False if the user was not in the system OR the email is in the system, but the password is incorrect
        """
        # raise NotImplementedError('must be implemented by subclass')
        for i in range(self.size):
            if isinstance(self.users[i], User):
                user = self.users[i]
                if user.email == email and user.password == int(self.hash_codes(password)):
                    self.users[i] = None
                    return True

        return False

    def check_password(self, email, password) -> int:
        """
        Checks if the user is in the system.
        Returns the bucket index of the user in the hashtable.
        :param email, password: strings
        :return: if the user is not in the system
                    -> return -1

                 if the user is in the system, but the password is incorrect
                    -> return -2

                 if the user is in the system and the password is correct
                    -> return the bucket index of the user in the hashtable
        """
        # raise NotImplementedError('must be implemented by subclass')

        check_user = None

        for i in range(self.size):
            if isinstance(self.users[i], User):
                user = self.users[i]
                if user.email == email:
                    check_user = self.users[i]

        if check_user == None:
            return -1
        else:
            if check_user.password != self.hash_codes(password):
                return -2
            else:
                return int(self.hash_codes(user.email) % self.size)

        # if len(check_users) == 0:
        #     return -1

        # for i in check_users:
        #     if i.password == self.hash_codes(password):
        #         return self.hash_codes(user.email)

        # return -2

        # for i in range(self.size):
        #     if isinstance(self.users[i], User):
        #         user = self.users[i]
        #         if user.email == email and user.password == self.hash_codes(password):
        #             return self.hash_codes(user.email)

    def change_password(self, email, old_password, new_password) -> bool:
        """
        Changes the user's password in the system to 'new_password'.
        :param email: string
        :param old_password: string
        :param new_password: string
        :return: True if the user's password was changed successfully
                 False if the user could not be found or 'old_password' is incorrect
        """
        for i in range(self.size):
            if isinstance(self.users[i], User):
                user = self.users[i]
                if user.email == email and user.password == self.hash_codes(old_password):
                    user.password = self.hash_codes(new_password)
                    return True

        return False


# class User(object):
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password


# class HashTable(object):
#     def __init__(self, size):
#         self.size = size
#         self.users = [None for i in range(self.size)]
#         self.counter = 0

#     def hash_index(self, key):
#         return key % self.size

#     def insert(self, key, value):
#         index = self.hash_index(key)
#         while self.users[index]:
#             index += 1
#             if index == self.size - 1:
#                 index = 0

#         self.users[index] = value
#         counter += 1

#         # triple resize the array if full
#         if counter == self.size:
#             self.newUsers = [None for i in range(self.size * 3)]
#             for i in range(self.size):
#                 self.newUsers[i] = self.users[i]

#             self.users = self.newUsers
#             self.size = self.size * 3

# if __name__ == "__main__":
#     """
#         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER
#         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         The following main function is provided for simple debugging only
#     """

#     login = LoginSystem()

#     assert login.hash_codes("GQHTMP") == login.hash_codes("H2HTN1")
#     assert len(login) == 101
#     assert login.check_password("a@b.c", "L6ZS9") == -1
#     login.add_user("a@b.c", "L6ZS9")
#     assert login.check_password("a@b.c", "ZZZZZZ") == -2
#     assert login.check_password("a@b.c", "L6ZS9") == 94
#     login.remove_user("a@b.c", "L6ZS9")
#     assert login.check_password("a@b.c", "L6ZS9") == -1
