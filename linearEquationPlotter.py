# created at : 01/10/2020
# created by : Vivek Patidar

# Linear equation solver and plotter using numpy and matplotlib

# importing numpy and matplotlib

try:
    import numpy as np
    from matplotlib import pyplot as plt
except Exception as e:
    print("Not imported because",e)
    
def plotLinearEquation(eq,xc=1,yc=1,c=1):
    # here eq is the linear equation
    
    # you can change it accordingly
    x = np.arange(-10,10,0.5)
    
    # the basic calculation of y from (xc*x + yc*y + c = 0)
    y = (-xc * x - c)/yc
    
    ax = plt.subplot()
    
    ax.plot(x,y)
    
    ax.grid(True)
    
    plt.title(eq)
    plt.xlabel("X axis ------>")
    plt.ylabel("Y axis ------>")
    
    # for including the origin (0,0)
    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k') 


def findXYC(stri):
    
    stri.replace(" ","") # remove all the white spaces

    e = len(stri) # if = is not found, then take constant till the end of string

    if("=" in stri): # if = is found then get its position and take constant before equals
        e = stri.find("=")

    res = []

    i = stri.find("x") # finding the position of x

    j = stri.find("y") # finding the position of y

    li = list(stri) # creating a list of the string to extract the values

    x = ''.join(map(str,li[:i])) # slicing the list for constant of x

    y = ''.join(map(str,li[i+1:j])) # slicing the list for constant of y

    c = ''.join(map(str,li[j+1:e])) # slicing the list for constant value (c)

    # some conditional formatting when constants of x = 1 or of y = 1 or c is not available
    if x=='':
        x='1'
    if y=='+':
        y='1'
    if c=='':
        c='0'
    
    # inserting the constants into result list
    res.append(int(x))
    res.append(int(y))
    res.append(int(c))
    
    # returning the result list
    return(res)
   
if __name__ == "__main__": 
    
    # take user input here (in form of ax + by + c = 0)
    stri = input("Enter equation in the form of ax + by + c = 0\n")
    
    # getting constants of every variable
    list1 = findXYC(stri)
    
    # plotting the graph
    plotLinearEquation(stri,list1[0],list1[1],list1[2])