package main

type parser interface {
	parseData() string
	setData()
}

type JsonParser struct {
	date string
}

func NewJsonParser() *JsonParser {
	return &JsonParser{}
}

func (p *JsonParser) parseData() string {
	return p.date
}

func (p *JsonParser) setData() {
	p.date = "date"
}

type XMLparser struct {
	date string
}

func NewXMLparser() *XMLparser {
	return &XMLparser{}
}

func (p *XMLparser) parseXML() string {
	return p.date
}

func (p *XMLparser) setData() {
	p.date = "date1"
}

type XMLAdaptor struct {
	parser *XMLparser
}

func NewXMLAdaptor() *XMLAdaptor {
	return &XMLAdaptor{}
}

func (a *XMLAdaptor) parseData() string {
	return a.parser.parseXML()
}

func (a *XMLAdaptor) setData() {
	a.parser.setData()
}
