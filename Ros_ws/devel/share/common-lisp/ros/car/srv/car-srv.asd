
(cl:in-package :asdf)

(defsystem "car-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "planner_srv" :depends-on ("_package_planner_srv"))
    (:file "_package_planner_srv" :depends-on ("_package"))
  ))