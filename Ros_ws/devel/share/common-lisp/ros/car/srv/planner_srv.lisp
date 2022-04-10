; Auto-generated. Do not edit!


(cl:in-package car-srv)


;//! \htmlinclude planner_srv-request.msg.html

(cl:defclass <planner_srv-request> (roslisp-msg-protocol:ros-message)
  ((start
    :reader start
    :initarg :start
    :type cl:integer
    :initform 0)
   (end
    :reader end
    :initarg :end
    :type cl:integer
    :initform 0))
)

(cl:defclass planner_srv-request (<planner_srv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <planner_srv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'planner_srv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name car-srv:<planner_srv-request> is deprecated: use car-srv:planner_srv-request instead.")))

(cl:ensure-generic-function 'start-val :lambda-list '(m))
(cl:defmethod start-val ((m <planner_srv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader car-srv:start-val is deprecated.  Use car-srv:start instead.")
  (start m))

(cl:ensure-generic-function 'end-val :lambda-list '(m))
(cl:defmethod end-val ((m <planner_srv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader car-srv:end-val is deprecated.  Use car-srv:end instead.")
  (end m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <planner_srv-request>) ostream)
  "Serializes a message object of type '<planner_srv-request>"
  (cl:let* ((signed (cl:slot-value msg 'start)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'end)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <planner_srv-request>) istream)
  "Deserializes a message object of type '<planner_srv-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'start) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'end) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<planner_srv-request>)))
  "Returns string type for a service object of type '<planner_srv-request>"
  "car/planner_srvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'planner_srv-request)))
  "Returns string type for a service object of type 'planner_srv-request"
  "car/planner_srvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<planner_srv-request>)))
  "Returns md5sum for a message object of type '<planner_srv-request>"
  "1d89cdb41487474b11205506e2f1ce37")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'planner_srv-request)))
  "Returns md5sum for a message object of type 'planner_srv-request"
  "1d89cdb41487474b11205506e2f1ce37")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<planner_srv-request>)))
  "Returns full string definition for message of type '<planner_srv-request>"
  (cl:format cl:nil "int64 start~%int64 end~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'planner_srv-request)))
  "Returns full string definition for message of type 'planner_srv-request"
  (cl:format cl:nil "int64 start~%int64 end~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <planner_srv-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <planner_srv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'planner_srv-request
    (cl:cons ':start (start msg))
    (cl:cons ':end (end msg))
))
;//! \htmlinclude planner_srv-response.msg.html

(cl:defclass <planner_srv-response> (roslisp-msg-protocol:ros-message)
  ((path
    :reader path
    :initarg :path
    :type cl:integer
    :initform 0))
)

(cl:defclass planner_srv-response (<planner_srv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <planner_srv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'planner_srv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name car-srv:<planner_srv-response> is deprecated: use car-srv:planner_srv-response instead.")))

(cl:ensure-generic-function 'path-val :lambda-list '(m))
(cl:defmethod path-val ((m <planner_srv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader car-srv:path-val is deprecated.  Use car-srv:path instead.")
  (path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <planner_srv-response>) ostream)
  "Serializes a message object of type '<planner_srv-response>"
  (cl:let* ((signed (cl:slot-value msg 'path)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <planner_srv-response>) istream)
  "Deserializes a message object of type '<planner_srv-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'path) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<planner_srv-response>)))
  "Returns string type for a service object of type '<planner_srv-response>"
  "car/planner_srvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'planner_srv-response)))
  "Returns string type for a service object of type 'planner_srv-response"
  "car/planner_srvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<planner_srv-response>)))
  "Returns md5sum for a message object of type '<planner_srv-response>"
  "1d89cdb41487474b11205506e2f1ce37")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'planner_srv-response)))
  "Returns md5sum for a message object of type 'planner_srv-response"
  "1d89cdb41487474b11205506e2f1ce37")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<planner_srv-response>)))
  "Returns full string definition for message of type '<planner_srv-response>"
  (cl:format cl:nil "int64 path~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'planner_srv-response)))
  "Returns full string definition for message of type 'planner_srv-response"
  (cl:format cl:nil "int64 path~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <planner_srv-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <planner_srv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'planner_srv-response
    (cl:cons ':path (path msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'planner_srv)))
  'planner_srv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'planner_srv)))
  'planner_srv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'planner_srv)))
  "Returns string type for a service object of type '<planner_srv>"
  "car/planner_srv")