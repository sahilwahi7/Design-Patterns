// chain of responsibilities pattern in go
package main

import (
	"fmt"
)

// designing the logger application in golang using chain of responsibilities pattern
type handler interface {
	setNext(handler)
	execute(request string)
}

type DebugLogger struct {
	next handler
}
//defining execute method of debug logger
func (d *DebugLogger) execute(request string) {
	if request == "Debug" {
		fmt.Println("This is debug log")
		d.next.execute(request)
		return
	}
	d.next.execute(request)

}
func (d *DebugLogger) setNext(next handler) {
	d.next = next
}

type ErrorLogger struct {
	next handler
}
//defining execute method of error logger
func (e *ErrorLogger) execute(request string) {
	if request == "Error" {
		fmt.Println("This is error log")
		e.next.execute(request)
		return
	}
	e.next.execute(request)

}

func (e *ErrorLogger) setNext(next handler) {
	e.next = next
}

func main() {
	errorLogger := &ErrorLogger{}
	debugLogger := &DebugLogger{}
	errorLogger.setNext(debugLogger)
	errorLogger.execute("Debug")
	

}
