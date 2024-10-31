package controller

import (
	"fmt"
	"time"
)

type LimitingStrategy interface {
	Limit() bool
}

type TokenBucket struct {
	bucketSize     int64
	refillTime     time.Duration
	LastRefillTime time.Time
	tokenCount     int64
}

func NewTokenBucket(bucketSize int64, refillTime time.Duration) *TokenBucket {
	return &TokenBucket{
		bucketSize:     bucketSize,
		refillTime:     refillTime,
		LastRefillTime: time.Now(),
	}
}
func (t *TokenBucket) Limit() bool {
	now := time.Now()
	elaspsedTime := now.Sub(t.LastRefillTime)
	t.tokenCount += int64(elaspsedTime / t.refillTime)
	if t.tokenCount >= t.bucketSize {
		t.tokenCount = t.bucketSize
	}
	t.LastRefillTime = time.Now()
	if t.tokenCount > 0 {
		t.tokenCount -= 1
		return true
	}
	return false
}

type LeakyBucket struct {
	capacity int
	queue    int
	lastLeak time.Time
	leakRate time.Duration
}

func NewLeakyBucket(capacity int, leakRate time.Duration) *LeakyBucket {
	return &LeakyBucket{
		capacity: capacity,
		queue:    0,
		lastLeak: time.Now(),
		leakRate: leakRate,
	}
}
func (l *LeakyBucket) Limit() bool {
	now := time.Now()
	elaspsedTime := now.Sub(l.lastLeak)
	leakCount := int(elaspsedTime / l.leakRate)
	l.queue -= leakCount
	if l.queue <= 0 {
		l.queue = 0
	}
	l.lastLeak = now
	if l.queue < l.capacity {
		l.queue += 1
		return true
	}
	return false
}

type RateLimiter struct {
	strategy LimitingStrategy
}

func NewRateLimiter(strategy LimitingStrategy) *RateLimiter {
	return &RateLimiter{
		strategy: strategy,
	}
}

func (l *RateLimiter) Allow() bool {
	return l.strategy.Limit()
}

func main() {
	rateLimiter := NewRateLimiter(
		NewLeakyBucket(5, time.Second))
	for i := 0; i < 10; i++ {
		go func(id int) {
			if rateLimiter.Allow() {
				fmt.Printf("Request %d allowed\n", id)
			} else {
				fmt.Printf("Request %d denied\n", id)
			}
		}(i)
		time.Sleep(200 * time.Millisecond)
	}
	time.Sleep(3 * time.Second)
}
