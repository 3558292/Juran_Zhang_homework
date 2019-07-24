import os
class Employee:
    def __init__(self, first_name="", last_name="", e_id="00000", e_duration=0, salary_per_day=0):
        self.first_name = first_name
        self.last_name = last_name
        self.e_id = e_id
        self.e_duration = e_duration
        self.salary_per_day = salary_per_day
        self.last_name_lst=[]

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

    lst=[]
    def bi_serch(key:str,low,high):
        mid=(high+low)//2
        key=key[0]

        while high >= low:
            print(mid)
            if ord(Employee.lst[mid].last_name[0]) < ord(key):
                Employee.bi_serch(key,mid+1,high)
            elif ord(Employee.lst[mid].last_name[0]) > ord(key):
                Employee.bi_serch(key,low,mid-1)
            else:
                print(Employee.lst[mid])
        return -1  # not found


if __name__ == '__main__':
    in_f = open(os.path.join(str(os.getcwd()), "input"), 'r')
    out_f = open(os.path.join(str(os.getcwd()), "output"), 'w')

    for i in in_f:
        i.strip("\n")
        l = i.split(",")
        emp = Employee(l[0], l[1], l[2], int(l[3]), int(l[4].strip('$')))
        Employee.lst.append(emp)
        out_f.write(emp.employee_info)

    out_f.flush()
    in_f.close()
    out_f.close()

Employee.bi_serch(input("name"),0,len(Employee.lst))

