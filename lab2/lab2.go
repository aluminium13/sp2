package main

import "fmt"

func main() {
	fmt.Println("Лабораторна робота №2")
	fmt.Println("Симуляція роботи автомату")
	stm := stateMachine{1}
	for stm.state != 10 {
		fmt.Print("Enter signal: ")
		var signal string
		fmt.Scanln(&signal)
		before, after := stm.next(signal)
		fmt.Printf(">> S(%d) -[%s]-> S(%d) \n", before, signal, after)
	}
}
