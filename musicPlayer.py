# -*- coding: utf-8 -*-
"""
Spyder Editor

a  script file.
"""
import webbrowser as wb
choice = 0
def mood(choice):
        if choice == 1:
            wb.open('https://www.youtube.com/watch?v=-boKk8uhmcY&list=PLKe9CVqEUDMGhEM42kKWsVt0SScAE1r0X')
        elif choice == 5:
            wb.open('https://www.youtube.com/watch?v=RgKAFK5djSk&list=PLKe9CVqEUDME-e6ulWPdlV7vt3T5PaHi5')
        elif choice == 2:
            wb.open('https://www.youtube.com/watch?v=TW9d8vYrVFQ&list=PLKe9CVqEUDMEYvAy57HkCNfVBprD18cA-')
        elif choice == 3:
            wb.open('https://www.youtube.com/watch?v=xLPGtQoRUbk&list=PLKe9CVqEUDMEcpW3Zy2KJWTcPpTGtKAck')
        elif choice == 4:
            wb.open('https://www.youtube.com/watch?v=yZIummTz9mM&list=PLKe9CVqEUDMH77Bk07v8esKG5L83UOFjH')
        else :
            print('please choose the options from the list !')
choice = int(input('choose the type of music you want : \n1) mix \n2) edm \n3) pop \n4) rock  \n5) chill\nEnter your input:'))        
mood(choice)
