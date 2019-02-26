package main

type stateMachine struct {
	state int
}

func (sM *stateMachine) next(signal string) (int, int) {
	lastState := sM.state
	if lastState == 3 && signal == "ltr" {
		sM.state = 1
	} else if sM.state == 9 {
		return lastState, sM.state
	} else if lastState == 5 && signal == "cfr" {
		sM.state = 3
	} else if lastState == 7 && signal == "dlm" {
		sM.state = 7
	} else if signal == "ltr" || signal == "cfr" || signal == "dlm" {
		sM.state++
	}
	return lastState, sM.state
}
