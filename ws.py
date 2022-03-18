from websocket import create_connection


def on_message():
	print("MESSAGE")

def on_error():
	print("ERROR")

def on_close():
	print("CLOSE")

def on_open():
	print("OPEN")


ws = create_connection("ws://dev2.0build-partner.goexfx.com:8000/api/exfx/v2/chat/message/97/",
								on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open
                               )
print(ws.recv())