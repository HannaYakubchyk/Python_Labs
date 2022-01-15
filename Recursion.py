
def square_out_of_rectangle(a, b, n):

    if a == b:
        print("Отрезание прямоугольника на квадрат невозможно, так как прямоугольник уже квадрат с длиной ребра: " + str(a) +" на " +str(b))
        print("Получилось "+str(n+1)+" квадратa(-ов)")
        return
    elif a < b:
        print("Из прямоугольника можно отрезать квадрат с длиной ребра: "+ str(a) +" на " +str(a))
        print("После чего остается прямоугольник со сторонами " +str(b-a) + " на " +str(a))
        print()

        square_out_of_rectangle(a, b-a, n+1)

    elif a > b:
        print("Из прямоугольника можно отрезать квадрат с длиной ребра: " + str(b) +" на " +str(b))
        print("После чего остается прямоугольник со сторонами " + str(a-b) + " на "+str(b))
        print()
        square_out_of_rectangle(a-b, b, n+1)


a = int(input("Введите сторону а прямоугольника: "))
b = int(input("Введите сторону b прямоугольника: "))
print()
square_out_of_rectangle(a, b, n=0)
