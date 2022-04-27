from app.worker import worker

worker = worker()

def run():
    print("eu sou o run e %s" % worker)