import os
class Employee:
    def __init__(self, first_name="", last_name="", e_id="00000", e_duration=0, salary_per_day=0):
        self.first_name = first_name
        self.last_name = last_name
        self.e_id = e_id
        self.e_duration = e_duration
        self.salary_per_day = salary_per_day

    def __str__(self):
        return self.employee_info

    @property
    def received_payment(self):
        return self.e_duration * self.salary_per_day

    @property
    def employee_info(self):
        return f"{'-' * 45}\
                    \n| EMPLOYEE INFO:{' ':<26}||\
                    \n| First Name: {self.first_name:<28}||\
                    \n| Last Name: {self.last_name:<29}|| \
                    \n| ID: {self.e_id:<36}||\
                    \n| Received Payment: ${self.received_payment:<21.2f}||\
                    \n"


if __name__ == '__main__':
    in_f = open(os.path.join(str(os.getcwd()), "input"), 'r')
    out_f = open(os.path.join(str(os.getcwd()), "output"), 'w')

    for i in in_f:
        i.strip("\n")
        l = i.split(",")
        emp = Employee(l[0], l[1], l[2], int(l[3]), int(l[4].strip('$')))
        out_f.write(emp.employee_info)

    out_f.flush()
    in_f.close()
    out_f.close()

