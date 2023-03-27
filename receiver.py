from vidstream import StreamingServer
import threading

receiver = StreamingServer('IPv4 Address', 50649)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()