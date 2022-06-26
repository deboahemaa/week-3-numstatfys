import matplotlib.pyplot as plt
import numpy as np
import random

def lattice(L):
    matrix = np.random.random((L, L))
    x_max = L
    y_max = L 
    spin = np.zeros((L,L))

    for x in np.arange(x_max):
        for y in np.arange(y_max):
            if matrix[x,y] < 0.5:
                spin[x,y] = 0.5
            else:
                spin[x,y] = -0.5
    return spin

def hamiltonian(L):
    spin = lattice(L)
    x_max = L
    y_max = L
    H = 0
    J = 1
    for x in np.arange(x_max):
        for y in np.arange(y_max):
            H += -J * 0.5 * (spin[(x+1)%L, y%L] + spin[(x-1)%L, y%L] + spin[x%L, (y+1)%L] + spin[x % L , y-1 % L]) 
    
    return H, spin 

# function to calculate difference in energy between a random spin state and its augmented version where one spin is turned around
def delta_E(L):
    H = hamiltonian(L) #
    Energy = H[0]
    c = H[1]

    x_rand = random.randrange(L)
    y_rand = random.randrange(L)
    c_1 = np.copy(c)
    c_1[x_rand, y_rand] = c[x_rand, y_rand] * -1

    x_max = L
    y_max = L
    J = 1
    H = 0

    for x in np.arange(x_max):
        for y in np.arange(y_max):
            H += -J * 0.5 * (c_1[(x+1)%L, y%L] + c_1[(x-1)%L, y%L] + c_1[x%L, (y+1)%L] + c_1[x % L , y-1 % L]) 

    delta_energy = np.abs(Energy - H)

    return delta_energy, c, c_1

# this is the easier way to compute dE between c and c'
def dE_easy():
    return 2

def magnetization(L):
    dE = delta_E(L)
    dH = dE[0]
    c = dE[1]
    c_1 = dE[2]
    x_max = L
    y_max = L
    M = 0

    for x in np.arange(x_max):
        for y in np.arange(y_max):
            M += c_1[x,y]
        
    
    print("The difference in energy between the two spin states is:", dH)
    print("The magnetisation is:", M)
    #print("Original spin onfiguration")
    #print(c)
    #print("Augmented spin configuration")
    #print(c_1)
    
    plt.subplot(1, 2, 1) # row 1, col 2 index 1
    plt.imshow(c)
    plt.title("Original spin configuration")
    plt.colorbar()
    #plt.xlabel('X-axis ')
    #plt.ylabel('Y-axis ')

    plt.subplot(1, 2, 2) # index 2
    plt.imshow(c_1)
    plt.title("Augmented spin configuration")
    plt.colorbar()
    #plt.xlabel('X-axis ')
    #plt.ylabel('Y-axis ')
    plt.show()
    return

magnetization(9)