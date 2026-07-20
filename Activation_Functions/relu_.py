def get_relu(x):

    return max(0,x)


while True: 
    x = input("Enter any real Number (q to quit): ")
    if x == 'q':
        break
    # print(float(x))
    print(f"{get_relu(float(x)):.2f}")