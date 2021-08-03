#genera promedio de un estudiante de un diccionario dato

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks:
        if i == query_name:
            suma = sum(student_marks[query_name])
            promedio = suma/len(student_marks[query_name])
            print(round(promedio,2))
