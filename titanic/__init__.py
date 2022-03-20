from titanic.templates import TitanicTemplate

if __name__ == '__main__':
    while 1:
        menu = (input('1. Temp 2. process'))
        if menu == '1':
            template = TitanicTemplate(fname='train.csv')
            # template.visualize()
            break
