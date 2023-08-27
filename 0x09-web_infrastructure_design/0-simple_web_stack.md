# 0x09. Web infrastructure design

## What is a Server?
A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network. In theory, whenever computers share resources with client machines they are considered servers.

## Role of the Domain Name
A domain name is the address where users can access a website. It's used to find and identify computers on the Internet. Computers use IP addresses, which are a series of number. However, it is difficult for humans to remember strings of numbers so we use domain names instead.

## DNS Record
In the context of www.foobar.com, 'www' is typically an A or AAAA type DNS record. It's used to point a domain or subdomain to an IP address. 

## Role of the Web Server
A web server's main role is to store and deliver web pages to clients upon request. It communicates with the client's browser and sends the requested resources along with HTTP headers.

## Role of the Application Server
An application server serves web-based applications to client devices. It performs operations such as reading and writing from a database, processing data, and more.

## Role of the Database
A database stores all the data necessary for running the website or application. It can be queried by the application server to retrieve or store data.

## Server-Client Communication
Servers communicate with client computers using various protocols. For web servers, this is typically HTTP (Hypertext Transfer Protocol) or HTTPS (HTTP Secure) if encryption is needed.
