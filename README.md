#### About:

Lightweight WebSocket server that listens to keyboard events and reports requested hot-keys to connected clients.

##### Requirements:

 * python >= 3.4
 * modules: evdev, websockets

##### CLI Usage (wshotkeys --help):

```
usage: WebSocket hot-key server. [-h] [-p PORT] [-a ADDR] [-k KEYBOARD]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Run WebSocket server on this port.
  -a ADDR, --addr ADDR  Run WebSocket server on this address. [SECURITY RISK]:
                        Using 0.0.0.0 will allow anyone to log your keyboard
                        activity, only set this if you REALLY know what you're
                        doing.
  -k KEYBOARD, --keyboard KEYBOARD
                        Path to keyboard device (auto-detected if unset).
```
#### WebSocket usage:

After connecting to server, you are required to send one message, describing all the hot-keys in json format.
Expected json is an array of objects with fields "keys" and "message":
```json
[ { "keys": ["KEY_1", ...], "message": "msg1"}, ... ]
```
Each object descries an individual hot-key, `keys` field describes all the buttons that need to be pressed simultaneously to activate the hot-key. And `message` field describes the message that server sends back to client when the hotkey activates.

#### Available key codes:

All the key codes are defined using their linux constant names:
https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h#L75

#### Example usage (client):
```html
<!DOCTYPE html>
<html>
    <head>
        <title>wshotkeys demo</title>
    </head>
    <body>
        <script>
            var ws = new WebSocket("ws://127.0.0.1:46724/"),
                messages = document.createElement('ul');
            ws.onmessage = function (event) {
                var messages = document.getElementsByTagName('ul')[0],
                    message = document.createElement('li'),
                    content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };
            ws.onopen = function() {
              ws.send(JSON.stringify([{keys:['KEY_LEFTCTRL', 'KEY_F1'], message: 'CTRL+F1 Pressed'}]));
            }
            document.body.appendChild(messages);
        </script>
    </body>
</html>
```
This will connect to existing server and define 1 hot-key: CTRL+F1. If everything works correctly, pressing CTRL+F1 anywhere should print "CTRL+F1 Pressed" message in browser.
