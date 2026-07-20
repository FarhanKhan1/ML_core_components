def get_tanh(x):

    return (((2.718)**x - (2.718)**-x)/((2.718)**x + (2.718)**-x))


while True: 
    x = input("Enter any real Number (q to quit): ")
    if x == 'q':
        break
    # print(float(x))
    print(f"{get_tanh(float(x)):.2f}")