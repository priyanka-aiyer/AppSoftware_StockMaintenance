### Stock Maintenance of Vending Machine

class VendingMachine:
    '''
        >>> x=VendingMachine()
        >>> print(x)
        Vending Machine stock
        Chocolate: 0 unit(s)
        Nuts: 0 unit(s)
        Chips: 10 unit(s)
        Soda: 0 unit(s)
        >>> x.getStock()     # {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 10], 879: [3.0, 0]} is also ok
        {156: [0, 0], 254: [0, 0], 384: [2.5, 10], 879: [0, 0]}
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.isStocked
        True
        >>> x.restock(156, 9)
        'Current item stock: 9'
        >>> x.getStock()
        {156: [1.5, 9], 254: [0, 0], 384: [2.5, 10], 879: [0, 0]}
        >>> x.purchase(156)
        'Please deposit $1.5'
        >>> x.purchase(156,2)
        'Please deposit $3.0'
        >>> x.purchase(156,23)
        'Current 156 stock: 9, try again'
        >>> x.deposit(3)
        'Balance: $3'
        >>> x.purchase(156,3)
        'Please deposit $1.5'
        >>> x.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> x.getStock()
        {156: [1.5, 8], 254: [0, 0], 384: [2.5, 10], 879: [0, 0]}
        >>> x.purchase(254)
        'Item out of stock'
        >>> x.deposit(300)
        'Balance: $300'
        >>> x.purchase(876)
        'Invalid item'
        >>> x.purchase(384,10)
        'Item dispensed, take your $275.0 back'
        >>> x.purchase(156,10)
        'Current 156 stock: 8, try again'
        >>> x.purchase(156,8)
        'Please deposit $12.0'
        >>> x.deposit(12)
        'Balance: $12'
        >>> x.purchase(156,8)
        'Item dispensed'
        >>> x.getStock()
        {156: [1.5, 0], 254: [0, 0], 384: [2.5, 0], 879: [0, 0]}
        >>> x.isStocked
        False
        >>> x.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> x.purchase(156,2)
        'Machine out of stock'
    '''

    # Initializing values of Class Attributes 
    productID_1 = 156
    productID_2 = 254
    productID_3 = 384
    productID_4 = 879

    productID_1_Name = 'Chocolate'
    productID_2_Name = 'Nuts'
    productID_3_Name = 'Chips'
    productID_4_Name = 'Soda'

    productID_1_Price = 1.5
    productID_2_Price = 2.0
    productID_3_Price = 2.5
    productID_4_Price = 3.0

    # To be used in setName() and setPrice() functions
    dictProductName = { productID_1: productID_1_Name, productID_2: productID_2_Name, productID_3: productID_3_Name, productID_4: productID_4_Name }
    dictProductPrice = { productID_1: productID_1_Price, productID_2: productID_2_Price, productID_3: productID_3_Price, productID_4: productID_4_Price }
    
    def __init__(self):

        #--- YOUR CODE STARTS HERE
        self.dictProductStock = { self.productID_1: 0, self.productID_2: 0, self.productID_3: 10, self.productID_4: 0 }

        # Setting initial value of displayProductStock; used in getStock() to check if Stock has been Zero from start
        if self.dictProductStock[self.productID_1] == 0 :
            self.displayProductStock1 = 0
        if self.dictProductStock[self.productID_2] == 0 : 
            self.displayProductStock2 = 0
        if self.dictProductStock[self.productID_3] == 0 :
            self.displayProductStock3 = 0
        if self.dictProductStock[self.productID_4] == 0 :
            self.displayProductStock4 = 0

        self.amountToDeposit = 0
        self.amountToBeReturned = 0
        self.amountDeposited = 0
        self.displayDictProductPrice = 0


    def __str__(self):
        #--- YOUR CODE STARTS HERE
        # To format display of output as per some doctest cases
        return 'Vending Machine stock\n{}: {} unit(s)\n{}: {} unit(s)\n{}: {} unit(s)\n{}: {} unit(s)'.format(self.dictProductName[self.productID_1], self.dictProductStock[self.productID_1], self.dictProductName[self.productID_2], self.dictProductStock[self.productID_2], self.dictProductName[self.productID_3], self.dictProductStock[self.productID_3], self.dictProductName[self.productID_4], self.dictProductStock[self.productID_4])
        

    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        return

    def purchase(self, item, *args):
        #--- YOUR CODE STARTS HERE
        self.qty = 1

        #If more than one argument is entered, then get the qty value
        for x in args:
            self.qty = x
        
        # Check if 'amount' value is a positive integer or float 
        if isinstance(self.qty, (int, float)) == False or self.qty <= 0 :
            return 'Invalid qty'

        # Check if entered 'item' is valid ProductID for purchase 
        if (item == self.productID_1 or item == self.productID_2 or item == self.productID_3 or item == self.productID_4) :
            
            if self.isStocked == False :
                return 'Machine out of stock'  

            if self.dictProductStock[item] == 0 :
                return 'Item out of stock'

            if self.dictProductStock[item] < self.qty :
                return 'Current {} stock: {}, try again'.format( item, self.dictProductStock[item] )

            # Compute cost value
            self.cost = self.qty * self.dictProductPrice[item]

            if ( self.cost > self.amountDeposited ):
                self.amountToDeposit = self.cost - self.amountDeposited    
                return 'Please deposit ${}'.format( self.amountToDeposit )
            else:
                self.dictProductStock[item] -= self.qty

                # Setting displayProductStock value to -1 for formatting display in getStock() as per doctest case
                if item == self.productID_1 :
                    self.displayProductStock1 = -1
                if item == self.productID_2 :
                    self.displayProductStock2 = -1
                if item == self.productID_3 :
                    self.displayProductStock3 = -1
                if item == self.productID_4 :
                    self.displayProductStock4 = -1

                self.amountToBeReturned = self.amountDeposited - self.cost
                self.amountDeposited = 0

                if self.amountToBeReturned > 0 :
                    return 'Item dispensed, take your ${} back'.format( self.amountToBeReturned)
                else :
                    return 'Item dispensed'
                
        else:
            return 'Invalid item'     


    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        # Check if 'amount' value is a positive integer or float 
        if isinstance(amount, (int, float)) == False or amount <= 0 :
            return 'Invalid amount'

        # Check if the stock of all Products is Zero
        if self.isStocked == False :
            return 'Machine out of stock. Take your ${} back'.format(amount)

        self.amountDeposited += amount
        #if amount > self.amountDeposited :
        #    self.amountDeposited = amount - self.amountDeposited
        #else :
        #    self.amountDeposited = self.amountDeposited - amount

        return 'Balance: ${}'.format(self.amountDeposited)


    def restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        # Check if 'stock' value is a positive integer or float 
        if isinstance(stock, (int, float)) == False or stock <= 0 :
            return 'Invalid Stock-qty'

        # Check if entered 'item' is valid ProductID and then restock
        if (item == self.productID_1 or item == self.productID_2 or item == self.productID_3 or item == self.productID_4) :
            self.dictProductStock[item] += stock
            return 'Current item stock: {}'.format(self.dictProductStock[item])
        else:
            return 'Invalid item'     


    @property
    def isStocked(self):
        #--- YOUR CODE STARTS HERE
        # Checking if the Stock of all Products is Zero
        if (self.dictProductStock[self.productID_1] == 0 and self.dictProductStock[self.productID_2] == 0 and self.dictProductStock[self.productID_3] == 0 and self.dictProductStock[self.productID_4] == 0 ) :
            return False
        else :
            return True

   
    def getStock(self):

        #--- YOUR CODE STARTS HERE
        # Check if Stock of all Products is Zero
        if self.isStocked == False:
            # Check displayProductStock to ensure if the Stock has been 0 from start & was never restocked or purchased
            # This validation is done to format the display of the Price, Stock as expected in some doctest cases
            if self.displayProductStock1 == 0 :
                self.value_list1 = [0, 0]
            else :
                self.value_list1 = [self.dictProductPrice[self.productID_1], self.dictProductStock[self.productID_1]]

            if self.displayProductStock2 == 0 :
                self.value_list2 = [0, 0]
            else :
                self.value_list2 = [self.dictProductPrice[self.productID_2], self.dictProductStock[self.productID_2]]

            if self.displayProductStock3 == 0 :
                self.value_list3 = [0, 0]
            else :
                self.value_list3 = [self.dictProductPrice[self.productID_3], self.dictProductStock[self.productID_3]]

            if self.displayProductStock4 == 0 :
                self.value_list4 = [0, 0]
            else :
                self.value_list4 = [self.dictProductPrice[self.productID_4], self.dictProductStock[self.productID_4]]
    
            self.dictStock = { self.productID_1: self.value_list1, self.productID_2: self.value_list2, self.productID_3: self.value_list3, self.productID_4: self.value_list4 }
            return self.dictStock


        # This validation is done to format the display of the Price, Stock as expected in certain doctest cases
        self.displayDictProductPrice = 0
        if self.dictProductStock[self.productID_1] != 0 :
            self.displayDictProductPrice = self.dictProductPrice[self.productID_1]
        self.value_list1 = [self.displayDictProductPrice, self.dictProductStock[self.productID_1]]

        self.displayDictProductPrice = 0
        if self.dictProductStock[self.productID_2] != 0 :
            self.displayDictProductPrice = self.dictProductPrice[self.productID_2]
        self.value_list2 = [self.displayDictProductPrice, self.dictProductStock[self.productID_2]]

        self.displayDictProductPrice = 0
        if self.dictProductStock[self.productID_3] != 0 :
            self.displayDictProductPrice = self.dictProductPrice[self.productID_3]
        self.value_list3 = [self.displayDictProductPrice, self.dictProductStock[self.productID_3]]

        self.displayDictProductPrice = 0
        if self.dictProductStock[self.productID_4] != 0 :
            self.displayDictProductPrice = self.dictProductPrice[self.productID_4]
        self.value_list4 = [self.displayDictProductPrice, self.dictProductStock[self.productID_4]]

        self.dictStock = { self.productID_1: self.value_list1, self.productID_2: self.value_list2, self.productID_3: self.value_list3, self.productID_4: self.value_list4 }
        return self.dictStock


    def setName(self, item, new_name):
        #--- YOUR CODE STARTS HERE
        # Setting the VendingMachine class attribute value with the new Name for respective ProductID
        if (item == self.productID_1):
            VendingMachine.productID_1_Name = new_name
            VendingMachine.dictProductName = { VendingMachine.productID_1: VendingMachine.productID_1_Name, self.productID_2: self.productID_2_Name, self.productID_3: self.productID_3_Name, self.productID_4: self.productID_4_Name }
        elif (item == self.productID_2):
            VendingMachine.productID_2_Name = new_name                       
            VendingMachine.dictProductName = { self.productID_1: VendingMachine.productID_1_Name, VendingMachine.productID_2: VendingMachine.productID_2_Name, self.productID_3: self.productID_3_Name, self.productID_4: self.productID_4_Name }
        elif (item == self.productID_3):
            VendingMachine.productID_3_Name = new_name
            VendingMachine.dictProductName = { self.productID_1: VendingMachine.productID_1_Name, self.productID_2: self.productID_2_Name, VendingMachine.productID_3: VendingMachine.productID_3_Name, self.productID_4: self.productID_4_Name }         
        elif (item == self.productID_4):
            VendingMachine.productID_4_Name = new_name
            VendingMachine.dictProductName = { self.productID_1: VendingMachine.productID_1_Name, self.productID_2: self.productID_2_Name, self.productID_3: self.productID_3_Name, VendingMachine.productID_4: VendingMachine.productID_4_Name }          
        else:
            return 'Invalid item'     

        return new_name



    def setPrice(self, item, new_price):
        #--- YOUR CODE STARTS HERE
        # Setting the VendingMachine class attribute value with the new Price for respective ProductID
        if (item == self.productID_1):
            VendingMachine.productID_1_Price = new_price
            VendingMachine.dictProductPrice = { VendingMachine.productID_1: VendingMachine.productID_1_Price, self.productID_2: self.productID_2_Price, self.productID_3: self.productID_3_Price, self.productID_4: self.productID_4_Price }
        elif (item == self.productID_2):
            VendingMachine.productID_2_Price = new_price                       
            VendingMachine.dictProductPrice = { self.productID_1: self.productID_1_Price, VendingMachine.productID_2: VendingMachine.productID_2_Price, self.productID_3: self.productID_3_Price, self.productID_4: self.productID_4_Price }
        elif (item == self.productID_3):
            VendingMachine.productID_3_Price = new_price
            VendingMachine.dictProductPrice = { self.productID_1: self.productID_1_Price, self.productID_2: self.productID_2_Price, VendingMachine.productID_3: VendingMachine.productID_3_Price, self.productID_4: self.productID_4_Price }        
        elif (item == self.productID_4):
            VendingMachine.productID_4_Price = new_price
            VendingMachine.dictProductPrice = { self.productID_1: self.productID_1_Price, self.productID_2: self.productID_2_Price, self.productID_3: self.productID_3_Price, VendingMachine.productID_4: VendingMachine.productID_4_Price }           
        else:
            return 'Invalid item'     

        return new_price




