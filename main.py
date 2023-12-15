from jinja2 import Environment, FileSystemLoader
import random

f_template = open('task1.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('task1.html')

n = 5
m = 2


def create_matrix(num_rows, num_columns):
    matrix_ = []
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            row.append(random.randint(-9, 9))
        matrix_.append(row)
    return matrix_


matrix = create_matrix(n, m)
print(matrix)

result_html = template.render(matrix=matrix, n=n, m=m)

f = open('exit.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()

