team1_name = 'Мастера кода'
team2_name = 'Волшебники Данных'

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print("В команде '%s' участников: %s!" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

print("Команда Волшебники данных решила задач: {}!".format(score2))
print("'{}' решили задачи за: {} с!".format(team2_name, team1_time))

print(f'Команды решили {score1} и {score2} задач.')
challenge_result = 'Мастера кода'
print(f'Результат битвы: победа команды {challenge_result}!')
tasks_total = score1 + score2
time_avg = team2_time + team1_time
print(time_avg)
print(f'Сегодня было решено {score1 + score2} задач, в среднем по {time_avg / tasks_total:.2f} секунды на задачу!.')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    print('Победа команды Мастера кода!')
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    print(f'Победа команды Волшебники Данных!')
else:
    print('Ничья')
