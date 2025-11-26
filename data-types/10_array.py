from array import array
# TypeCode  C Type                  Python Type
'b'         # signed char           int(1Byte)
'B'         # unsigned char         int(1Byte)
'h'         # signed short          int(2Byte)
'H'         # unsigned short        int(2Byte)
'i'         # signed int            int(2Byte)
'I'         # unsigned int          int(2Byte)
'l'         # signed long           int(4Byte)
'L'         # unsigned long         int(4Byte)
'q'         # signed long long      int(8Byte)
'Q'         # unsigned long long    int(8Byte)
'f'         # float                 float(4Byte)
'd'         # double                float(8Byte)

numbers = array('i', [1, 2, 3])
# numbers[0] = 10.0 # error

numbers.append(4)
print(numbers)
print(type(numbers))