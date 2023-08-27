# 0x09. Web infrastructure design

## Load Balancer
A load balancer is added to a system to distribute network or application traffic across a number of servers. This enhances the responsiveness and availability of applications, websites, databases and other services. 

### Distribution Algorithm
The distribution algorithm configured in a load balancer could be one of several types such as Round Robin, Least Connections, IP Hash, etc. The choice depends on the specific requirements of your application.

- **Round Robin** distributes client requests across all servers sequentially.
- **Least Connections** directs traffic to the server with the fewest active connections.
- **IP Hash** uses the IP address of the client to determine which server receives the request.

### Active-Active vs Active-Passive Setup
In an **Active-Active** setup, traffic is distributed across all available resources simultaneously. All servers are online and available to handle requests.

In an **Active-Passive** setup, there's a primary server handling all traffic (active), while one or more secondary servers are on standby (passive), ready to take over if the primary server fails.

## Database Primary-Replica (Master-Slave) Cluster
In a Primary-Replica (formerly known as Master-Slave) setup, the "Primary" database processes all write operations and optionally, can process read operations. The "Replica" databases are read-only copies of the primary database. They replicate changes from the primary to ensure data consistency across all nodes.

### Primary Node vs Replica Node
The **Primary node** handles all write operations and can also handle read operations. It's responsible for replicating changes to the replica nodes.

The **Replica node** is a read-only participant in the cluster. It replicates data from the primary node to ensure it has the same data. This can be used to distribute read queries across multiple nodes, reducing load on the primary and providing redundancy.

SPOF (Single Point of Failure): These are parts of a system that can cause the entire system to fail if they stop working. SPOFs can be anywhere in a system, including servers, networking hardware, a single piece of software, or a line of code in a script.

Security issues (no firewall, no HTTPS): Without a firewall, your system is open to many security threats including unauthorized access, hacking, and denial-of-service (DoS) attacks. Not using HTTPS can expose data to potential interception or alteration as it travels over the network.

No monitoring: Without monitoring, you won’t be able to identify and address issues promptly. This can lead to increased downtime, loss of productivity, and potential loss of revenue.