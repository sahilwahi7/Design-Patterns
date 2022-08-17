// decorator pattern in go
// What we need , we need 2 abstract classes one for main object second for decorator
// which extends the main object
package main

import "fmt"

type abstarctBeverage interface {
	getDescription() string
	getCost() float32
}

type coffee struct {
}

func (c *coffee) getDescription() string {
	description := "Espresso"
	return description
}

func (c *coffee) getCost() float32 {
	return 20.00
}

type mocha struct {
	coffee abstarctBeverage
}

func (m *mocha) getDescription() string {
	description := m.coffee.getDescription() + "Mocha"
	return description
}
func (m *mocha) getCost() float32 {
	return m.coffee.getCost() + 0.5
}

func main() {
	coffee := &coffee{}
	fmt.Println(coffee.getDescription())
	mocha := &mocha{
		coffee: coffee,
	}
	fmt.Println(mocha.getDescription())
}
