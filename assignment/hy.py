filename=" file.txt"
foods=[]

print("enter your 5 favourite food")
for t in range(5):
    food = input(f"food {t+1}:")
    foods.append(food)

with open(filename, "w", encoding="utf-8") as f:
        for food in foods:
              f.write(food +"\n") 

print(f"\nall food are now in {filename}")


print(f"\nreading from file.txt")

with open(filename, "r", encoding="utf-8")as f:
         for t, line in enumerate (f,1):
                f.read(f"{t}.{line.strip()}")

          

         print("\nDone")     