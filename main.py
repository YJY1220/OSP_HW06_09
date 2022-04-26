#2021113750 유지예

#!/usr/bin/python
import sys
import bin_to_hex
import setcys
import fibonacci

def print_menu():
    print("Select menu: 1)bin 2)set 3)fibo 4)exit ?", end="")           
     
    inputed_number = int(input(""))
      
    if inputed_number == 1:
       bin_to_hex.binTohex()
       print()
    elif inputed_number == 2:
       setcys.set1()
       print()
    elif inputed_number == 3:
       fibonacci.fibonacci() 
       print()
    elif inputed_number == 4:
       print("exit the program...")
       exit()
    else:                                                                              print("번호를 다시 입력하세요.")
if __name__ == "__main__":
    while True:                                                                        print_menu()
