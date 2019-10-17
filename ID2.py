import datetime,time

class ID:
    def __init__(self,id_numder):
        self.id_numder = id_numder
        self.area = id_numder[:6]
        self.birthday = id_numder[6:14]
        self.sex = id_numder[14:17]
        self.sss  = int(id_numder[17:])
        print(self.area,'地区')
        print(self.birthday,'生日')
        print(self.sex,'性别')
        print(self.sss,'编号')
        print(type(self.sex))
        print('_____________________')
        self.lists = []
        self.lists.append(self.DT())
        self.lists.append(self.SEX())
        self.lists.append(self.odatetime.strftime("%Y-%m-%d"))
        self.lists.append(self.address())
        print(self.lists)

    def DT(self):
        year = self.birthday[:4]
        month = self.birthday[4:6]
        day = self.birthday[6:]

        self.odatetime = datetime.datetime(int(year), int(month), int(day))
        odate = datetime.datetime(1970,1,2)
        oda = time.mktime(odate.timetuple())
        ti = time.time()
        odat = time.mktime(self.odatetime.timetuple())

        if oda < odat < ti and len(self.id_numder) == 18:
            print('OK')
            print(self.odatetime.strftime("%Y-%m-%d"))
            return '有效'
        else:
            print('无效')
            return '无效'

        print(oda,odat)
    def SEX(self):
        if int(self.sex) % 2 == 0:
            return '女'
        else:
            return '男'
    def address(self):
        # f = open(file='身份证归属地.txt',mode='r',encoding='utf-8')
        # all = f.readlines()
        # res = ''
        # for item in all:
        #     print(item)
        #     if self.area == item[:6]:
        #         res = self.area
        #
        #         return res[6:-1]
        f = open(file="身份证归属地.txt", mode='r', encoding="utf-8")
        all_area = f.readlines()
        res_area = ''
        for item in all_area:
            if self.area == item[:6]:
                res_area = item[6:-1]
        if res_area == '':
            return False

        else:
            return res_area

        def get_check_number(self):
            number = self.id_number[0:17]

        # 系数
            si_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            check_number = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
            # 验证
            of_number = 0
            for index in range(len(number)):
                of_number += int(number[index]) * int(si_list[index])

                yu_number = of_number % 11
                return check_number[yu_number]

            # 校验码验证ss
            def validate_check_number(self):
                if self.get_check_number() == self.sss:
                    return '有效'

                else:
                    return False

    # def address(self):
    #     if self.area == '130637':
    #         return '河北保定'
    #     else:
    #         return '咱不知道'
    #     # def id_time(self):
    #
    #     year = self.birthday[:4]
    #     month = self.birthday[4:6]
    #     day = self.birthday[6:]
    #     odatetime = datetime.datetime(int(year),int(month),int(day))
    #     return odatetime.strftime('%Y-%m-%d')
    #
    # def id_is(self):
    #     odate = datetime.datetime(1970, 1, 2)
    #     otime = time.time()
    #     year = self.birthday[:4]
    #     month = self.birthday[4:6]
    #     day = self.birthday[6:]
    #     odatetime = datetime.datetime(int(year), int(month), int(day))
    #     od = time.mktime(odate.timetuple())
    #     odt = time.mktime(odatetime.timetuple())
    #     if od < odt < otime:
    #
    #         return '有效'
    #
    #     else:
    #         return '无效'
    # def Sex(self):
    #     if self.sex % 2 == 1:
    #         return '男'
    #     else:
    #         return '女'
    #
    # def zuihou(self):
    #     checkidc = ID("130637211101080316")
    #     aaa = checkidc.address()
    #     aab =  checkidc.id_time()
    #     aac = checkidc.id_is()
    #     aad = checkidc.Sex()
    #     a = [aac,aad,aab,aaa]
# id = Id()
# id.yunxing()

# 130637200001080315