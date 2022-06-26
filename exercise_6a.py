import numpy as np
import matplotlib.pyplot as plt
import random

## Question 1
# No you dont, you can just set it to 1 since that is the exact solution.

## Question 2
def p(x):
    if x<0 or x>1:
        return 0
    else:
        return np.exp(-x)


def A_p(x0, N_t, N_MC):

    mean_list = []
    std_list = []
    y_list = []
    x_list = []
    np.random.seed(0)

    N = N_t + N_MC
    x = x0
    x_1 = 0
    A = 0  

    for i in np.arange(N):                
        x_1 = x + random.choice([-0.2, 0.2])
        P = p(x_1) / p(x)
        
        if P > 1:
            x = x_1
        
        elif P < 1 and P != 0:
            r = np.random.rand()
        
            if r < P:
                x = x_1
        
            else:
                x = x 
        
        if i >= N_t:
            A += x * p(x)
            y_list.append(x)  
    
    mean_list.append(np.mean(y_list))
    std_list.append(np.std(y_list)/np.sqrt(N_MC-1))
    print(np.mean(y_list), np.std(y_list))
    plt.hist(y_list)
    plt.show()
    return

A_p(0.5, 10000, 2**18)

