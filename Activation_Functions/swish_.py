"""
Swish(x)=x.sigmoid(beta*x) = x/(1+e**-(beta*x))
"""


def get_sigmoid(x):
    
    return (1/(1+(2.7183)**-x))


def get_swish(x, beta=1):
    return x*get_sigmoid(beta*x)


if __name__ == '__main__':

    for each_value in [-3,-1,0,1,3]:
        print(f"{get_swish(float(each_value)):.4f}")


