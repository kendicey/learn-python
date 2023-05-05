def d():
    animal = "elephant"
    def e():
        nonlocal animal     # use nonlocal keyword to access "elephant"
        animal = "giraffe"
        print("Inside nested function: " + animal)  # use local animal here (giraffe)

    print("Before calling function: " + animal)     # Before calling function: elephant
    e()                                             # Inside nested function: giraffe
    print("After nested function: " + animal)       # After nested function: giraffe

animal = "camel"
d()
print("Global animal: " + animal)   # Global animal: camel