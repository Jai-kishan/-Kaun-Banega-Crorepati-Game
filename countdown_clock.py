# def countdown(t):
#     import time
#     print('This window will remain open for 3 more seconds...')
#     while t >= 0:
#         print(t, end='...')
#         time.sleep(1)
#         t -= 1
#     print('Goodbye! \n \n \n \n \n')

# t=3
# print (countdown(7))


import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')

countdown(60)