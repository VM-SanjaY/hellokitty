from locust import HttpUser, task, between
from locust.main import main

class SiteUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(1, 5)

    @task
    def hello(self):
        self.client.get(url="/home/paradise/")

    @task
    def theatre(self):
        self.client.get(url="/home/thertical/")

if __name__ == "__main__":
    import sys
    sys.argv = ["locust", "-f", "locustfile.py", "--web-port", "8888"]  # Change the port number to any available port
    main()