
number = iter([1, 2, 3])  # a sample iterator to demonstrate StopIteration

while True:
    x = input("Enter something (or 'q' to quit): ")

    if x.lower() == 'q':
            print("Exiting loop.")
            break

    try:
        value = next(number)
        print(f"Next number from iterator: {value}")

            # Try evaluating the user's input (may raise NameError/SyntaxError)
        result = eval(x)
        print(f"Result of your expression: {result}")

    except StopIteration:
        print("Iteration error: No more items in the iterator!")
        number = iter([1, 2, 3])  

    except NameError as e:
        print(f"Symbol error: Undefined name used -> {e}")

    except SyntaxError as e:
        print(f"Symbol error: Invalid syntax -> {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

