# EX01 Developing a Simple Webserver
## Date:14-03-2025

## AIM:
To develop a simple webserver to create a lyrics searching webpage

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lyrics Search</title>
</head>
<body>
    <h1>Lyrics Search</h1>
    <input type="text" id="song" placeholder="Enter song name">
    <button onclick="searchLyrics()">Search</button>
    <div id="lyrics"></div>
    
    <script>
        function searchLyrics() {
            document.getElementById('lyrics').innerHTML = "Lyrics will appear here.";
        }
    </script>
</body>
</html>
~~~
## OUTPUT:

[alt text](exp1-webexp-2.png)
[alt text](exp1-webexp-1.png)

## RESULT:
The program for implementing simple webserver is executed successfully.

