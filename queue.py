import threading
import time

class SimpleQueue:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            if not self.is_empty():
                return self.items.pop(0)
            else:
                raise queue.Empty

    def get_nowait(self):
        return self.get()

    def is_empty(self):
        with self.lock:
            return len(self.items) == 0

    def qsize(self):
        with self.lock:
            return len(self.items)

class Topic:
    def __init__(self):
        self.subscribers = {}
        self.messages = SimpleQueue()
        self.new_message_event = threading.Event()
        self.subscribers_lock = threading.Lock()

    def publish(self, message, publisher_name):
        self.messages.put((message, publisher_name))
        self.new_message_event.set()

    def subscribe(self, subscriber):
        with self.subscribers_lock:
            self.subscribers[subscriber.name] = subscriber

    def unsubscribe(self, subscriber):
        with self.subscribers_lock:
            if subscriber.name in self.subscribers:
                del self.subscribers[subscriber.name]

class Subscriber(threading.Thread):
    def __init__(self, name, topic):
        super().__init__()
        self.name = name
        self.topic = topic
        self.last_message_index = -1

    def run(self):
        while True:
            # Wait for the event with a timeout to avoid indefinite blocking
            self.topic.new_message_event.wait(timeout=1)
            
            while self.last_message_index < self.topic.messages.qsize() - 1:
                self.last_message_index += 1
                message, publisher_name = self.topic.messages.items[self.last_message_index]
                print(f"Subscriber {self.name} received message from {publisher_name}: {message}")
            
            # Reset the event
            if self.last_message_index == self.topic.messages.qsize() - 1:
                self.topic.new_message_event.clear()

class PubSubSystem:
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = Topic()

    def publish(self, topic_name, message, publisher_name):
        if topic_name in self.topics:
            self.topics[topic_name].publish(message, publisher_name)
        else:
            print("Topic does not exist")

    def subscribe(self, topic_name, subscriber_name):
        if topic_name in self.topics:
            subscriber = Subscriber(subscriber_name, self.topics[topic_name])
            self.topics[topic_name].subscribe(subscriber)
            subscriber.start()
        else:
            print("Topic does not exist")

# Example usage
pub_sub_system = PubSubSystem()

pub_sub_system.create_topic("topic1")
pub_sub_system.create_topic("topic2")

pub_sub_system.publish("topic1", "Message 1", "Publisher A")
pub_sub_system.publish("topic1", "Message 2", "Publisher B")

pub_sub_system.subscribe("topic1", "Subscriber X")
pub_sub_system.subscribe("topic1", "Subscriber Y")

pub_sub_system.publish("topic1", "Message 3", "Publisher C")

pub_sub_system.publish("topic2", "Message 5", "Publisher C")
pub_sub_system.publish("topic2", "Message 6", "Publisher D")

pub_sub_system.subscribe("topic2", "Subscriber L")
pub_sub_system.subscribe("topic2", "Subscriber M")

pub_sub_system.publish("topic2", "Message 7", "Publisher C")
pub_sub_system.publish("topic2", "Message 8", "Publisher D")
pub_sub_system.publish("topic2", "Message 9", "Publisher E")

# Allow some time for subscribers to process messages
time.sleep(5)
