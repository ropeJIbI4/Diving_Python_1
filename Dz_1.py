# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны  предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print('Треугольник существует')
        if a == b == c:
            print('Треугольник равносторонний')
        elif a == b or b == c or c == a:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
    else:
        print('Такого треугольника не существует')

print (check_triangle(1, 2 , 3))
print (check_triangle(3, 2 , 3))
print (check_triangle(3, 3 , 3))