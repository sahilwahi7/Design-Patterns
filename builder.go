package controller

import "fmt"

type House struct {
	windowType string
	doorType   string
	floor      int
}

type Ibuilder interface {
	setDoorType()
	setWindowType()
	setNumFloor()
	getHouse() House
}

func getBuilder(builder string) Ibuilder {
	if builder == "igloo" {
		return newIglooBuilder()
	}
	return newNormalBuilder()
}

type NormalBuilder struct {
	windowType string
	doorType   string
	floor      int
}

func newNormalBuilder() *NormalBuilder {
	return &NormalBuilder{}
}

func (b *NormalBuilder) setWindowType() {
	b.windowType = "window"
}

func (b *NormalBuilder) setDoorType() {
	b.doorType = "door"
}
func (b *NormalBuilder) setNumFloor() {
	b.floor = 1
}

func (b *NormalBuilder) getHouse() House {
	return House{
		windowType: b.windowType,
		doorType:   b.doorType,
		floor:      b.floor,
	}
}

type IglooBuilder struct {
	windowType string
	doorType   string
	floor      int
}

func newIglooBuilder() *IglooBuilder {
	return &IglooBuilder{}
}

func (b *IglooBuilder) setWindowType() {
	b.windowType = "window"
}

func (b *IglooBuilder) setDoorType() {
	b.doorType = "door"
}
func (b *IglooBuilder) setNumFloor() {
	b.floor = 1
}

func (b *IglooBuilder) getHouse() House {
	return House{
		windowType: b.windowType,
		doorType:   b.doorType,
		floor:      b.floor,
	}
}

type Director struct {
	builder Ibuilder
}

func newDirector(b Ibuilder) *Director {
	return &Director{
		builder: b,
	}
}
func (d *Director) setBuilder(b Ibuilder) {
	d.builder = b
}
func (d *Director) buildHouse() House {
	d.builder.setDoorType()
	d.builder.setWindowType()
	d.builder.setNumFloor()
	return d.builder.getHouse()
}

func main() {
	normalBuilder := getBuilder("normal")
	iglooBuilder := getBuilder("igloo")

	director := newDirector(normalBuilder)
	normalHouse := director.buildHouse()

	fmt.Printf("Normal House Door Type: %s\n", normalHouse.doorType)
	fmt.Printf("Normal House Window Type: %s\n", normalHouse.windowType)
	fmt.Printf("Normal House Num Floor: %d\n", normalHouse.floor)

	director.setBuilder(iglooBuilder)
	iglooHouse := director.buildHouse()

	fmt.Printf("\nIgloo House Door Type: %s\n", iglooHouse.doorType)
	fmt.Printf("Igloo House Window Type: %s\n", iglooHouse.windowType)
	fmt.Printf("Igloo House Num Floor: %d\n", iglooHouse.floor)

}
