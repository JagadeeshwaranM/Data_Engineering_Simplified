
Messaging is a key data integration strategy employed in many distributed environments such as the cloud. 

Messaging supports asynchronous operations, enabling you to decouple a process that consumes a service from the process that implements the service.

![image](https://user-images.githubusercontent.com/42135673/232835267-9521697a-55eb-4f0f-a101-4c45095313d5.png)

Messaging connects multiple applications in an exchange of data.

Messaging uses an encapsulated asynchronous approach to exchange data through a network.

A traditional messaging system has two models of abstraction:

    Queue – a message channel where a single message is received exactly by one consumer in a point-to-point message-queue pattern. 
            If there are no consumers available, the message is retained until a consumer processes the message.

    Topic -  a message feed that implements the publish-subscribe pattern and broadcasts messages to consumers that subscribe to that topic.
    
Messaging Models:

  1. Point to Point 
  2. Publish and Subscribe
 
 ![image](https://user-images.githubusercontent.com/42135673/232836338-409f9e17-9865-47e2-a67f-e9818d9c2e55.png)

Kafka is an example of publish-and-subscribe messaging model




