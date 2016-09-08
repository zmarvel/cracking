
#lang racket

; Recursive, unmemoized solution
(define (ways-to-ascend n)
  (cond
    [(zero? n) 0]
    [(= n 1) 1]
    [(= n 2) 2]
    [(= n 3) 4]
    [else (+ (ways-to-ascend (- n 1))
             (ways-to-ascend (- n 2))
             (ways-to-ascend (- n 3)))]))
