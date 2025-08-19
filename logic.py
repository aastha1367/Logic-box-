def right():
 for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

def pyramid():
 for i in range(1,6):
        print(" " * (6-i), end=" ")
        print("* " * i)

def left():
 for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

def number(a, b):
   total=0
   for num in range(a, b+1):
      if num % 2 == 0:
         print(f"Number{num} is even")   
      else:
         print(f"Number{num} is odd")   
      total += num
   print(f"Sum of all numbers from {a} to {b} is: {total}")

def main():
    while True:
        print("\nWelcome to the Pattern Generator and Number Analyzer!")
        print("Select an option:")
        print("1. Right-angled Triangle")
        print("2. Pyramid")
        print("3. Left-angled Triangle")
        print("4. Analyze a Range of Numbers")
        print("5. Exit")
    
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            right()
        elif choice == "2":
            pyramid()
        elif choice == "3":
            left()
        elif choice == "4":
            a = int(input("Enter start of range: "))
            b = int(input("Enter end of range: "))
            number(a, b)
        elif choice == "5":
            print("Exit")
            break
    else:
        print("Invalid choice! Please try again.")

main()
