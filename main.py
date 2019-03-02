from gpio import isReset
from gpio import resetAction
from gpio import gameOverAction
import health
import fire
from time import sleep
from params import *


while True:
	resetAction()
	t_health = health.healthThread(1)
	t_fire = fire.fireThread(2)
	t_health.start()
	t_fire.start()
	while True:
		if not t_health.isAlive():
			gameOverAction()
			while not isReset():
				sleep(0.1)
			break
		if isReset():
			break
		sleep(0.05)
