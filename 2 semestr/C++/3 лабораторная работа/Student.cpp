#include "Student.h"
#include "Date.h"
#include <cmath>
#include <string>

int Student::count = 0;
int Student::the_longest_fam_len  = 0;
int Student::the_longest_name_len = 0;
int Student::max_grup_len         = 0;

Student::Student(string fam_arg, string name_arg, int grup_arg, int day_arg, int month_arg, int year_arg) {
    fam = new char[fam_arg.length() + 1];
    strcpy(fam, fam_arg.c_str());
    the_longest_fam_len = max(the_longest_fam_len, fam_arg.length());

    name = new char[name_arg.length() + 1];
    strcpy(name, name_arg.c_str());
    the_longest_name_len = max(the_longest_name_len, name_arg.length());

    grup = grup_arg;
    max_grup_len = max(max_grup_len, log10(grup) + 1);

    birthday.day = day_arg;
    birthday.month = month_arg;
    birthday.year = year_arg;

    count++;
};

Student::~Student() {
    delete[] fam;
    delete[] name;
}

Student::Student(const Student &p) {
    fam = new char[strlen(p.fam) + 1];
    strcpy(fam, p.fam);

    name = new char[strlen(p.name) + 1];
    strcpy(name, p.name);

    grup = p.grup;

    birthday = p.birthday;
}

char* Student::GetFam() {
    return fam;
}

char* Student::GetName() {
    return name;
}


int Student::GetCount() {
    return count;
}


ostream& operator << (ostream &os, Student &person)
{
    return os << person.GetFam() << " " << person.GetName() << " " << person.grup << " " << person.birthday;
}


bool operator==(Student& person, Date& date)
{
    return ((person.birthday.GetDay() == date.GetDay()) and (date.GetMonth() == person.birthday.GetMonth()) and (date.GetYear() == person.birthday.GetYear()));
}


void Student::add_student(vector<Student> &arr) {
    string temp_fam, temp_name;
    int temp_grup;
    int day_temp, month_temp, year_temp;

    cout << "Введите фамилию студента: ";
    cin >> temp_fam;

    cout << "Введите имя студента: ";
    cin >> temp_name;

    cout << "Введите группу студента (число): ";
    cin >> temp_grup;

    cout << "Введите год рождения: ";
    cin >> year_temp;

    cout << "Введите месяц рождения: ";
    cin >> month_temp;

    cout << "Введите день рождения: ";
    cin >> day_temp;

    cout << endl;

    arr.push_back(Student(temp_fam, temp_name, temp_grup, day_temp, month_temp, year_temp));
}


void Student::show_database(vector<Student> arr, const char* database_title) {
    int fam_num_of_char  = the_longest_fam_len + 4;
    int name_num_of_char = the_longest_name_len + 4;
    int grup_num_of_char = max_grup_len + 4;

    cout << endl << database_title << endl;
    print_line(fam_num_of_char + name_num_of_char + grup_num_of_char + 13);


    cout << "Фамилия";
    print_whitespaces(fam_num_of_char, 7);

    cout << "Имя";
    print_whitespaces(name_num_of_char, 3);

    cout << "Группа";
    print_whitespaces(grup_num_of_char, 6);

    cout << "ДР" << endl;
    print_line(fam_num_of_char + name_num_of_char + grup_num_of_char + 13);

    for (int i = 0; i < Student::count; i++)
    {
        cout << arr[i].GetFam();
        print_whitespaces(fam_num_of_char, strlen(arr[i].GetFam()));

        cout << arr[i].GetName();
        print_whitespaces(name_num_of_char, strlen(arr[i].GetName()));


        cout << arr[i].grup;
        print_whitespaces(grup_num_of_char, log10(arr[i].grup) + 1);

        cout << arr[i].birthday << endl;
    }

    print_line(fam_num_of_char + name_num_of_char + grup_num_of_char + 13);
    cout << "Количество записей в базе: " << count << endl << endl;
}


void Student::halt(vector<Student> unsaved_database) {
    ofstream output("data.txt");

    for (Student i : unsaved_database) {
        output << i.GetFam() << " " << i.GetName() << " " << i.grup << " " << i.birthday.day << " " << i.birthday.month << " " << i.birthday.year << endl;
    }
    exit(0);
}


void find_student_by_name(vector<Student> database) {
    char fam_arg[30], name_arg[30];

    cout << "Введите фамилию: ";
    cin >> fam_arg;
    cout << "Введите имя: ";
    cin >> name_arg;

    bool found = false;
    for (Student i : database) {
        if (strcmp(i.GetFam(), fam_arg) == 0 && strcmp(i.GetName(), name_arg) == 0) {
            if (!found) {
                found = true;
                cout << "Найденные студенты:" << endl;
            }
            cout << i << endl;
        }
    }

    if (!found) cout << "Подходящие студенты не найдены" << endl;
}

void find_student_by_grup(vector<Student> database) {
    int grup_arg;
    cout << "Введите номер группы (число): ";
    cin >> grup_arg;

    bool found = false;
    for (Student i : database) {
        if (i.grup == grup_arg) {
            if (!found) {
                found = true;
                cout << "Найденные студенты в группе " << grup_arg << ":" << endl;
            }
            cout << i << endl;
        }
    }

    if (!found) cout << "Подходящие студенты не найдены" << endl;
}

void print_whitespaces(int num_of_all_char, int num_of_printed) {
    if (num_of_all_char >= num_of_printed){
        for (int i = num_of_printed; i < num_of_all_char+1; i++) {
            cout << ' ';
        }
    }

    else{
        for (int i=0; i < num_of_printed+1; i++)
        {
            cout << ' ';
        }
    }

}

void find_student_by_birthday(vector<Student> database)
{
    int day_temp, month_temp, year_temp;
    cout << "Введите год рождения (YYYY): ";
    cin >> year_temp;

    cout << "Введите месяц рождения (MM): ";
    cin >> month_temp;

    cout << "Введите день рождения (DD): ";
    cin >> day_temp;

    Date date(day_temp, month_temp, year_temp);
    vector<Student> Rez;

    for (Student i:database)
    {


        if (i == date)
        {
           Rez.push_back(i);
        }
    }
    Student::show_database(Rez, "Студенты с заданным Днем рождения");
}


void print_line(int num) {
    for (int i = 0; i < num; i++) {
        cout << "-";
    }
    cout << endl;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}
