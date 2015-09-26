"""Led Zeppelin - Simple HTTP server for toggling LEDs connected to GPIO 17""" 
import RPi.GPIO as GPIO
import BaseHTTPServer as server


PIN=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

class LedHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if '/on' == self.path:
            GPIO.output(PIN, True)
        elif '/off' == self.path:
            GPIO.output(PIN, False)
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    httpd = server.HTTPServer(('', 8080), LedHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    GPIO.cleanup()
