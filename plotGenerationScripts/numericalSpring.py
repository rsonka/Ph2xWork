'''Rita Sonka
10/11/2016
Ph 20
hw 3
'''
import numpy as np
import matplotlib.pyplot as plt




# Problem 1 ========================================

# Using the w=1 case....
def explicitEuler(x0, v0, h, N):
    TT = np.arange(N+1)*h
    XX = np.zeros([N+1])
    VV = np.zeros([N+1])
    XX[0] = x0
    VV[0] = v0
    for i in range(1, N+1):
        XX[i] = XX[i-1] + h*VV[i-1]
        VV[i] = VV[i-1] - h*XX[i-1]
    return (TT, XX, VV)

def plotExplicitEuler(x0, v0, h, N, saveName):
    (TT, XX, VV) = explicitEuler(x0, v0, h, N)
    #if saveName:
    plotXVT(TT, XX, VV, 'X(t) of spring', 'V(t) of spring', saveName=saveName)
    #else:
    #    plotXVT(TT, XX, VV, 'X(t) of spring', 'V(t) of spring')

def plotXVT(TT, XX, VV, xtitle, vtitle, saveName=""):
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(TT, XX)
    axarr[0].set_title(xtitle)
    axarr[1].plot(TT, VV)
    axarr[1].set_title(vtitle)
    if saveName:
        plt.savefig(saveName, bbox_inches='tight')
    else:
        plt.show()
    plt.gcf().clear()


# Problem 2 ========================================

def analyticEuler(x0, v0, h, N):
    TT = np.arange(N+1)*h
    XX = x0*np.cos(TT) + v0*np.sin(TT)
    VV = - x0*np.sin(TT) + v0*np.cos(TT)
    return (TT, XX, VV)

# Using the w=1 case....
def explicitEulerErrors(x0, v0, h, N):
    (TT, XX, VV) = explicitEuler(x0, v0, h, N)
    (Ta, Xa, Va) = analyticEuler(x0, v0, h, N)
    return (TT, XX - Xa, VV - Va)


def plotExplicitEulerErrors(x0, v0, h, N, saveName):
    (TT, XX, VV) = explicitEulerErrors(x0, v0, h, N)
    plotXVT(TT, XX, VV, 'Xnumeric(t)-Xanalytic(t) of spring', 'Vnumeric(t)-Vanalytic(t) of spring', saveName=saveName)


# Problem 3 ========================================

# It is slowly accumulating more options...
def plotXY(xX, yY, titleString, xlabel, ylabel, logLog=False, semiLogY=False, markPoints=[], saveName=""):
    # xX and yY should be numpy arrays.
    # the below bit was part of me attempting to prove the closed surface thing.
    if semiLogY:
        plt.semilogy(xX, yY, '-bD', markevery=markPoints)
    elif logLog:
        plt.loglog(xX, yY, '-bD', markevery=markPoints)
    else:
        plt.plot(xX, yY,'-bD', markevery=markPoints)
    plt.title(titleString)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if saveName:
        plt.savefig(saveName, bbox_inches='tight')
    else:
        plt.show()
    plt.gcf().clear()

# Using the w=1 case....
def eE_truncation(x0, v0, h0, time, saveName):
    h0 = float(h0)
    HH = np.array([h0, h0/2, h0/4, h0/8, h0/16])
    truncError = np.zeros([5])
    for i in range(5):
        N = int(float(time) / HH[i])+1
        (TT, XX, VV) = explicitEulerErrors(x0, v0, HH[i], N)
        truncError[i] = max(XX)
    plotXY(HH, truncError, "Truncation error of explicit Euler", "h used", "maximum truncation error in " + str(time) + " units of time", saveName=saveName)
    plt.gcf().clear()


# Problem 4 ========================================

def eE_energy(x0, v0, h, N, saveName):
    (TT, XX, VV) = explicitEuler(x0, v0, h, N)
    EE = XX*XX + VV*VV
    plotXY(TT, EE, "Energy x^2+v^2 of numerical explicit Euler", "time", " energy ", saveName=saveName)
    plt.gcf().clear()

# Problem 5 ========================================

# 5.1

