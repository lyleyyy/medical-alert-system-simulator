from alert_system_base import AlertSystemBase, User


class AlertSystem(AlertSystemBase):

    def __init__(self):
        super().__init__()
        self.users = []
        self.matrix = []
    """
        Implement the described functions here !
    """

    def add_person(self, person: User):
        """
        Adds a person to the system.
        :return: True if the person was successfully added,
                 False if they are already in the system
        """
        if person in self.users:
            return False

        elif self.users == [] and self.matrix == []:
            self.users.append(person)
            self.matrix = [[0]]
            return True

        else:
            self.users.append(person)
            for i in self.matrix:
                i.append(0)
            self.matrix.append([0]*len(self.users))
            return True

    def remove_person(self, person: User):
        """
        Removes a person to the system.
        :return: True if a person is successfully removed,
                 False if they were not in the system
        """
        if person not in self.users:
            return False

        else:
            self.users.remove(person)
            index = self.users.index(person)
            for i in self.matrix:
                i.pop(index)
            self.matrix.pop(index)
            return True

    def add_contact(self, person1: User, person2: User):
        """
        Adds a contact between two people.
        :return: True if a contact is successfully added,
                 False otherwise
        """
        if person1 in self.users and person2 in self.users:
            index1 = self.users.index(person1)
            index2 = self.users.index(person2)
            self.matrix[index1][index2] = 1
            self.matrix[index2][index1] = 1
            return True

        else:
            return False

    def count_contacts(self, person: User):
        """
        Counts how many contacts the person has.
        :return: the number of contacts the person has, or
                 -1 if the person is not in the system
        """
        if person not in self.users:
            return -1

        else:
            count = 0
            index = self.users.index(person)
            for i in self.matrix:
                if i[index] == 1:
                    count += 1

            for i in self.matrix[index]:
                if i == 1:
                    count += 1

            if self.matrix[index][index] == 1:
                count -= 1

            return int(count / 2)

    def remove_contact(self, person1: User, person2: User):
        """
        Removes a contact between two people.
        :return: True if the contact was successfully removed,
                 False otherwise
        """
        if person1 in self.users and person2 in self.users:
            index1 = self.users.index(person1)
            index2 = self.users.index(person2)
            self.matrix[index1][index2] = 0
            self.matrix[index2][index1] = 0
            return True

        else:
            return False

    def mark_infected(self, infected_person: User, virus_degree: int = 0):
        """
        Marks a person as infected.
        Based on the virus degree, marks infected:
                virus_degree = 1: the infected person's contacts,
                virus_degree = 2: the infected person's contacts and the contacts of the contacts,
                virus_degree = 3: the infected person's contacts, the contacts of the contacts, and
                                 the contacts of the contacts of the contacts,
                and so on.
        """
        if virus_degree == 0:
            # self.add_contact(infected_person)
            self.users[self.users.index(infected_person)].got_virus()

        elif virus_degree == 1:
            self.users[self.users.index(infected_person)].got_virus()
            self.find_contact(infected_person)

        # else:
        #     # infected_persons = []
        #     # self.add_contact(infected_person)
        #     self.users[self.users.index(infected_person)].got_virus()
        #     while virus_degree > 0:
        #         contact_persons = self.find_contact(infected_person)

    def find_contact(self, infected_person: User):
        contact_persons = []
        index = self.users.index(infected_person)
        contact_check_list = self.matrix[index]
        for i in contact_check_list:
            if i == 1:
                contact_person = self.users[contact_check_list.index(i)]
                contact_person.got_virus()
                contact_persons.append(contact_person)

        return contact_persons


# if __name__ == "__main__":
#     """
#         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER
#         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         The following main function is provided for simple debugging only
#     """

#     alert = AlertSystem()
#     u1, u2 = User("Alex"), User("Max")
#     u3, u4 = User("Nick"), User("Bing")
#     users = [u1, u2, u3, u4]
#     for u in users:
#         alert.add_person(u)
#     # alert.add_contact(u1, u2)
#     # alert.add_contact(u1, u3)
#     # alert.add_contact(u2, u4)
#     # assert alert.count_contacts(u1) == 2
#     # alert.mark_infected(u1, virus_degree=1)
#     # assert u1.infected
#     # assert u2.infected
#     # assert not u4.infected
