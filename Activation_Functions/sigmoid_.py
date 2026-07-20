def get_sigmoid(x):
    return (1/(1+(2.718)**-x))



while True: 
    x = input("Enter any real Number (q to quit): ")
    if x == 'q':
        break
    # print(float(x))
    print(f"{get_sigmoid(float(x)):.2f}")