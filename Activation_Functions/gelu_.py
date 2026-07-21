
"""
Formula with sigmoid approximation, where the complex Commulative distributive function for 
Normal distribution has been simplifies to:

gelu = x.sigmoid(1.702x) --> x/(1+e^(-1.702x))

"""

def get_sigmoid(x):
    
    return (1/(1+(2.7183)**-x))


def get_gelu(x):
    return (x*(get_sigmoid(1.702*x)))



while True: 
    x = input("Enter any real Number (q to quit): ")
    if x == 'q':
        break
    # print(float(x))
    print(f"{get_gelu(float(x)):.4f}")






