package main

import (
	"fmt"
	"log"
)

// Table struct  of a Table
type Table struct {
	records []*Record
}

// Len returns number of records in a Table
func (t *Table) Len() int {
	return len(t.records)

}

func (t *Table) output() {
	fmt.Println("Table:")
	for _, elem := range t.records {
		fmt.Printf("\t%s", elem.tostring())
	}
}

func (r *Record) tostring() string {
	return fmt.Sprintf("Record ( key: %s, mod: %d, functional: %d)\n", r.key.dsearch, r.key.esearch, r.fnc.f)
}

// selNmb select Record by index
func (t *Table) selNmb(n int) *Record {
	if t.Len() <= n {
		log.Println("Упс! Нема цього")
		return emptyRecord()
	}
	return t.records[n]
}

// insNmb insert Record by index
func (t *Table) insNmb(n int, r *Record) {
	if n >= t.Len() {
		limit := n - t.Len()
		for i := 0; i <= limit; i++ {
			t.records = append(t.records, emptyRecord())
		}
	}
	t.records[n] = r
}

// delNmb delete Record by index
func (t *Table) delNmb(n int) {
	if t.Len() <= n {
		log.Println("Упс! Цього елемента і так тут не було")
	} else {
		t.records[n].key.dsearch = ""
		t.records[n].key.esearch = 0
		t.records[n].fnc.f = nil
	}

}

// updNmb update Record by index
func (t *Table) updNmb(n int, r *Record) {
	if n >= t.Len() {
		log.Println("Помилка! Індекс поза межами таблиці")
	} else {
		t.records[n] = r
	}
}

// selLin select Record by key (choose the first match)
func (t *Table) selLin(key Key) *Record {
	for _, rec := range t.records {
		if cmpKeys(key, rec.key) == 0 {
			return rec
		}
	}
	log.Println("Упс! Нема цього")
	return emptyRecord()
}

// insLin insert Record to a first empty place (or append)
func (t *Table) insLin(r *Record) {
	for i, record := range t.records {
		if record.key.dsearch == "" {
			t.records[i] = r
			return
		}
	}
	t.records = append(t.records, r)
}

// delLin delete Record by key (choose the first match)
func (t *Table) delLin(key Key) {
	r := t.selLin(key)
	r.key.dsearch = ""
	r.key.esearch = 0
	r.fnc.f = nil
}

// updLin update Record by key (choose the first match)
func (t *Table) updLin(key Key, r *Record) {
	res := t.selLin(key)
	if !res.isEmpty() {
		res.key = r.key
		res.fnc = r.fnc
	} else {
		log.Println("Помилка! Запис не найдено!")
	}
}

// selBin select Record by key (choose the first match)
func (t *Table) selBin(key Key) *Record {
	low := 0
	high := t.Len()
	t.sortByStr(key.dsearch)
	for low < high {
		mid := (low + high) / 2
		cmp := cmpKeys(t.records[mid].key, key)
		if cmp == 0 {
			return t.records[mid]
		} else if cmp < 0 {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return emptyRecord()
}

// insBin insert Record to a first empty place (or append)
func (t *Table) insBin(r *Record) {
	res := t.selBin(r.key)
	if res.isEmpty() {
		t.records = append(t.records, r)
	}
}

// delBin delete Record by key (choose the first match)
func (t *Table) delBin(key Key) {
	r := t.selBin(key)
	r.key.dsearch = ""
	r.key.esearch = 0
	r.fnc.f = nil
}

// updBin update Record by key (choose the first match)
func (t *Table) updBin(r *Record, key Key) {
	res := t.selBin(key)
	if !res.isEmpty() {
		res.key = r.key
		res.fnc = r.fnc
	} else {
		log.Println("Помилка! Запис не найдено!")
	}
}

// sortByStr sort Table by dsearch Key by alphabeth
func (t *Table) sortByStr(str string) []*Record {
	By(func(r1, r2 *Record) bool {
		return cmpStr(str, r1.key.dsearch) > cmpStr(str, r2.key.dsearch)
	}).Sort(t)
	return t.records
}
