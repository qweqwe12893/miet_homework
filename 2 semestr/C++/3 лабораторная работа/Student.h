#include <vector>
#include <cstring>
#include <cmath>
#include <fstream>

#include "Date.h"


#include <iostream>




class Student {
private:
    char* fam;
    char* name;

public:
    int grup;
    static int count;

    Date birthday;

    static int the_longest_fam_len;
    static int the_longest_name_len;
    static int max_grup_len;

    Student(string fam_arg, string name_arg, int grup_arg, int day, int month, int year);
    ~Student();
    Student(const Student &p);

    char* GetFam();
    char* GetName();
    static int GetCount();

    static void add_student(vector<Student> &arr);
    static void show_database(vector<Student> arr, const char* database_title);
    static void halt(vector<Student> unsaved_database);
};


std::ostream& operator << (ostream &os, Student &person);
bool operator==(Student& person, Date& date);

void find_student_by_name(vector<Student> database);
void find_student_by_grup(vector<Student> database);
void find_student_by_birthday(vector<Student> database);

void print_whitespaces(int num_of_all_char, int num_of_printed);
void print_line(int num);
int max(int a, int b);







