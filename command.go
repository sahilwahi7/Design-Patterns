//commad pattern in go

package main

import "fmt"

type command interface {
	execute()
}

type Device interface {
	on()
	off()
}

type Light struct {
	isRunning bool
}

func (l *Light) on() { // the light object passed to the  to define the on function
	l.isRunning = true
	fmt.Println("Light is on")

}

func (l *Light) off() { // the light object passed to the  to define the on function
	l.isRunning = false
	fmt.Println("Light is off")

}

type OnCommand struct { // we will pass light object to the oncommand
	device Device
}

func (c *OnCommand) execute() {
	c.device.on()
}

type OffCommand struct {
	device Device
}

func (c *OffCommand) execute() {
	c.device.off()
}

type Button struct {
	command command
}

func (b *Button) press() {
	b.command.execute()
}

func main() {
	light := &Light{}

	onCommand := &OnCommand{
		device: light,
	}

	offCommand := &OffCommand{
		device: light,
	}

	onButton := &Button{
		command: onCommand,
	}
	onButton.press()

	offButton := &Button{
		command: offCommand,
	}
	offButton.press()
}
