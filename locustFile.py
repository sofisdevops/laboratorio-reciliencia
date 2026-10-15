from locust import HttpUser, task, between

class Navegador(HttpUser):
    wait_time = between(1, 2)

    @task(4)
    def index(self):
        self.client.get("/navegador")

class Comprador(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def comprar(self):

        self.client.post("/comprador")


