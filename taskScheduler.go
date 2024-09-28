package indian_stock_broker

import (
	"container/heap"
	"fmt"
	"time"
)

/*
Problem statement:
You are given a list of runnables + delay that after t ms run this runnable. How do you store it?

Solution:
 We can store all these in a heap based on delay and pass all the runnables to a channel
*/

type TaskScheduler struct {
	runnable func()
	runTime  time.Time
	index    int
}
type TaskQueue []*TaskScheduler

func (q TaskQueue) Len() int { return len(q) }
func (q TaskQueue) Less(i, j int) bool {
	return q[i].runTime.Before(q[j].runTime)
}
func (q TaskQueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
	q[i].index = i
	q[j].index = j
}
func (q *TaskQueue) Push(x interface{}) {
	n := len(*q)
	item := x.(*TaskScheduler)
	item.index = n
	*q = append(*q, item)
}

func (q *TaskQueue) Pop() interface{} {
	old := *q
	n := len(old)
	item := old[n-1]
	old[n-1] = nil // Avoid memory leak
	item.index = -1
	*q = old[0 : n-1]
	return item
}

type Scheduler struct {
	taskQueue *TaskQueue
	taskChan  chan *TaskScheduler
	stopChan  chan struct{}
}

func NewScheduler() *Scheduler {
	taskQueue := &TaskQueue{}
	heap.Init(taskQueue)
	scheduler := &Scheduler{
		taskQueue: taskQueue,
		taskChan:  make(chan *TaskScheduler),
		stopChan:  make(chan struct{}),
	}

	go scheduler.consume()
	return scheduler
}

func (s *Scheduler) SubmitTask(runnable func(), delay int) {
	runAt := time.Now().Add(time.Duration(delay) * time.Millisecond)
	task := &TaskScheduler{
		runnable: runnable,
		runTime:  runAt,
	}
	s.taskChan <- task
}

func (s *Scheduler) consume() {
	var nextTaskTimer <-chan time.Time
	for {
		var nextTask *TaskScheduler
		if len(*s.taskQueue) > 0 {
			nextTask = (*s.taskQueue)[0]
			delay := time.Until(nextTask.runTime)
			if delay <= 0 {
				heap.Pop(s.taskQueue)
				nextTask.runnable()
				continue
			}
			nextTaskTimer = time.After(delay)
		}

		select {
		case task := <-s.taskChan:
			heap.Push(s.taskQueue, task)
		case <-nextTaskTimer:
			heap.Pop(s.taskQueue)
			nextTask.runnable()
		case <-s.stopChan:
			return
		}

	}
}
func (s *Scheduler) Stop() {
	close(s.stopChan)
}

func main() {
	scheduler := NewScheduler()

	// Example tasks to submit
	scheduler.SubmitTask(func() {
		fmt.Println("Task 1 executed at", time.Now())
	}, 3000) // Execute after 3000ms (3 seconds)

	scheduler.SubmitTask(func() {
		fmt.Println("Task 2 executed at", time.Now())
	}, 1000) // Execute after 1000ms (1 second)

	scheduler.SubmitTask(func() {
		fmt.Println("Task 3 executed at", time.Now())
	}, 2000) // Execute after 2000ms (2 seconds)

	// Let the main goroutine wait for tasks to be executed
	time.Sleep(5 * time.Second)

	// Stop the scheduler if needed
	scheduler.Stop()
}
