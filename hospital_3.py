
from hospital_base import HospitalBase
from patient import Patient


class Hospital_3 (HospitalBase):

    def __init__(self):
        super().__init__()
        self.patients = []
        self.counterIndex = 0

    def __iter__(self):
        """
            Add your code here!
        """
        self.patients = self.patients[:(len(self.patients)-1)]
        self.patients = self.merge_sort(self.patients)
        for i in self.patients:
            if isinstance(i, Patient):
                yield i

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """
        hrs = patient.time.split(":")[0]
        if hrs != "12" and hrs >= "08" and hrs < "18":
            if len(self.patients) == 0:
                # if isinstance(self.patients[0], str) and self.patients[0] == "Available":
                self.patients += ["Available"]
                self.patients[self.counterIndex] = patient
                self.patients += ["Available"]
                self.counterIndex += 1
                return True
            else:
                self.patients[self.counterIndex] = patient
                self.patients += ["Available"]
                self.counterIndex += 1
                return True

    # ==============================  Add any extra functions below   ==============================
    # def remove_duplicate(self, list_of_patients):
    #     copy_of_patients = list_of_patients * 1
    #     for i in range(0, len(list_of_patients)):
    #         if isinstance(list_of_patients[i], Patient):
    #             for j in copy_of_patients:
    #                 if isinstance(j, Patient) and j.time == list_of_patients[i].time and copy_of_patients.index(j) != i:
    #                     list_of_patients[copy_of_patients.index(
    #                         j)] = "Available"
    #     return list_of_patients

    def merge_sort(self, arr):

        if len(arr) > 1:
            left_arr = arr[:len(arr) // 2]
            right_arr = arr[len(arr) // 2:]

            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
            self.merge(left_arr, right_arr, arr)

        return arr

    def merge(self, left_arr, right_arr, arr):

        i = 0
        l = 0
        r = 0

        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l].time <= right_arr[r].time:
                arr[i] = left_arr[l]
                l += 1
            else:
                arr[i] = right_arr[r]
                r += 1
            i += 1

        while l < len(left_arr):
            arr[i] = left_arr[l]
            l += 1
            i += 1

        while r < len(right_arr):
            arr[i] = right_arr[r]
            r += 1
            i += 1


# if __name__ == "__main__":
#     """
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             The following main function is provided for simple debugging only
#         """
#     ll = Hospital_3()
#     ll.add_patient(Patient("Max", "11:00"))
#     ll.add_patient(Patient("Alex", "13:15"))
#     ll.add_patient(Patient("George", "14:00"))
#     list_of_patients = [Patient("Max", "11:00"), Patient(
#         "Alex", "13:15"), Patient("George", "14:00")]
#     for i, el in enumerate(ll):
#         assert el == list_of_patients[i]

# if __name__ == "__main__":
#     """
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             The following main function is provided for simple debugging only
#         """
#     ll = Hospital_3()
#     ll.add_patient(Patient("Max", "11:00"))
#     ll.add_patient(Patient("Alex", "13:15"))
#     ll.add_patient(Patient("Lyle", "14:00"))
#     ll.add_patient(Patient("George", "14:00"))
#     ll.add_patient(Patient("Mask", "11:00"))
    # print(ll.patients)
    # list_of_patients = [Patient("Max", "11:00"), Patient(
    #     "Alex", "13:15"), Patient("Lyle", "14:00")]
    # for i, el in enumerate(ll):
    #     print(i, el)
    #     assert el == list_of_patients[i]
