package PrintUsbStream

import (
	"log"

	"go.bug.st/serial"
)

type Listener struct {
	port    string
	timeout int
	mode    serial.Mode
}

func (listener *Listener) checkForPorts() bool {
	ports, err := serial.GetPortsList()
	if err != nil {
		log.Fatal(err)
		return false
	}
	if len(ports) == 0 {
		log.Fatal("No serial ports found!")
		return false
	}
	return true
}

func (listener *Listener) listenOnPort() {
	port, err := serial.Open(listener.port, listener.mode)
	if err != nil {
		log.Fatal(err) //error opening the port
	}

}

func createListener() Listener {

}
