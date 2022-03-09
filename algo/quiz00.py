from algo.domain import my100, memberlist, myRandom


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        pass

    def quiz01bmi(self): pass

    def quiz02dice(self): pass

    def quiz03rps(self): pass

    def quiz04leap(self): pass

    def quiz05grade(self): pass

    def quiz06memberChoice(self):
        return memberlist()[myRandom(0, 23)]

    def quiz07lotto(self): pass

    def quiz08bank(self):
        Account.main()


class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = Quiz00().quiz06memberChoice() if name == None else name
        self.account_number = self.create_account_number() if account_number == None else account_number
        self.money = myRandom(100, 1000) if money == None else money

    def to_string(self):
        return f'은행 : {self.BANK_NAME},' \
               f'입금자 : {self.name},' \
               f'계좌번호 : {self.account_number},' \
               f'금액 : {self.money} 만원'

    def create_account_number(self):
        """
        ls = [myRandom(0, 10) for i in range(3)]
        ls.append('-')
        ls += [myRandom(0, 10) for i in range(2)]
        ls.append('-')
        ls += [myRandom(0, 10) for i in range(6)]
        return "".join(ls)
        """
        return ''.join('-' if i == 3 or i == 6 else str(myRandom(1, 10)) for i in range(13))

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def find_account(ls, account_number):
        return ''.join([j.to_string() if j.account_number == account_number
                        else '찾는 계좌가 아닙니다.' for (i, j) in enumerate(ls)])

    @staticmethod
    def add_account(ls, account_number, add):
        '''for i, j in enumerate(ls):
            if j.account_number == account_number:
                ls[i].money += int(add)
                return ls[i].to_string()'''
        # [i, j if i == 0 or i == 0 else i for i, j in ls]

    @staticmethod
    def withdraw_account(ls, account_number, withdraw):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                ls[i].money -= int(withdraw)
                return ls[i].to_string()

    @staticmethod
    def deposit(ls, account_number, money):
        for i, j in enumerate(ls):
            print (j.account_number, j.money)

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0. 종료 1. 계좌 개설 2. 계좌 목록 3. 입금 4. 출금 5. 계좌 해지 6. 계좌 조회')
            if menu == '0': break
            if menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()} .. 개설')
                ls.append(acc)
            elif menu == '2':
                li = '\n'.join(i.to_string() for i in ls)
                print(li)
            elif menu == '3':
                print(Account.add_account(ls, input('입금할 계좌번호'), input('입금액')))
            elif menu == '4':
                print(Account.withdraw_account(ls, input('출금할 계좌번호'), input('출금액')))
            elif menu == '5':
                Account.del_account(ls, input('탈퇴할 계좌번호'))
            elif menu == '6':
                print(Account.find_account(ls, input('조회할 계좌 입력')))
            elif menu == '7':
                print(Account.deposit(ls, input('계좌번호'), int(input('입금액'))))
            else:
                print('Wrong Number.. Try Again')
                continue
