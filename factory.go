package main

import "fmt"

type iPublication interface {
	setName(name string)
	setPublisher(publisher string)
	getname() string
}

type publication struct {
	name      string
	publisher string
}

func (p *publication) setName(name string) {
	p.name = name
}

func (p *publication) setPublisher(publisher string) {
	p.publisher = publisher
}

func (p *publication) getname() string {
	return p.name
}

type newspaper struct {
	publication
}

func createNewspaper(name string, pub string) iPublication {
	return &newspaper{
		publication: publication{
			name:      name,
			publisher: pub,
		},
	}
}

type magazine struct {
	publication
}

func createMagazine(name string, pub string) iPublication {
	return &magazine{
		publication: publication{
			name:      name,
			publisher: pub,
		},
	}
}
func newPublication(pubtype string, name string, pub string) (iPublication, error) {
	if pubtype == "magazine" {
		return createMagazine(name, pub), nil
	}
	if pubtype == "newspaper" {
		return createNewspaper(name, pub), nil
	}
	return nil, fmt.Errorf("No such type")
}

func main() {
	mg1, err1 := newPublication("magazine", "Howt o design in go", "Sahil wahi")
	mg2, err2 := newPublication("magazine", "Factory in go", "Sahil wahi")

	if err1 != nil {
		fmt.Println("Error in crreation og magazine")
	} else {
		pubDetails(mg1)

	}
	if err2 != nil {
		fmt.Println("Error in crreation og magazine")
	} else {
		pubDetails(mg2)

	}
}

func pubDetails(pub iPublication) {
	fmt.Println(pub.getname())
}
