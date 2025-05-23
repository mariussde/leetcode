
### 🔹 **"Tell me about a time you made a mistake."**

**Leadership Principle:** *Earn Trust, Learn and Be Curious*

**Situation:** Early in my migration work at Sopra Steria, I forgot to update a config file that pointed to the new API endpoint.
**Task:** This caused QA to report broken functionality that I initially thought was a backend issue.
**Action:** Once I realized it was my oversight, I immediately informed the team, fixed the config, and added a checklist item for future environment setups.
**Result:** The team appreciated my honesty and the process change helped avoid similar issues later.


### 🔹 **"Tell me about a time you influenced a decision without authority."**

**Leadership Principle:** *Have Backbone; Disagree and Commit*

**Situation:** A senior dev proposed reusing an old monolithic API pattern in the new system.
**Task:** I believed a microservice structure was better for scalability and clarity.
**Action:** I prepared a quick prototype, showed how it improved code separation and performance, and respectfully explained my viewpoint.
**Result:** The team agreed, and we adopted microservices for all new modules.


### 🔹 **"Tell me about a time you improved a process."**

**Leadership Principle:** *Invent and Simplify*

**Situation:** Our deployment process involved 4+ manual steps and frequent human errors.
**Task:** I wanted to make it safer and faster.
**Action:** I created simple deployment scripts, documented everything clearly, and worked with DevOps to add automated checks.
**Result:** Deployments became 2× faster and error-free. Other teams started using our approach.


---


### 1. **Singleton Pattern**

Ensure only one instance of LoadBalancer exists.

```python
class LoadBalancer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.servers = []
            cls._instance.strategy = None
        return cls._instance

    def add_server(self, server):
        self.servers.append(server)

    def get_server(self, request):
        return self.strategy.get_server(self.servers, request)

    def set_strategy(self, strategy):
        self.strategy = strategy
```

---

### 2. **Strategy Pattern**

Encapsulate interchangeable load balancing algorithms.

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def get_server(self, servers, request):
        pass

class RoundRobinStrategy(Strategy):
    def __init__(self):
        self.index = 0

    def get_server(self, servers, request):
        if not servers:
            raise Exception("No servers available")
        server = servers[self.index % len(servers)]
        self.index += 1
        return server

class LeastConnectionsStrategy(Strategy):
    def get_server(self, servers, request):
        healthy_servers = [s for s in servers if s.healthy]
        return min(healthy_servers, key=lambda s: s.connections, default=None)
```

---

### 3. **Observer Pattern** *(simplified server health check)*

```python
class ServerObserver:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, server):
        self.subscribers.append(server)

    def notify_health_change(self, server, status):
        server.healthy = status
```

---

### 4. **Proxy Pattern** *(request forwarding)*

```python
class ServerProxy:
    def __init__(self, server):
        self.server = server

    def handle_request(self, request):
        if self.server.healthy:
            return f"Request handled by {self.server.name}"
        return "Server unavailable"
```

---

### 5. **Decorator Pattern** *(adding logging to server request handling)*

```python
class Server:
    def __init__(self, name):
        self.name = name
        self.healthy = True
        self.connections = 0

    def handle(self, request):
        self.connections += 1
        return f"{self.name} handled request"

class LoggingServerDecorator:
    def __init__(self, server):
        self.server = server

    def handle(self, request):
        print(f"Logging: {self.server.name} received a request")
        return self.server.handle(request)
```

---

### ✅ **Example Usage**

```python
# Setup
s1 = Server("s1")
s2 = Server("s2")
lb = LoadBalancer()
lb.add_server(s1)
lb.add_server(s2)
lb.set_strategy(RoundRobinStrategy())

# Use decorator
logged_s1 = LoggingServerDecorator(s1)
print(logged_s1.handle("req1"))

# Use load balancer
server = lb.get_server("req2")
print(server.handle("req2"))
```

