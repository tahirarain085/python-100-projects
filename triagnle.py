
def area_of_triangle(height,base):
    area = height * base * (0.5)
    return area


height = float(input("Etner Height:\t "))
base = float(input("Enter base here:\t"))

area = area_of_triangle(height,base)
print(area)