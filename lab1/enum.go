package main

// implementation of Enum type

type Enum interface {
	name() string
	ordinal() int
	values() *[]string
}

type dayType uint

var dayTypeStrings = []string{
	"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
}

const (
	Mon = iota
	Tue
	Wed
	Thu
	Fri
	Sat
	Sun
)

func (gt dayType) name() string {
	return dayTypeStrings[gt]
}

func (gt dayType) ordinal() int {
	return int(gt)
}

func (gt dayType) values() *[]string {
	return &dayTypeStrings
}
