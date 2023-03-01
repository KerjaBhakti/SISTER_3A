import threading
import time

class ComputerGuard(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.event = event

    def run(self):
        while True:
            print("Penjaga Komputer: Menunggu aktivitas terdeteksi...")
            self.event.wait()
            print("Penjaga Komputer: Aktivitas terdeteksi!")
            self.event.clear()

class UserActivityDetector(threading.Thread):
    def __init__(self, event, idle_time):
        threading.Thread.__init__(self)
        self.event = event
        self.idle_time = idle_time

    def run(self):
        while True:
            time.sleep(self.idle_time)
            print("Pengguna: Tidak melakukan apapun...")
            self.event.set()

def main():
    idle_time = 5
    event = threading.Event()
    guard = ComputerGuard(event)
    user_detector = UserActivityDetector(event, idle_time)

    guard.start()
    user_detector.start()

    guard.join()
    user_detector.join()

if __name__ == "__main__":
    main()