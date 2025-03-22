#include "Date.h"



Date::Date(int dd, int mm, int yyyy)
{
    day = dd;
    month = mm;
    year = yyyy;
}

Date::Date()
{
    day = 0;
    month = 0;
    year = 0;
}

ostream& operator << (ostream &os, Date &date)
{
    return os << date.day << "/" << date.month << "/" << date.year;
}


int Date::GetDay()
{
    return day;
}


int Date::GetMonth()
{
    return month;
}


int Date::GetYear()
{
    return year;
}





