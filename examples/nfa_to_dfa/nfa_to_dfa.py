from fa import Transition, DFA


sigma = {'a', 'b'}
q = []
for i in range(1, 14):
    q.append(str(i))
delta = [
    Transition('1', 'a', '2'),
    Transition('1', 'b', '2'),
    Transition('2', 'a', '2'),
    Transition('2', 'b', '2'),
    Transition('2', 'a', '3'),
    Transition('3', 'a', '4'),
    Transition('3', 'b', '5'),
    Transition('4', 'a', '13'),
    Transition('4', 'b', '13'),
    Transition('5', 'a', '6'),
    Transition('6', 'b', '7'),
    Transition('7', 'a', '13'),
    Transition('7', 'b', '13'),
    Transition('2', 'b', '8'),
    Transition('8', 'b', '9'),
    Transition('9', 'a', '13'),
    Transition('9', 'b', '13'),
    Transition('8', 'a', '10'),
    Transition('10', 'b', '11'),
    Transition('11', 'a', '12'),
    Transition('12', 'a', '12'),
    Transition('12', 'b', '12'),
    Transition('12', 'a', '13'),
    Transition('12', 'b', '13'),
    Transition('13', 'a', '13'),
    Transition('13', 'b', '13'),
]
q0 = '1'
f = ['13']
w = DFA('Test4', sigma, q, delta, q0, f)

result_format = 'svg'
filename='images/nfa.gv'
w.view(result_format=result_format, show_nodes=False, save=True, filename=filename)
markdown = '# НКА в ДКА\n'
markdown += '## Исходный автомат\n'
markdown += '![Исходный автомат](' + filename + '.' + result_format + ')\n'
dfa, history = w.thompson()

for k, v in enumerate(history):
    filename = 'images/history' + str(k + 1) + '.gv'
    v.view(result_format=result_format, show_nodes=False, save=True, filename=filename)
    markdown += '## Итерация ' + str(k + 1) + '\n'
    markdown += '![Итерация ' + str(k + 1) + '](' + filename + '.' + result_format + ')\n'

filename = 'images/dfa.gv'
dfa.view(result_format=result_format, save=True, filename=filename)
markdown += '## Результат\n'
markdown += '![Результат](' + filename + '.' + result_format + ')\n'
with open("result.md", "w") as file:
    file.write(markdown)
