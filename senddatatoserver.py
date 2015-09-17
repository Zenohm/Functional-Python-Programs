def send_to_server(input):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost',8081))
    message = bytes(input, 'UTF-8')
    s.send(message)
    data = s.recv(2048).decode('UTF-8')
    s.close()
    data = str(data)
    print('Received:')
    return data

