<h1 align="center">Basics of HTTP/HTTPS</h1>

# **Background**  
The objective is to understand how to communicate
and transfer data efficiently between systems.  
We aim to differentiate between HTTP and HTTPS, understand the basic structure of HTTP requests and responses,  
recognize and explain common HTTP methods and status codes.   

## **1 Differenciating HTTP and HTTPS**
|Item|HTTP|HTTPS|
|-----|----|-----|
|URL Prefix|http://|https://|
|Requests|In readable text|In encrypted text|
|Responses|In readable text|In encrypted text|
|Identity|No identity verification|Identity verification|
Encryption|No encrytpion|TLS SSL certificates|
|Port|Port 80|Port 443|
|Speed|Faster|Slower|

The protocol HTTPS encrypts data, and allows them to be secured by making them unreadable, while HTTP sends and receives data in readable text.
The S of HTTPS stands for "Secure" which helps to understanding its purpose.
HTTPS use a TLS SSL encrytion while HTTP doesn't use any encryption.
HTTP is more speed to treat requests and responses than HTTPS because it doesn't perform encryption and decryption.  

## **2 Understanding HTTP Structure**  
Here is an example of an HTTP exchange when accessing the website: http://informatique.p.tous.free.fr/crbst_10.html.  
This is the structure of an HTTP request and response. 

****Request****  
Request URL: http://informatique.p.tous.free.fr/crbst_10.html  
***Request Method***  
GET  
****Response****  
***Status Code***  
304 Not Modified

****Response Headers****  
***connection***  
close  
***date***  
Mon, 09 Jun 2025 12:24:47 GMT  
***server***
Apache/ProXad [Jan 23 2019 20:05:46]  

****Request Headers:****  
***accept***  
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7  
***accept-encoding***  
gzip, deflate  
***accept-language***  
fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7  
***cache-control***  
max-age=0  
***connection***  
keep-alive  
***host***  
informatique.p.tous.free.fr  
***referer***  
https://www.google.com/  
***upgrade-insecure-requests***  
1  
***user-agent***  
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36  

****Timing****
![Plan of the timing](https://github.com/Mornac/holbertonschool-higher_level_programming/blob/main/restful-api/image/restful_api%20Timing.png)  
- Queueing: Wait before the request starts (browser is busy or prioritizing).  
- Stalled: Total time before the browser sends the request.  
- DNS Lookup: time to find the IP address of the website.  
- Initial connection: time to connect to the server.  
- SSL/TLS Negotiation (HTTPS only): secure handshake to encrypt communication.  
- Request sent: time it takes to send the request to the server.  
- Waiting: Time from request sent to receiving the first byte of the response.  
- Content download: time to download the entire response content.  

## **3 Exploring HTTP Methods and Status Codes**  
I made a list of 4 common HTTP methods, its use and an example of a real situation: a e-commerce website.  
Followed by a list of 5 common HTTP status codes, with a brief description and an example of use.

### **List of 4 common HTTP methods**
|HTTP Method|Use|Syntax|
|-----------|---|------|
|GET|Read or retrieve data from a given server using a specified URI|requests.get(url, params={key: value}, args)|
|POST|Send data to the server to create or update resources|requests.post(url, params={key: value}, args)|
|PATCH|Modify resources. Needs to contain the changes to the resource, not the complete resource|requests.patch(url, params={key: value}, args)
|DELETE|Delete a resource identified by filters or ID|requests.delete(url, params={key: value}, args)|  

****Example: HTTP Methods in an E-commerce website****  
- A customer views the product page of shoes:  
**method=GET**: retrieves product details  
There is no changes made to the database: it's a read information.  
- The seller adds a new product via the admin dashboard:  
**method=POST**: creates a new product entry  
A full product object is submitted and saved.  
- The seller updates the new price for an existing product:  
**method=PATCH**: updates only the price field.  
It's a partial update : only the provided fields are updates.  
- The seller removes a product that is out of stock:  
**method=DELETE**: deletes the product from the database.  
The product is permanently removed, no longer shown to users.  

### **List of 5 common HTTP status codes**  
****HTTP GET****  
|Status code|Description|Scenario where encountered|
|-----------|-----------|--------------------------|
|200|Success / OK - The request was successful|HTTP GET API: the resource is found on the server|
|404|Not found - The resource doesn't exist|The resource is not found on the server|
|400|Bad request - The request is malformed|The GET request itself is not correctly formed: syntax or parameters are incorrect|

****HTTP POST****  
|Status code|Description|Scenario where encountered|
|-----------|-----------|--------------------------|
|201|Created - A new resource was crated|Resource has been created on the origin server|

****HTTP DELETE****  
|Status code|Description|Scenario where encountered|
|-----------|-----------|--------------------------|
|202|Accepted - The request was accepted for processing but not yet completed|The action has been queued|  
