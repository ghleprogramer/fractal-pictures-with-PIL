# project fractal something point o

# burning ship fractal
def BurningShip_loop(x, iy, MAXitercount = 50, threshold = 5):    
    """ returns None if the number stays bounded
    returns the number of iterations if the number escapes
    takes RELx, IMGy for a complex number, max iteration count,
    escape threshold hold """

    ic = complex(x, iy)
    Z = ic
    for itercount in range(MAXitercount):
        if abs(Z) > threshold:
            return itercount
        Z = complex(abs(Z.real), abs(Z.imag))**2 + ic
    return None

# mandel brot fractal
def MandelBrot_loop(x, iy, MAXitercount = 10, threshold = 2):
    """ returns None if the number stays bounded
    returns the number of iterations if the number escapes
    takes RELx, IMGy for a complex number, max iteration count,
    escape threshold hold """
    
    ic = complex(x, iy)
    Zn = ic
    for itercount in range(MAXitercount):
        if abs(Zn) > threshold:
            return itercount 
        Zn = Zn**2 + ic
    return None

def FractalSetCreator(Xaxis , iYaxis ,  Func, looplength = 10, threshold = 2):
    """ function takes x axis, iy axis lists, Func fractal function, setaccuracy, looplength, threshold ints
    returns a 2d array[x][y] of the return of the given Func for values in the x and iy range """
    
    MaxVal = 0
    FractalSet = []
    
    def loop_update(FEV, Set, Max):
        Set.append(FEV)
        if FEV == None:    
            return Max
        if FEV > Max:
            Max = FEV
            return Max
        return Max

    for i in Xaxis:
        ySet = []
        for j in iYaxis:
            FractalEscapeVal = Func(i , j, looplength, threshold)  
            MaxVal = loop_update(FractalEscapeVal, ySet, MaxVal)
        FractalSet.append(ySet)

    return (FractalSet, MaxVal)

def CreatListForRange(Range, NumberOfValues):
    """ takes Range tulep or list returns List of values form the start 
    of the Range to the end(exclusive) the length of number of values """
    
    if Range[0] == Range[1] or Range[0] > Range[1]:
        raise ValueError("Range value error Range=(i,j) i<j && i!=j")

    List = []
    i = Range[0]
    numincrease = abs(Range[1] - Range[0]) / NumberOfValues
    while i < Range[1] and len(List) < NumberOfValues:
        List.append(i)
        i += numincrease

    return List

# x = CreatListForRange((5-, 05), 10)
# y = CreatListForRange((0, 4), 10)
# print(x, len(x))
# set = ComplexFractalSetCreator(x, y, ship_loop, threshold = 5)
# file = open("output.txt", "w")
# file.write(str(set))
# file.close()
