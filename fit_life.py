print('Здравствуйте! Пожалуйста, укажите ваше имя и возвраст.')
user_name = input('Ваше имя: ')
user_age = int(input('Ваш возвраст: '))
print('Пожалуйста, укажите ваш вес и рост.')
user_weight = float(input('Ваш вес в кг (например, 63.3): '))  # ввод данных пользователем,
user_height = float(input('Ваш рост в м (например, 1.73): '))  # необходимых для расчёта
bmi = round(user_weight / (user_height ** 2), 1)  # расчёт индекса массы тела
water_l_per_kg = 30 / 1000
water_l = (user_weight * water_l_per_kg)  # расчёт рекомендуемой нормы воды
print('')
print(f'Ваш отчёт, {user_name} ({user_age} г.):')  # вывод результатов
print(f'Индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.2f} л. в день')
print('')
print('Расчёт окончен. Будьте здоровы!')
