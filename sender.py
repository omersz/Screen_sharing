from vidstream import ScreenShareClient
import threading

sender =ScreenShareClient('IPv4 Address', 50649)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != "STOP":
    continue

sender.stop_stream()

