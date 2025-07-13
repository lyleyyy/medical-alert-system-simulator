
from hospital_base import HospitalBase
from patient import Patient


class Node:
    def __init__(self, patient):
        self.patient = patient
        self.next = None
        self.prev = None


class Hospital_2 (HospitalBase):

    def __init__(self):
        super().__init__()
        self.head = None

    def __iter__(self):
        """
            Add your code here!
        """
        cur = self.head
        while cur != None:
            yield cur.patient
            cur = cur.next

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """
        hrs = patient.time.split(":")[0]
        if hrs != "12" and hrs >= "08" and hrs < "18":
            # first empty
            if self.head == None:
                self.head = Node(patient)
                return True

            elif patient.time < self.head.patient.time:
                new_head = Node(patient)
                new_head.next = self.head
                self.head.prev = new_head
                self.head = new_head
                return True

            # elif patient.time == self.head.patient.time:
            #     new_patient = Node(patient)
            #     new_patient.next = self.head.next
            #     new_patient.prev = self.head
            #     self.head.next.prev = new_patient
            #     self.head.next = new_patient
            #     print(3)

            else:
                cur = self.head
                while cur != None:
                    if patient.time < cur.patient.time:
                        new_patient = Node(patient)
                        cur.prev.next = new_patient
                        new_patient.next = cur
                        new_patient.prev = cur.prev
                        cur.prev = new_patient
                        return True

                    elif patient.time == cur.patient.time:
                        new_patient = Node(patient)
                        cur.next.prev = new_patient
                        new_patient.next = cur.next
                        new_patient.prev = cur
                        cur.next = new_patient
                        return True

                    elif (patient.time > cur.patient.time) and cur.next == None:
                        new_patient = Node(patient)
                        new_patient.prev = cur
                        cur.next = new_patient
                        return True

                    else:
                        cur = cur.next
        else:
            return False

            # ==============================  Add any extra functions below   ==============================


# if __name__ == "__main__":
#     """
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             The following main function is provided for simple debugging only
#     """
#     ll = Hospital_2()
#     ll.add_patient(Patient("Max", "11:00"))
#     ll.add_patient(Patient("Alex", "13:15"))
#     ll.add_patient(Patient("George", "13:00"))
#     ll.add_patient(Patient("PePe", "10:00"))
#     ll.add_patient(Patient("George888", "08:00"))
#     ll.add_patient(Patient("QQ", "15:00"))
#     ll.add_patient(Patient("AA", "14:00"))
#     list_of_patients = [Patient("Max", "11:00"), Patient("George", "13:00"), Patient(
#         "Alex", "13:15"), ]
    # cur = ll.head
    # while cur != None:
    #     print(cur.patient)
    #     cur = cur.next
#     for i, el in enumerate(ll):
#         # print(el)
#         assert el == list_of_patients[i]
