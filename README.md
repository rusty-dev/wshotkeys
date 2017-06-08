#### About:

Lightweight WebSocket server that listens to keyboard events and reports requested hot-keys to connected clients.

##### Requirements:

 * python >= 3.4
 * modules: click, keyboard, websockets

##### CLI Usage (wshotkeys --help):

```
Usage: wshotkeys [OPTIONS]

  WebSocket hot-key server.

Options:
  -a, --addr TEXT     Run WebSocket server on this address.
  -p, --port INTEGER  Run WebSocket server on this port.
  --help              Show this message and exit.
```
#### WebSocket usage:

After connecting to server, you are required to send one message, describing all the hot-keys in json format.
Expected json is an array of objects with fields "keys" and "message":
```json
[ { "keys": "win+left", "message": "msg1"}, ... ]
```
Each object descries an individual hot-key, `keys` field describes the hot-key. And `message` field describes the message that server sends back to client when the hotkey activates.


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
              ws.send(JSON.stringify([{keys:'left ctrl+f1', message: 'CTRL+F1 Pressed'}]));
            }
            document.body.appendChild(messages);
        </script>
    </body>
</html>
```
This will connect to existing server and define 1 hot-key: CTRL+F1. If everything works correctly, pressing CTRL+F1 anywhere should print "CTRL+F1 Pressed" message in browser.
