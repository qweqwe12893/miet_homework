#ifndef DATE_H_INCLUDED
#define DATE_H_INCLUDED

#include <iostream>


using namespace std;

class Date
{
    friend class Student;
    friend ostream& operator << (ostream &os, Date &date);
    int day;
    int month;
    int year;

    public:

    Date();
    Date(int dd, int mm, int yyyy);

    int GetDay();
    int GetMonth();
    int GetYear();
};

ostream& operator << (ostream &os, Date &date);

#endif // DATE_H_INCLUDED
