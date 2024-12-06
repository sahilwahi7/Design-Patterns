package main

import (
	"fmt"
	"sync"
)

type Task struct {
	ID           int
	Prerequisites []int
	Runnable     func() error
}

type Job struct {
	ID    int
	Tasks map[int]*Task
}

type Scheduler struct {
	jobs        []*Job
	taskQueue   chan *Task
	inDegree    map[int]int
	taskGraph   map[int][]*Task
	taskStatus  map[int]string
	mu          sync.Mutex
	wg          sync.WaitGroup
}

func NewScheduler() *Scheduler {
	return &Scheduler{
		taskQueue:  make(chan *Task, 100),
		inDegree:   make(map[int]int),
		taskGraph:  make(map[int][]*Task),
		taskStatus: make(map[int]string),
	}
}

func (s *Scheduler) AddJob(job *Job) {
	s.jobs = append(s.jobs, job)
}

func (s *Scheduler) BuildDependencyGraph(job *Job) {
	for _, task := range job.Tasks {
		if _, exists := s.inDegree[task.ID]; !exists {
			s.inDegree[task.ID] = 0
		}
		for _, prereq := range task.Prerequisites {
			s.taskGraph[prereq] = append(s.taskGraph[prereq], task)
			s.inDegree[task.ID]++
		}
	}
}

func (s *Scheduler) StartWorkerPool(numWorkers int) {
	for i := 0; i < numWorkers; i++ {
		go s.worker()
	}
}

func (s *Scheduler) worker() {
	for task := range s.taskQueue {
		// Run the task
		err := task.Runnable()
		s.mu.Lock()
		if err != nil {
			fmt.Printf("Task %d failed\n", task.ID)
			s.taskStatus[task.ID] = "Failed"
		} else {
			fmt.Printf("Task %d completed\n", task.ID)
			s.taskStatus[task.ID] = "Completed"
			// Enqueue dependent tasks
			for _, dep := range s.taskGraph[task.ID] {
				s.inDegree[dep.ID]--
				if s.inDegree[dep.ID] == 0 {
					s.wg.Add(1)
					s.taskQueue <- dep
				}
			}
		}
		s.mu.Unlock()
		s.wg.Done()
	}
}

func (s *Scheduler) Execute() {
	for _, job := range s.jobs {
		// Build dependency graph for the job
		s.BuildDependencyGraph(job)

		// Add tasks with no prerequisites to the queue
		for _, task := range job.Tasks {
			if s.inDegree[task.ID] == 0 {
				s.wg.Add(1)
				s.taskQueue <- task
			}
		}
	}
	s.wg.Wait()
	close(s.taskQueue)
}

func main() {
	scheduler := NewScheduler()

	job := &Job{
		ID: 1,
		Tasks: map[int]*Task{
			1: {ID: 1, Prerequisites: []int{}, Runnable: func() error {
				fmt.Println("Task 1 running")
				return nil
			}},
			2: {ID: 2, Prerequisites: []int{1}, Runnable: func() error {
				fmt.Println("Task 2 running")
				return nil
			}},
			3: {ID: 3, Prerequisites: []int{1}, Runnable: func() error {
				fmt.Println("Task 3 running")
				return nil
			}},
			4: {ID: 4, Prerequisites: []int{1,2}, Runnable: func() error {
				fmt.Println("Task 4 running")
				return nil
			}},
			5: {ID: 5, Prerequisites: []int{3}, Runnable: func() error {
				fmt.Println("Task 5 running")
				return nil
			}},

		},
	}

	scheduler.AddJob(job)
	scheduler.StartWorkerPool(4)
	scheduler.Execute()
}
