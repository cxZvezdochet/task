"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""
while True:
    student_name = input("Введите имя студента (или 'стоп' для завершения): ")
    if student_name.lower() == 'стоп':
        break

    num_subjects = int(input("Введите количество предметов: "))
    total_score = 0
    for i in range(num_subjects):
        subject_score = int(input(f"Введите баллы по предмету {i + 1} (от 0 до 50): "))
        total_score += subject_score
    print(f"Итоговый счет для {student_name}: {total_score}")
    
    if total_score > 80:
        print("Наградить дипломом.")
    elif 50 < total_score <= 80:
        print("Наградить похвальной грамотой.")
    else:
        print("Выдать грамоту об участии.")