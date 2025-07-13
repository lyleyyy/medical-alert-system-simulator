
from hospital_base import HospitalBase
from patient import Patient


class Hospital_1 (HospitalBase):

    def __init__(self):
        super().__init__()
        # The number 27 is the max numebr of appointments from 08:00 to 18:00 excluding 12:00 - 13:00
        self.patients = ["Available" for i in range(27)]

    def __iter__(self):
        """
            Add your code here!
        """
        for i in self.patients:
            if isinstance(i, Patient):
                yield i

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """
        hrs = int(patient.time.split(":")[0])
        mins = int(patient.time.split(":")[1])
        index = int((hrs - 8)*3 + mins/20)
        if self.patients[index] == "Available":
            self.patients[index] = patient
            return True
        else:
            return False

    # ==============================  Add any extra functions below   ==============================


# if __name__ == "__main__":
#     """
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             The following main function is provided for simple debugging only
#         """
#     hospital = Hospital_1()
#     # print(hospital.patients)
#     hospital.add_patient(Patient("Max", "11:00"))
#     hospital.add_patient(Patient("Alex", "13:20"))
#     hospital.add_patient(Patient("George", "14:00"))
#     print(hospital.patients)
#     list_of_patients = [Patient("Max", "11:00"), Patient(
#         "Alex", "13:20"), Patient("George", "14:00")]
#     for i, el in enumerate(hospital):
#         assert el == list_of_patients[i]
