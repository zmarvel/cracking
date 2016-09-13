

#lang racket

(define empty-stack list)
(define (stack-min stk)
  (match stk
    [`((,value . ,info) . ,rest) info]
    [_ +inf.0]))
(define (stack-push stk value)
  (let ([smallest (min value (stack-min stk))])
    (cons `(,value . ,smallest) stk)))
(define (stack-pop stk)
  (match stk
    [`((,value . ,info) . ,rest) (values value rest)]
    [_ (values null stk)]))

(let ([items '(10 9 8 7 8 9 8 7 6 5 6 1)])
  (let ([stk (foldl (lambda (i acc)
                      (let ([stk^ (stack-push acc i)])
                        (display (format "pushed ~a; current min: ~a" i (stack-min stk^))) (newline)
                        stk^))
                    (empty-stack)
                    items)])
    (foldl (lambda (i acc)
             (let-values ([(popped stk^) (stack-pop acc)])
               (display (format "popped ~a; current min: ~a" popped (stack-min stk^))) (newline)
               stk^))
           stk
           items)))
