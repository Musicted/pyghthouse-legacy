# pyghthouse
Legacy Python API for CAU Lighthouse  

Requires https://pypi.org/project/umsgpack/ and https://pypi.org/project/websocket_client/  
...or install dependencies by running `pip install -r requirements.txt`.  

Initialize like this: `Pyghthouse(username, api_token)`.  
Open a connection: `start()`.  
Send an image: `send(img = None, verbose = False)`, where `img` is an iterable of integers from 0 to 255 of length 1176 (8-bit R, G and B values for every pixel, from left to right and top to bottom). If `img` is `None`, the most recently sent image is re-sent (which keeps the image from timing out on the actual lighthouse). Set `verbose` to `True` in order to print the server's response to the console.


Minimal usage example:
```
import pyghthouse

ph = pyghthouse.Pyghthouse('USERNAME', 'API-TOKEN')
ph.start()

i = 0
while True:
	img = [(i + (j//3)) % 256 for j in range(1176)]
	ph.send(verbose = True)
	i += 1
```
