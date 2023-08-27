# 0x09. Web infrastructure design

## Firewalls
Firewalls are added to a system to provide a layer of security. They monitor and control incoming and outgoing network traffic based on predetermined security rules, acting as a barrier between a trusted network and an untrusted network.

## HTTPS
Traffic is served over HTTPS to encrypt the communication between the server and the client, providing confidentiality and integrity. When data is sent over HTTPS, it is secured via Transport Layer Security protocol (TLS), which provides three key layers of protection: encryption, data integrity, and authentication.

## Monitoring
Monitoring is used to continuously keep track of the status of a system in order to find out when it deviates from normal operation. It helps in early detection of problems so they can be corrected before causing any significant damage.

### Data Collection by Monitoring Tools
Monitoring tools collect data through agents or scripts installed on the servers. These agents collect data about the system's performance, resource usage, and more. This data is then sent back to the monitoring tool for analysis and visualization.

### Monitoring Web Server QPS (Queries Per Second)
If you want to monitor your web server's QPS, you can use monitoring tools that provide this feature. You would need to install their agent on your server, which will then collect and send this data back to the tool. This can help you understand your server's performance and capacity, and can alert you when usage patterns deviate from the norm.

Terminating SSL at the load balancer level: This could potentially expose unencrypted traffic within your internal network. If an attacker gains access to your network, they could eavesdrop on the internal traffic. It’s generally recommended to use end-to-end encryption, especially for sensitive data.

Having only one MySQL server capable of accepting writes: This creates a single point of failure. If this server goes down, your application will not be able to write data, leading to potential data loss and downtime. It also limits your ability to scale as all write requests are funneled through a single server.

Having servers with all the same components (database, web server and application server): This could lead to resource contention, where each component is competing for the same system resources. It also makes it difficult to scale individual components based on their specific needs. For example, a database might need more memory while a web server might need more CPU resources. It’s generally recommended to separate these components onto different servers or containers to allow for better resource allocation and scaling.