import socket
PORT = 11113
BUFFER_SIZE = 1024

def str2morse(number):
    '''
    This function takes a string input called number (which will only be
    numbers and a period and translate it to morse code
    '''
    if number == '0':
        return '-----'
    elif number == '1':
        return '.----'
    elif number == '2':
        return '..---'
    elif number == '3':
        return '...--'
    elif number == '4':
        return '....-'
    elif number == '5':
        return '.....'
    elif number == '6':
        return '-....'
    elif number == '7':
        return '--...'
    elif number == '8':
        return '---..'
    elif number == '9':
        return '----.'
    elif number == '.':
        return '.-.-.-'

with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind (('0.0.0.0', PORT))
    s.listen ()
    while True:
        connection, client = s.accept ()
        client_ip = str(client[0])
        morse = ''
        for num in client_ip:
            morse += str2morse(num)
        try:
            print ('Client connected', client)
            connection.send (str.encode(morse))
        finally:
            connection.close ()
