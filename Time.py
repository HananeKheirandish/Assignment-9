class Time:
    def __init__(self , h , m , s):
        self.h = h
        self.m = m
        self.s = s

    def sum_time(self , guest):
        result = Time(None , None , None)
        result.h = self.h + guest.h
        result.m = self.m + guest.m
        result.s = self.s + guest.s
        return result

    def sub_time(self , guest):
        result = Time(None , None , None)
        result.h = self.h - guest.h
        result.m = self.m - guest.m
        result.s = self.s - guest.s
        return result

    def second_to_time(self):
        self.h = second / 3600
        self.m = (second % 3600) / 60
        self.s = (second % 3600) % 60

    def time_to_second(self):
        second = self.h * 3600 + self.m *60 + self.s
        print('Second: ' , second)

    def show_time(self):
            if self.s >= 60:
                self.s -= 60
                self.m += 1
            if self.m >= 60:
                self.m -= 60
                self.h += 1
            if self.h >= 24:
                self.h -= 24
            if self.s < 0:
                self.m -= 1
                self.s += 60
            if self.m < 0:
                self.h -= 1
                self.m += 60
            if self.h < 0:
                self.h += 24
            if self.h >= 24:
                self.h -= 24
            print(str(int(self.h)).zfill(2),":",str(int(self.m)).zfill(2),":",str(int(self.s)).zfill(2))

time1 = input('Please enter time1-{hour:minute:second} : ')
time1 = time1.split(':')
time1 = Time(int(time1[0]) , int(time1[1]) , int(time1[2]))

time2 = input('Please enter time2-{hour:minute:second} : ')
time2 = time2.split(':')
time2 = Time(int(time2[0]) , int(time2[1]) , int(time2[2]))

while True:
    print('1- sum of times ')
    print('2- submite of times ')
    print('3- second to time ')
    print('4- time to second ')
    print('5- exit ')
    choice = int(input('Please enter your choose: '))
    if choice == 1:
        res = time1.sum_time(time2)
        res.show_time()
    elif choice == 2:
        res = time1.sub_time(time2)
        res.show_time()
    elif choice == 3:
        second = int(input("Please enter second: "))
        res = Time(None , None , second)
        res.second_to_time()
        res.show_time()
    elif choice == 4:
        time1.time_to_second()
        time2.time_to_second()
    elif choice == 5:
        exit()
    else:
        print('Wrong choice. Try again.')