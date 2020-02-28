 #importing the requests library 
import requests 
import logging
import threading
import time

def enviar_requets():
      URL = "http://apps.disfarma.com.co:2083/logistica/crud"
      location = "delhi technological university"
      PARAMS = {'address':location} 
      r = requests.get(url = URL) 
      data = r.headers
      print(data) 


#for i in range(200):
      #enviar_requets()


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(7000):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=enviar_requets)
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

