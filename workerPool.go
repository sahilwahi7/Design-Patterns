package main

import (
    "fmt"
    "sync"
)

type Job struct {
    Number int
}

type Result struct {
    Number int
    Square int
}

var (
    jobs    chan Job
    results chan Result
    wg      sync.WaitGroup
)

func worker(id int) {
    for job := range jobs {
        fmt.Printf("Worker %d processing job for number %d\n", id, job.Number)
        square := job.Number * job.Number
        result := Result{Number: job.Number, Square: square}
        results <- result
    }
    wg.Done()
}

func startWorkerPool(numWorkers int) {
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go worker(i)
    }
}

func submitJobs(numbers []int) {
    for _, number := range numbers {
        jobs <- Job{Number: number}
    }
    close(jobs)
}

func collectResults(numResults int) {
    for i := 0; i < numResults; i++ {
        result := <-results
        fmt.Printf("Result: Number %d, Square %d\n", result.Number, result.Square)
    }
}

func main() {
    numWorkers := 3
    jobs = make(chan Job, 10)
    results = make(chan Result, 10)

    numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    startWorkerPool(numWorkers)

    submitJobs(numbers)

    go collectResults(len(numbers))

    wg.Wait()
    close(results)
}
