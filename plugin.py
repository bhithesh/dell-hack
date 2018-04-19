import sublime, sublime_plugin

import socket
from threading import Thread

URL = "0.0.0.0"
PORT = 12345

def send_data_to_server(data):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    soc.connect((URL, PORT))
    print("sending: " + data)
    soc.send(data.encode("utf8"))

    soc.close()


class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("test")
        # self.view.line(self.selection)

        line_string = self.view.substr(self.view.line(self.view.sel()[0]))

        # response = urllib.request.urlopen('http://192.168.0.82:5000/receive_from_sublime?intent=SQL_QUERY&q='+urllib.parse.quote(line_string))
        Thread(target=send_data_to_server, args=(line_string,)).start()
        
