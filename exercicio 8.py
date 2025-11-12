nota = int(input("Qual é a nota? "))

match nota:
    case 20:
        avaliação = "Excelente aluno, não foste explodido yaai"
    case 18:
        avaliação = "muito bom meu aluno"
    case _:
        avaliação = "nota inexistente, vais ser explodido"
        
print("*Sons de explosões explodidas 2 a sequela*")
print(f"de qualquer forma o resultado é: {avaliação}")