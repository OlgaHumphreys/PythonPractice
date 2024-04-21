'''
Створіть програму на Python, яка визначає, чи проходить кандидат в наступний тур співбесіди на основі кількості набраних 
ним балів у тесті.

Задачі:

Введіть кількість балів, які кандидат набрав у тесті, через функцію input та збережіть їх у змінній num як ціле число.
Використовуйте оператор контролю виконання if-else, щоб визначити, чи проходить кандидат до наступного туру. 
Якщо num більше або дорівнює 83, змінній is_next привласніть значення True. В іншому випадку привласніть їй значення False.
Очікуваний результат:

Програма повинна отримати кількість балів, набраних кандидатом, та вивести, чи проходить кандидат до наступного туру.

Підказки:

Використовуйте int() для перетворення рядкового введення в ціле число.
Умовний оператор if-else допомагає визначити, яку дію потрібно виконати, залежно від виконання умови.
'''


is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
    is_next = True
else: 
    is_next = False


print(is_next)