class Complex:
    '''
        >>> a=Complex(5.2,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7.2, 8i)
        >>> a-b
        (3.2, -20i)
        >>> a*b
        (94.4, 60.8i)
        >>> a/b
        (-0.368, -0.424i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> 5+a
        (10.2, -6i)
        >>> a+5
        (10.2, -6i)
        >>> 5-b
        (3, -14i)
        >>> b-5
        (-3, 14i)
        >>> print(a)
        5.2-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
    '''
    def __init__(self, real, imag):
        # You are not allowed to modify the constructor
        self.real = real
        self.imag = imag


    #--- YOUR CODE STARTS HERE
    OpFlag = ''

    def __str__(self):

        displayRealNum = self.real
        displayImagNum = self.imag

        # To format the display of resultStr as expected in doctest
        realStr = str(displayRealNum)
        imagStr = str(displayImagNum)+'i'
        if (Complex.OpFlag == '+' or Complex.OpFlag == '-' or Complex.OpFlag == '*' or Complex.OpFlag == '/') :
            resultStr = '(' + realStr + ", " + imagStr + ')'
        else:
            resultStr = '{}{:+}i'.format(displayRealNum, displayImagNum)

        Complex.OpFlag = ''
        return f'{resultStr}'

    
    def __repr__(self):

        displayRealNum = self.real
        displayImagNum = self.imag

        # To format the display of resultStr as expected in one of the doctest case
        realStr = str(displayRealNum)
        imagStr = str(displayImagNum)+'i'
        resultStr = '(' + realStr + ", " + imagStr + ')'

        Complex.OpFlag = ''
        return f'{resultStr}'


    def __add__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        # Addition of Complex Numbers
        Complex.OpFlag = '+'
        computedRealNum = self.real + other.real
        computedImagNum = self.imag + other.imag

        returnObject = Complex(computedRealNum, computedImagNum) 
        return returnObject
    

    def __radd__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        Complex.OpFlag = '+'
        if isinstance(other, (float,int)):
            newOther = Complex(other, 0)
            newOther.real = other
            newOther.imag = 0

        return newOther.__add__(self)


    def __sub__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        # Subtraction of Complex Numbers
        Complex.OpFlag = '-'
        computedRealNum = self.real - other.real
        computedImagNum = self.imag - other.imag

        returnObject = Complex(computedRealNum, computedImagNum) 
        return returnObject


    def __rsub__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        Complex.OpFlag = '-'
        if isinstance(other, (float,int)):
            newOther = Complex(other, 0)
            newOther.real = other
            newOther.imag = 0

        return newOther.__sub__(self)


    def __mul__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        # Multiplication of Complex Numbers
        Complex.OpFlag = '*'
        computedPart1 = (self.real * other.real - self.imag * other.imag)
        computedPart2 = (self.imag*other.real + self.real*other.imag)

        returnObject = Complex(computedPart1, computedPart2)        
        return returnObject


    def __rmul__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        Complex.OpFlag = '*'
        if isinstance(other, (float,int)):
            newOther = Complex(other, 0)
            newOther.real = other
            newOther.imag = 0

        return newOther.__mul__(self)


    def __truediv__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple, float, int)) :
            raise TypeError('Invalid Operation')
            return None

        # Division of Complex Numbers
        Complex.OpFlag = '/'
        numerator1 = (self.real * other.real + self.imag * other.imag)
        numerator2 = (self.imag * other.real - self.real * other.imag)
        denominator = (other.real**2 + other.imag**2)
        # Check to raise ZeroDivisionError if denominator is zero
        if denominator == 0 :
            raise ZeroDivisionError('Denominator cannot be zero')
            return None

        returnObject = Complex ( numerator1 / denominator, numerator2 / denominator )       
        return returnObject


    def __rtruediv__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        # Allow only Complex / Complex in division Operation 
        if isinstance(other, (str, list, dict, tuple, float, int)) :
            raise TypeError('Invalid Operation')
            return None

        Complex.OpFlag = '/'
        newOther = 0
        if isinstance(other, (float,int)):
            newOther = Complex(other, 0)
            newOther.real = other
            newOther.imag = 0

        return newOther.__truediv__(self)


    def __eq__(self, other):

        # Check for TypeError i.e. 'Invalid Operation'
        if isinstance(other, (str, list, dict, tuple)) :
            raise TypeError('Invalid Operation')
            return None

        # Equality of Complex Numbers
        return self.real == other.real and self.imag == other.imag