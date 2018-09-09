package main

import (
	"sort"
	"strings"
)

// cmpKeys compare two keys
func cmpKeys(k1 Key, k2 Key) uint {
	if cmp := strings.Compare(k1.dsearch, k2.dsearch); cmp != 0 {
		return uint(cmp)
	}
	return k1.esearch - k2.esearch
}

// By is a type of a "less" function that defines the ordering of its Record arguments
type By func(r1, r2 *Record) bool

// recordsSorter is a struct that implements sort.Interface
type recordsSorter struct {
	records []*Record
	by      func(r1, r2 *Record) bool
}

// Sort is a method on the function type, By, that sorts the argument slice according to the function
func (by By) Sort(t *Table) {
	rs := &recordsSorter{
		records: t.records,
		by:      by,
	}
	sort.Sort(rs)
}

// Len is part of sort.Interface, so must be implemented
func (s *recordsSorter) Len() int {
	return len(s.records)
}

// Swap is also a part of sort interface
func (s *recordsSorter) Swap(i, j int) {
	s.records[i], s.records[j] = s.records[j], s.records[i]
}

// Less is also a part of sort interface
func (s *recordsSorter) Less(i, j int) bool {
	return s.by(s.records[i], s.records[j])
}

// cmpStr is a function to compare strings by rule from 1.3 table
func cmpStr(a, b string) int {
	CyrAndLat := "othpmabxkyeотнрмавхкуе"
	count := 0
	bl := strings.ToLower(b)
	for _, char := range strings.ToLower(a) {
		count += strings.Count(bl, string(char))
		if strings.ContainsAny(CyrAndLat, string(char)) {
			count += strings.Count(bl, pairs[string(char)])
		}
	}
	return count
}
