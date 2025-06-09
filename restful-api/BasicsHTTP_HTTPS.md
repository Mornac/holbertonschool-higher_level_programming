<h1 align="center">Basics of HTTP/HTTPS</h1>

# **Background**  
The objective is to understand how to communicate
and transfer data efficiently between systems.    
We can differentiate HTTP and HTTPS, understand the basic working and structure of HTTP requests and responses. 
We can recognize and explain the common HTTP methods and status codes.   

## **1 Differences between HTTP and HTTPS**
|Items|HTTP|HTTPS|
|-----|----|-----|
|URL Prefix|http://|https://|
|Requests|In readable text|In encrypted text|
|Responses|In readable text|In encrypted text|
|Identity|No verification of identity|Verification of identity|
Encryption|No encrytpion|TLS SSL certificates|
|Port|Port 80|Port 443|
|Speed|More speed|Less speed|

The protocol HTTPS encrypts its data, and allows them to be secured by making them unreadable. While HTTP gets and posts in readable data.
The S of HTTPS is Security to facilitate the understanding.
HTTPS use a TLS SSL encrytion while HTTP doesn't use any encryption.
HTTP is more speed to treat requests and responses than HTTPS.  


## **2 Structure of an HTTP request and response**
Exemple de site: http://informatique.p.tous.free.fr/crbst_10.html  

****Headers section****   
Request URL: http://informatique.p.tous.free.fr/crbst_10.html  
***Request Method***  
GET  
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
![Plan of the timing]{https://github.com/Mornac/holbertonschool-higher_level_programming/blob/main/restful-api/image/restful_api%20Timing.png}  
