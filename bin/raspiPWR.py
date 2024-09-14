#!/usr/bin/env python3

import syslog, sys, signal, os
from gpiozero import Button

btnPWR = Button(23)
btnRBT = Button(24)



def terminate(signalNumber, frame):
  
  syslog.syslog(syslog.LOG_INFO, "SIGTERM/SIGQUIT received. Terminating..")
  syslog.closelog()
  sys.exit(0)


if __name__ == '__main__':

  signal.signal(signal.SIGHUP, signal.SIG_IGN)
  signal.signal(signal.SIGINT, signal.SIG_IGN)
  signal.signal(signal.SIGQUIT, terminate)
  signal.signal(signal.SIGILL, signal.SIG_IGN)
  signal.signal(signal.SIGTRAP, signal.SIG_IGN)
  signal.signal(signal.SIGABRT, signal.SIG_IGN)
  signal.signal(signal.SIGBUS, signal.SIG_IGN)
  signal.signal(signal.SIGFPE, signal.SIG_IGN)
  signal.signal(signal.SIGUSR1, signal.SIG_IGN)
  signal.signal(signal.SIGSEGV, signal.SIG_IGN)
  signal.signal(signal.SIGUSR2, signal.SIG_IGN)
  signal.signal(signal.SIGPIPE, signal.SIG_IGN)
  signal.signal(signal.SIGALRM, signal.SIG_IGN)
  signal.signal(signal.SIGTERM, terminate)

###


while True:

	btnPWR.wait_for_press(0.1)
	if btnPWR.is_pressed:

		syslog.syslog(syslog.LOG_INFO, "Poweroff button pressed. Shutting down..")
		syslog.closelog()
		btnPWR.wait_for_release()
		os.system("/usr/sbin/poweroff")

	btnRBT.wait_for_press(0.1)
	if btnRBT.is_pressed:

		syslog.syslog(syslog.LOG_INFO, "Reboot button pressed. Rebooting..")
		syslog.closelog()
		btnRBT.wait_for_release()
		os.system("/usr/sbin/reboot")


