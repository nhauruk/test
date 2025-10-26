import math

def cosine_distance(vec1, vec2):
    if not isinstance(vec1, list) or not isinstance(vec2, list):
        print("Ожидаются списки")
        return

    if len(vec1) == 0 or len(vec2) == 0:
        print("Пустой вектор")
        return

    if len(vec1) != len(vec2):
        print("Разная длина")
        return

    dot_product = 0
    for a, b in zip(vec1, vec2):
        dot_product += a * b

    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    
    if norm1 == 0 or norm2 ==0:
      print("Нулевой вектор")
      return

    cosine_distance = 1 - (dot_product / (norm1 * norm2))

    print(cosine_distance)
    
