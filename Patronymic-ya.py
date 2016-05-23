# -*- coding: utf-8 -*-
class Patronymer(object):
    def get_patro(self, name, feminine=False):
        # Словарь. У гласных значение 1. У согласных 2. У 'Ь' 3. У 'Й' 4.
        dict = {'а': 1, 'б': 2, 'в': 2, 'г': 2, 'д': 2, 'е': 1, 'ё': 1, 'ж': 2, 'з': 2, 'и': 1, 'й': 4, 'к': 2, 'л': 2,
                'м': 2, 'н': 2, 'о': 1, 'п': 2, 'р': 2, 'с': 2, 'т': 2, 'у': 1, 'ф': 2, 'х': 2, 'ц': 2, 'ч': 2, 'ш': 2,
                'щ': 2, 'ъ': 5, 'ы': 1, 'ь': 3, 'э': 1, 'ю': 1, 'я': 1}
        res = ''
        # подготовка имени и проверка корректности
        name = name.lower().strip().replace('ё', 'е')
        if not name.isalpha():
            print('Некорректное имя: ' + name + '. Убедитесь что в имени нет цифр и специальных символов.')
            exit()
        for x in name:
            if dict.get(x) is None:
                print('Убедитесь что в имени ' + name + ' нет латинских букв.')
                exit()

        # имя окнчивается на согласную
        if dict[name[-1]] == 2:
            if feminine:
                res = name + 'овна'
            else:
                res = name + 'ович'

        # имя оканчивается на Ь
        elif dict[name[-1]] == 3:
            if feminine:
                res = name[0:-1] + 'евна'
            else:
                res = name[0:-1] + 'евич'

        # имя оканчивается на ИЙ
        elif name[-2:] == 'ий':
            if name[-4:-2] == 'нт' or dict[name[-3]] == 2 and dict[name[-4]] != 2:
                if feminine:
                    res = name[0:-2] + 'ьевна'
                else:
                    res = name[0:-2] + 'ьевич'
            if name[-4:-2] != 'нт' and dict[name[-3]] == 2 and dict[name[-4]] == 2:
                if feminine:
                    res = name[0:-1] + 'евна'
                else:
                    res = name[0:-1] + 'евич'

        # имя оканчивается на 'гласную + Й'
        elif dict[name[-1]] == 4 and name[-2] != 'и' and dict[name[-2]] == 1:
            if feminine:
                res = name[0:-1] + 'евна'
            else:
                res = name[0:-1] + 'евич'

        # имя оканчивается на гласную
        elif dict[name[-1]] == 1:
            if feminine:
                print('В имени ' + name + ' ударение падает на последний слог? [y/n]')
                ans = input()
                while ans != 'y' and ans != 'n':
                    print('Некорректный ответ! Попробуйте ещё раз:')
                    ans = input()
                if ans == 'y':
                    res = name[0:-1] + 'инична'
                else:
                    res = name[0:-1] + 'ична'
            else:
                res = name[0:-1] + 'ич'
        else:
            print('Не удалось составить отчество по имени: ' + name)
            exit()
        res = res.capitalize()
        return res


if __name__ == "__main__":
    p = Patronymer()
    assert p.get_patro("Иван") == "Иванович"
    assert p.get_patro("Андрей") == "Андреевич"
    assert p.get_patro("Дмитрий") == "Дмитриевич"
    assert p.get_patro("Фома") == "Фомич"
    assert p.get_patro("Егор") == "Егорович"
    assert p.get_patro("Фаддей") == "Фаддеевич"
    assert p.get_patro("Эмиль") == "Эмилевич"
    assert p.get_patro("Ярослав") == "Ярославович"
    assert p.get_patro("Илья") == "Ильич"
    assert p.get_patro("Валерий") == "Валерьевич"
    assert p.get_patro("Юрий") == "Юрьевич"
    assert p.get_patro("Пётр") == "Петрович"
    assert p.get_patro("Савва") == "Саввич"

    assert p.get_patro("Иван", True) == "Ивановна"
    assert p.get_patro("Дмитрий", True) == "Дмитриевна"
    assert p.get_patro("Фома", True) == "Фоминична"
    assert p.get_patro("Егор", True) == "Егоровна"
    assert p.get_patro("Фаддей", True) == "Фаддеевна"
    assert p.get_patro("Эмиль", True) == "Эмилевна"
    assert p.get_patro("Ярослав", True) == "Ярославовна"
    assert p.get_patro("Валерий", True) == "Валерьевна"
    assert p.get_patro("Юрий", True) == "Юрьевна"
    assert p.get_patro("Андрей", True) == "Андреевна"
    assert p.get_patro("Пётр", True) == "Петровна"
    assert p.get_patro("Илья", True) == "Ильинична"
    assert p.get_patro("Савва", True) == "Саввична"
