import os
os.makedirs('recipe book', exist_ok=True)
a = input("Enter the name of the dish:--")
file_path = os.path.join('recipe book', f'{a}.txt')
with open(file_path, 'a') as f:
    b = input("The ingredients needed to make the dish:--")
    c = input("Instructions to make the dish:--")
    f.write(f'{a}\n')
    f.write(f'Ingredients:--\n{b}\n')
    f.write(f'Instructions:--\n{c}\n')
print(f"Recipe for {a} saved successfully in the 'recipe book' directory!")


