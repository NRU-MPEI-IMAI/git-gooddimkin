from fa import Transition, DFA


sigma = {'a', 'b'}
q = ['1', '2', '3']
delta = [
    Transition('1', 'a', '2'),
    Transition('1', 'b', '1'),
    Transition('2', 'a', '3'),
    Transition('2', 'b', '2'),
    Transition('3', 'a', '3'),
    Transition('3', 'b', '3'),
]
q0 = '1'
f = ['3']
x = DFA('Test1', sigma, q, delta, q0, f)

sigma = {'a', 'b'}
q = ['4', '5', '6']
delta = [
    Transition('4', 'a', '4'),
    Transition('4', 'b', '5'),
    Transition('5', 'a', '5'),
    Transition('5', 'b', '6'),
    Transition('6', 'a', '6'),
    Transition('6', 'b', '6'),
]
q0 = '4'
f = ['6']
y = DFA('Test2', sigma, q, delta, q0, f)

markdown = '# Прямое произведение\n'

result_format = 'svg'
filename = 'images/1.gv'
x.view(result_format=result_format, show_nodes=False, save=True, filename=filename)
markdown += '## Первый автомат\n'
markdown += '![Исходный автомат](' + filename + '.' + result_format + ')\n'

filename = 'images/2.gv'
y.view(result_format=result_format, show_nodes=False, save=True, filename=filename)
markdown += '## Второй автомат\n'
markdown += '![Исходный автомат](' + filename + '.' + result_format + ')\n'

dfa1, history = x.intersection(y)
dfa2, _ = x.union(y)
dfa3, _ = x.difference(y)

for k, v in enumerate(history):
    filename = 'images/history' + str(k + 1) + '.gv'
    v.view(result_format=result_format, show_nodes=False, save=True, filename=filename)
    markdown += '## Итерация ' + str(k + 1) + '\n'
    markdown += '![Итерация ' + str(k + 1) + '](' + filename + '.' + result_format + ')\n'

filename = 'images/intersection.gv'
dfa1.view(result_format=result_format, save=True, filename=filename)
markdown += '## Пересечение\n'
markdown += '![Результат](' + filename + '.' + result_format + ')\n'

filename = 'images/union.gv'
dfa2.view(result_format=result_format, save=True, filename=filename)
markdown += '## Объединение\n'
markdown += '![Объединение](' + filename + '.' + result_format + ')\n'

filename = 'images/difference.gv'
dfa3.view(result_format=result_format, save=True, filename=filename)
markdown += '## Разность\n'
markdown += '![Разность](' + filename + '.' + result_format + ')\n'

with open("result.md", "w") as file:
    file.write(markdown)
