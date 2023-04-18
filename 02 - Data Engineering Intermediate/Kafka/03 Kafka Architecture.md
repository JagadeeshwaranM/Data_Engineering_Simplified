![image](https://user-images.githubusercontent.com/42135673/232838913-e37e4947-3ce5-4b62-bda1-6ce02a2f672e.png)


Kafka maintains data feeds of messages in categories called topics.

Messages are published to topics in Kafka by processes called producers.

Messages are consumed from topics in Kafka by consuming processes called subscribers.

Kafka is run in a distributed environment cluster comprising of one or more servers each of which is called a broker.

Kafka generalizes (combines) the traditional messaging model of queuing (with a queue) and publish-subscribe (with a topic) 
using a single consumer abstraction called – a consumer group.

Kafka message delivery is based on subscriber group name or identity.

Two or more separate consumer subscriber instances that need to get messages at least once from Kafka will subscribe to Kafka based on
using different consumer group name or identification. All messages will be broadcast to all consumers in a publish-subscribe pattern.

If two or more consumer subscriber instances use the same consumer group name, then messages are load-balanced (evenly divided) across all instances 
of consumers with the same consumer group name and works like the traditional queue model.
