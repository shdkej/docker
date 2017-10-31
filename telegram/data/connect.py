from gevent.server import StreamServer
from gevent.queue import Queue
import logging

tasks = Queue()

def handle(socket, address):

	logging.debug('%s: received' % (address[0]))
	f = socket.makefile('r')
	task = tasks.get()
	logging.debug('%s' %(task))
	for l in f:
		msg = l.strip()
		socket.sendall(l)
		logging.debug('msg: %s' %(msg))
	name = f.readline().strip()
	while True:
		line = f.readline()
		logging.debug('%s'%(line))
		if not line:
			print("not line")
		st = line.strip().lower()
		logginn.debug('%s'%(st))
	socket.close()
	

if __name__ == '__main__':

	server = StreamServer(('59.27.177.110',7777), handle)
	logging.getLogger().setLevel(logging.DEBUG)
	logging.info("START SERVER")
	server.serve_forever()
	
	
