import Pyro4
import time

@Pyro4.expose
class ShippingServer:
    def process_shipping(self, sender, receiver, item):
        print(f"Processing shipping: {sender} -> {receiver} ({item})")
        # time.sleep(3)  # Simulasi proses pengiriman barang
        print(f"Shipping completed: {item} has been delivered from {sender} to {receiver}")

daemon = Pyro4.Daemon()
uri = daemon.register(ShippingServer)

print("Ready. Object URI =", uri)
daemon.requestLoop()