# Using the w=1 case....
def implicitEuler(x0, v0, h, N):
    TT = np.arange(N+1)*h
    XX = np.zeros([N+1])
    VV = np.zeros([N+1])
    XX[0] = float(x0)
    VV[0] = float(v0)
    for i in range(1, N+1):
        XX[i] = (XX[i-1] + h*VV[i-1])/(1+h*h)
        VV[i] = (VV[i-1] - h*XX[i-1])/(1+h*h)
    return (TT, XX, VV)

def plotImplicitEuler(x0, v0, h, N, saveName):
    (TT, XX, VV) = implicitEuler(x0, v0, h, N)
    plotXVT(TT, XX, VV, 'X(t) of spring', 'V(t) of spring', saveName=saveName)

# 5.2

# Using the w=1 case....
def implicitEulerErrors(x0, v0, h, N):
    (TT, XX, VV) = implicitEuler(x0, v0, h, N)
    (Ta, Xa, Va) = analyticEuler(x0, v0, h, N)
    return (TT, XX - Xa, VV - Va)

def plotImplicitEulerErrors(x0, v0, h, N, saveName):
    (TT, XX, VV) = implicitEulerErrors(x0, v0, h, N)
    plotXVT(TT, XX, VV, 'Xnumeric(t)-Xanalytic(t) of spring', 'Vnumeric(t)-Vanalytic(t) of spring', saveName=saveName)

# don't have to mimic 3 (yay!)

# 5.4

def iE_energy(x0, v0, h, N, saveName):
    (TT, XX, VV) = implicitEuler(x0, v0, h, N)
    EE = XX*XX + VV*VV
    plotXY(TT, EE, "Energy x^2+v^2 of numerical implicit Euler", "time", " energy ", saveName=saveName)



# PART 2 ===================================================================



# Problem 1 ========================================

def eE_iE_phaseSpace(x0, v0, h, N, saveName1, saveName2):
    (eT, eX, eV) = explicitEuler(x0, v0, h, N)
    (iT, iX, iV) = implicitEuler(x0, v0, h, N)
    plotXY(eX, eV, "Explicit Euler in phase space-starting X/V marked", "X(t)", "V(t)", markPoints = [eX[0]], saveName=saveName1)
    plotXY(iX, iV, "Implicit Euler in phase space-starting X/V marked", "X(t)", "V(t)", markPoints = [iX[0]], saveName=saveName2)


# Problem 2 ========================================

def symplecticEuler(x0, v0, h, N):
    TT = np.arange(N+1)*h
    XX = np.zeros([N+1])
    VV = np.zeros([N+1])
    XX[0] = float(x0)
    VV[0] = float(v0)
    for i in range(1, N+1):
        XX[i] = XX[i-1] + h*VV[i-1]
        VV[i] = VV[i-1] - h*XX[i]
    return (TT, XX, VV)

def symp_phaseSpace(x0, v0, h, N, saveName):
    (sT, sX, sV) = symplecticEuler(x0, v0, h, N)
    plotXY(sX, sV, "Symplectic Euler in phase space-starting X/V marked", "X(t)", "V(t)", markPoints = [sX[0]], saveName=saveName)

# Problem 3 ========================================

def symp_energy(x0, v0, h, N, saveName):
    (TT, XX, VV) = symplecticEuler(x0, v0, h, N)
    EE = XX*XX + VV*VV
    plotXY(TT, EE, "Energy x^2+v^2 of numerical symplectic Euler", "time", " energy ", saveName=saveName)



# Problem 4 ========================================

def symp_lag(x0, v0, h, N, saveName):
    startN = int(float(3)/4*N)
    (TT, XX, VV) = symplecticEuler(x0, v0, h, N)
    (Ta, Xa, Va) = analyticEuler(x0, v0, h, N)
    f, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(TT[startN:], XX[startN:], 'b', Ta[startN:], Xa[startN:], 'r')
    axarr[0].set_title("X(t) versus time: blue symplectic Euler, red analytic solution.")
    axarr[1].plot(TT[startN:], VV[startN:], 'b', Ta[startN:], Va[startN:], 'r')
    axarr[1].set_title("V(t) versus time: blue symplectic Euler, red analytic solution.")
    plt.savefig(saveName, bbox_inches='tight')
    plt.gcf().clear()
            


