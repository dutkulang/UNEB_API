# UNEB API

A clone of the Uganda National Examination Board Education System.
The systems aims to become a National education systems.

Schools will be registered and each school can add students each with
a unique per year index number.
    Student has a full name,a photo, sex, date of Birth, index number and
    telephone contact.


Aims.
    Return all students who sat in year
    http://127.0.0.1:8000/ple/year=default to current year&center-number=center-number
    
    Return result for a student
    http://127.0.0.1:8000/PLE/year = year_of_sitting & school_center_number & student_index
    http://127.0.0.1:8080/PLE/year=2020&center-name=003267&index=081
    
    http://127.0.0.1:8000/upe/003267    (UPE -> Uganda Primary Education aka Government School)
    http://127.0.0.1:8000/nupe/52782    Private School

