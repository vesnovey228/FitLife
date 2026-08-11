print('Здравствуйте! Пожалуйста, укажите ваше имя и возвраст.')
user_name = input('Ваше имя: ')
while True:
    try:
        user_age = int(input('Ваш возвраст: '))
        if user_age < 0:
            print('Ваш возвраст не может быть меньше нуля. Попробуйте снова.')
            continue
        break
    except ValueError:
        print('Ошибка. Пожалуйста, введите число.')
    except KeyboardInterrupt:
        print('Программа завершина пользователем.')
        break
print('Пожалуйста, укажите ваш вес и рост.')
while True:
    try:
        user_weight = float(input('Ваш вес в кг (например, 63.3): '))
        if user_weight < 0:
            print('Ваш вес не может быть отрицательным. Попробуйте снова.')
            continue
        break
    except ValueError:
        print('Ошибка. Пожалуйста, введите число.')
    except KeyboardInterrupt:
        print('Программа завершина пользователем.')
        break
while True:
    try:
        user_height = float(input('Ваш рост в м (например, 1.73): '))
        if user_height < 0:
            print('Ваш рост не может быть отрицательным. Попробуйте снова.')
            continue
        break
    except ValueError:
        print('Ошибка. Пожалуйста, введите число.')
    except KeyboardInterrupt:
        print('Программа завершина пользователем.')
        break
bmi = round(user_weight / (user_height ** 2), 1)  # расчёт индекса массы тела
water_per_kg = 30
water_l_per_kg = water_per_kg / 1000
water_l = (user_weight * water_l_per_kg)  # расчёт рекомендуемой нормы воды
print(f'\nВаш отчёт, {user_name} ({user_age} г.):')
print(f'Индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.2f} л. в день\n')
print('Расчёт окончен. Будьте здоровы!')
