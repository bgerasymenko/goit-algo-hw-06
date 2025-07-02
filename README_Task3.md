# Завдання 3: Алгоритм Дейкстри

## Найкоротші відстані між усіма вершинами

### Від джерела Central
- до Central: 0
- до Parkside: 5
- до Museum: 7
- до Riverside: 8
- до University: 13
- до Airport: 20
- до Harbor: 16

### Від джерела Parkside
- до Central: 5
- до Parkside: 0
- до Museum: 12
- до Riverside: 3
- до University: 18
- до Airport: 15
- до Harbor: 11

### Від джерела Museum
- до Central: 7
- до Parkside: 12
- до Museum: 0
- до Riverside: 15
- до University: 6
- до Airport: 16
- до Harbor: 20

### Від джерела Riverside
- до Central: 8
- до Parkside: 3
- до Museum: 15
- до Riverside: 0
- до University: 21
- до Airport: 12
- до Harbor: 8

### Від джерела University
- до Central: 13
- до Parkside: 18
- до Museum: 6
- до Riverside: 21
- до University: 0
- до Airport: 10
- до Harbor: 14

### Від джерела Airport
- до Central: 20
- до Parkside: 15
- до Museum: 16
- до Riverside: 12
- до University: 10
- до Airport: 0
- до Harbor: 4

### Від джерела Harbor
- до Central: 16
- до Parkside: 11
- до Museum: 20
- до Riverside: 8
- до University: 14
- до Airport: 4
- до Harbor: 0

## Висновок
Реалізовано алгоритм Дейкстри для зваженого графа; отримано довжини найкоротших шляхів.