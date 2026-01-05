(define (over-or-under num1 num2) 
  (if (< num1 num2) -1 (if (= num1 num2) 0 1) )
) 
;ok

(define (make-adder num) 
  ;(lambda (inc) (+ num inc))
  (define (add-sum inc) 
    (+ num inc))
  add-sum
  
)
;ok

(define (composed f g) 
  (lambda (x) (f (g x)))
) 
;ok

(define (repeat f n) 'YOUR-CODE-HERE
  (if (= n 1)
      f 
      (lambda (x) (f ((repeat f (- n 1)) x))))
) ;writen by AI, I guess I should be completed by recursion


(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 'YOUR-CODE-HERE
  (if (zero? (modulo (max a b) (min a b))) 
    (min a b)
    ((lambda (a b) (gcd (min a b) (modulo (max a b) (min a b)))) a b)
  ) 
)
