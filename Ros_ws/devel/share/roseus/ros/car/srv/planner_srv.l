;; Auto-generated. Do not edit!


(when (boundp 'car::planner_srv)
  (if (not (find-package "CAR"))
    (make-package "CAR"))
  (shadow 'planner_srv (find-package "CAR")))
(unless (find-package "CAR::PLANNER_SRV")
  (make-package "CAR::PLANNER_SRV"))
(unless (find-package "CAR::PLANNER_SRVREQUEST")
  (make-package "CAR::PLANNER_SRVREQUEST"))
(unless (find-package "CAR::PLANNER_SRVRESPONSE")
  (make-package "CAR::PLANNER_SRVRESPONSE"))

(in-package "ROS")





(defclass car::planner_srvRequest
  :super ros::object
  :slots (_start _end ))

(defmethod car::planner_srvRequest
  (:init
   (&key
    ((:start __start) 0)
    ((:end __end) 0)
    )
   (send-super :init)
   (setq _start (round __start))
   (setq _end (round __end))
   self)
  (:start
   (&optional __start)
   (if __start (setq _start __start)) _start)
  (:end
   (&optional __end)
   (if __end (setq _end __end)) _end)
  (:serialization-length
   ()
   (+
    ;; int64 _start
    8
    ;; int64 _end
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _start
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _start (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _start) (= (length (_start . bv)) 2)) ;; bignum
              (write-long (ash (elt (_start . bv) 0) 0) s)
              (write-long (ash (elt (_start . bv) 1) -1) s))
             ((and (class _start) (= (length (_start . bv)) 1)) ;; big1
              (write-long (elt (_start . bv) 0) s)
              (write-long (if (>= _start 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _start s)(write-long (if (>= _start 0) 0 #xffffffff) s)))
     ;; int64 _end
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _end (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _end) (= (length (_end . bv)) 2)) ;; bignum
              (write-long (ash (elt (_end . bv) 0) 0) s)
              (write-long (ash (elt (_end . bv) 1) -1) s))
             ((and (class _end) (= (length (_end . bv)) 1)) ;; big1
              (write-long (elt (_end . bv) 0) s)
              (write-long (if (>= _end 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _end s)(write-long (if (>= _end 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _start
#+(or :alpha :irix6 :x86_64)
      (setf _start (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _start (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _end
#+(or :alpha :irix6 :x86_64)
      (setf _end (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _end (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass car::planner_srvResponse
  :super ros::object
  :slots (_path ))

(defmethod car::planner_srvResponse
  (:init
   (&key
    ((:path __path) 0)
    )
   (send-super :init)
   (setq _path (round __path))
   self)
  (:path
   (&optional __path)
   (if __path (setq _path __path)) _path)
  (:serialization-length
   ()
   (+
    ;; int64 _path
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _path
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _path (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _path) (= (length (_path . bv)) 2)) ;; bignum
              (write-long (ash (elt (_path . bv) 0) 0) s)
              (write-long (ash (elt (_path . bv) 1) -1) s))
             ((and (class _path) (= (length (_path . bv)) 1)) ;; big1
              (write-long (elt (_path . bv) 0) s)
              (write-long (if (>= _path 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _path s)(write-long (if (>= _path 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _path
#+(or :alpha :irix6 :x86_64)
      (setf _path (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _path (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass car::planner_srv
  :super ros::object
  :slots ())

(setf (get car::planner_srv :md5sum-) "1d89cdb41487474b11205506e2f1ce37")
(setf (get car::planner_srv :datatype-) "car/planner_srv")
(setf (get car::planner_srv :request) car::planner_srvRequest)
(setf (get car::planner_srv :response) car::planner_srvResponse)

(defmethod car::planner_srvRequest
  (:response () (instance car::planner_srvResponse :init)))

(setf (get car::planner_srvRequest :md5sum-) "1d89cdb41487474b11205506e2f1ce37")
(setf (get car::planner_srvRequest :datatype-) "car/planner_srvRequest")
(setf (get car::planner_srvRequest :definition-)
      "int64 start
int64 end
---
int64 path


")

(setf (get car::planner_srvResponse :md5sum-) "1d89cdb41487474b11205506e2f1ce37")
(setf (get car::planner_srvResponse :datatype-) "car/planner_srvResponse")
(setf (get car::planner_srvResponse :definition-)
      "int64 start
int64 end
---
int64 path


")



(provide :car/planner_srv "1d89cdb41487474b11205506e2f1ce37")


