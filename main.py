#!/usr/bin/python
import sys
def print_menu():
    print("Select menu: 1)bin 2)set 3)fibo 4)exit ?")           
     
    inputed_number = int(input(" "))
      
    if inputed_number == 1:
       print("1")

    elif inputed_number == 2:
       print("2")
    elif inputed_number == 3:
       print("3")         
    elif inputed_number == 4:
       print("exit the program...")
       exit()
    else:                                                                              print("번호를 다시 입력하세요.")
if__name__=='__main__':
    while True:                                                                        print_menu()
