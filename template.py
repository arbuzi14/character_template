import random
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os


def main():
    count_card = int(input("сколько карточек создать? "))
    for number in range(count_card):
        name=input('введите имя: ')
        env = Environment(
            loader=FileSystemLoader('.'),
            autoescape=select_autoescape(['html'])
        )
        template = env.get_template('template.html')
        races = ['человек', 'пеленг', 'молок', 'фаянин', 'галец']
        character_race = int(input("выберите рассу 1 человек 2 пеленг 3 молк 4 фаянин 5 галец: "))
        classes = ['лучник', 'убийца', 'бард', 'воин', 'маг']
        character_class = int(input("выберите класс 1 лучник 2 убийца 3 бард 4 воин 5 маг"))
        character_class = classes[character_class-1]
        clases_base = {
            'бард': {
                'skills':  ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
                'strength': random.randint(1, 3),
                'agility': random.randint(1, 3),
                'intelligence': random.randint(1, 3),
                'luck': random.randint(1, 3),
                'temper': 15,
                'image': '../images/bard.webp'
            },
            'лучник': {
                'skills': ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                'strength': random.randint(1, 3),
                'agility': 15,
                'intelligence': random.randint(1, 3),
                'luck': random.randint(1, 3),
                'temper': random.randint(1, 3),
                'image': '../images/archer.png'
            },
            'убийца': {
                'skills': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                'strength': random.randint(1, 3),
                'agility': random.randint(1, 3),
                'intelligence': random.randint(1, 3),
                'luck': 15,
                'temper': random.randint(1, 3),
                'image': '../images/assasin.png'
            },
            'воин': {
                'skills': ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                'strength': 15,
                'agility': random.randint(1, 3),
                'intelligence': random.randint(1, 3),
                'luck': ran1dom.randint(1, 3),
                'temper': random.randint(1, 3),
                'image': '../images/warrior.png'
            },
            'маг': {
                'skills': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                'strength': random.randint(1, 3),
                'agility': random.randint(1, 3),
                'intelligence': 15,
                'luck': random.randint(1, 3),
                'temper': random.randint(1, 3),
                'image': '../images/wizard.png'
            },
        }

        skills = random.sample(clases_base[character_class]['skills'],3)
        rendered_page = template.render(
            name=name,
            race=races[character_race-1],
            character_class=character_class,
            strength=clases_base[character_class]['strength'],
            agility=clases_base[character_class]['agility'],
            intelligence=clases_base[character_class]['intelligence'],
            luck=clases_base[character_class]['luck'],
            temper=clases_base[character_class]['temper'],
            image=clases_base[character_class]['image'],
            first_skill=skills[0],
            second_skill=skills[1],
            third_skill=skills[2],
        )

        os.makedirs("characters", exist_ok=True)
        with open(f'characters/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()
