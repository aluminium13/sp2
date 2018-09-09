package main

// Key contains Keys of Record
type Key struct {
	dsearch string
	esearch uint
}

// FunctionField fuctional part of Record
type FunctionField struct {
	f Enum
}

// Record struct as an element of a Table
type Record struct {
	key Key
	fnc FunctionField
}

// newRecord template to create a new Record
func newRecord(dsearch string, esearch uint, funcF Enum) *Record {
	return &Record{key: Key{dsearch, esearch}, fnc: FunctionField{funcF}}
}

// emptyRecord template to create a new empty Record
func emptyRecord() *Record {
	return &Record{}
}

// isEmpty check if a Record is empty
func (r *Record) isEmpty() bool {
	if r.key.dsearch == "" {
		return true
	}
	return false
}
