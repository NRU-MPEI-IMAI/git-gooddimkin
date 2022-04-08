
# Теоретические модели вычислений
## Дмитрий Поздеев, А-05-19
## ДЗ №1: Регулярные языки и конечные автоматы

### Задание 1. Построить конечный автомат, распознающий язык

![1. L=\{w\in\{a,b,c\}^*\ |\ |w|_c=1\}](images/latex21.svg)

![](images/task21.gv.svg)

![2. L=\{w\in\{a,b\}^*\ |\ |w|_a \leq 2,|w|_b \geq 2\}](images/latex21.svg)

Автомат получен с помощью прямого произведения автоматов. Исходные автоматы представлены снизу.

![](images/task22.gv.svg)

![3. L = \{w \in \{a, b\}^?\ |\ |w|_a \neq |w|_b \$](images/latex23.svg) 

В языке необходимо запоминать количество букв, конечные автоматы такого не умеют.

![4. L=\{w\in\{a,b\}^*\ |\ ww=www\}](images/latex24.svg)

![](images/task24.gv.svg)

### Задание 2. Построить конечный автомат, используя прямое произведение 

![1. L_1=\{w\in\{a, b\}^*\ |\ |w|_a \geq 2 \land |w|_b \geq 2\}](images/latex31.svg)

![](images/task31.gv.svg)


![2. L_2 = \{w \in \{a, b\}^*\ |\ |w| \geq 3 \land |w|\ нечётное\}](images/latex32.svg)

![](images/task32.gv.svg)

![3. L_3 = \{w \in \{a, b\}^* |\ |w|_a чётно \land |w|_b\ кратно\ трём\}](images/latex33.svg)

![](images/task33.gv.svg)

![4. L_4 = \neg L_3](images/latex34.svg)

![](images/task34.gv.svg)

![5. L_5 = L_2 \setminus L_3](images/latex35.svg)

![](images/task35.gv.svg)

### Задание 3. Построить минимальный ДКА по регулярному выражению

![1. (ab+aba)^*a](images/latex41.svg)

![](images/task41.gv.svg)

![2. a(a(ab)^*b)^*(ab)^*](images/latex42.svg)

![](images/task42.gv.svg)

![3. (a+(a+b)(a+b)b)^*](images/latex43.svg)

![](images/task43.gv.svg)

![4. (b+c)((ab)^*c+(ba)^*)^*](images/latex44.svg)

![](images/task44.gv.svg)

![5. (a+b)^+(aa+bb+abab+baba)(a+b)^+](images/latex45.svg)

![](images/task45.gv.svg)

# Задание 4. Определить является ли язык регулярным или нет

![1. L = \{(aab)^nb(aba)^m\ |\ n \geq 0, m \geq 0\}](images/latex51.svg)

![](images/task51.gv.svg)

# Задание 5. Реализовать алгоритмы

В библиотеке fa были реализованы классы для взаимодействия с конечными автоматами. В папке examples находятся примеры построения ДКА по НКА, а также пересечения, объединения и разности языков.