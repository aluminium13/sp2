package main

import "fmt"

func main() {
	var ds dayType = Mon
	t := &Table{records: []*Record{
		newRecord("Manicure", 400, ds),
		emptyRecord(),
		emptyRecord(),
		newRecord("Pedicure", 550, ds),
		newRecord("Shugaring", 890, ds),
		emptyRecord(),
		newRecord("Peeling", 1200, ds),
		emptyRecord(),
		newRecord("Massage", 1200, ds),
		emptyRecord(),
	}}

	fmt.Println("Лабораторна робота №1")
	t.output()
	fmt.Println()

	fmt.Println("--Робота з таблицею за допомогою бінарного пошуку--")
	fmt.Println(t.selBin(Key{"Manicure", 400}))

	fmt.Println()
	fmt.Println("--Робота з таблицею за індексом--")
	fmt.Println("Пошук за неіснуючим індексом")
	fmt.Println(t.selNmb(666))
	//Додавання нового елемента за індексом
	t.insNmb(15, newRecord("Mesotherapy", 2100, ds))
	fmt.Println("Пошук за існуючим індексом")
	fmt.Println(t.selNmb(15))
	fmt.Println("Видалення за існуючим індексом")
	t.delNmb(15)
	fmt.Println(t.selNmb(15))
	fmt.Println("Оновлення за існуючим індексом")
	t.updNmb(12, newRecord("Mesotherapy", 2100, ds))
	fmt.Println(t.selNmb(12))
	fmt.Println("Оновлення за неіснуючим індексом")
	t.updNmb(71, newRecord("Mesotherapy", 2100, ds))
	fmt.Println()

	fmt.Println("--Робота з таблицею за допомогою лінійного пошуку--")
	fmt.Println("Пошук за існуючим ключем")
	fmt.Println(t.selLin(Key{"Peeling", 1200}))
	fmt.Println("Пошук за неіснуючим ключем")
	fmt.Println(t.selLin(Key{"Spa", 4700}))
	fmt.Println()

	fmt.Println("--Робота з використанням міри схожості--")
	fmt.Println(*t.sortByStr("Ma")[0])
	fmt.Println(cmpStr("lalAlaррр", "adap"))
}
