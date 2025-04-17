(defun sum-even-odd (n)
  (let ((even-sum 0)
        (odd-sum 0))
    (loop for i from 1 to n do
      (if (evenp i)
          (setf even-sum (+ even-sum i))
          (setf odd-sum (+ odd-sum i))))
    (format t "Sum of even numbers from 1 to ~A: ~A~%" n even-sum)
    (format t "Sum of odd numbers from 1 to ~A: ~A~%" n odd-sum)))

(defun main ()
  (format t "Enter a number: ")
  (let ((num (read)))
    (sum-even-odd num)))

(main)
