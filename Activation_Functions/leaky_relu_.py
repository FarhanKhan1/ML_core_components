def get_l_relu(x, constant=0.01):

    return max(constant*x,x)


while True: 
    x = input("Enter any real Number (q to quit): ")
    if x == 'q':
        break
    # print(float(x))
    print(f"{get_l_relu(float(x)):.2f}")