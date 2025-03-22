#include <iostream>
#include <cstring> // для работы с стр в си-стиле
#include <vector>
#include <cmath>
#include <fstream>// для чтения и записи
#include <string> // для getstring
using namespace std;


void print_whitespaces(int num_of_all_char, int num_of_printed);
void print_line(int num);
int max(int a, int b);



class Student
{
    private:
        char* fam;
        char* name;


    public:
        int grup;      // номер группы
        static int count;   // счетчик существующих объектов класса

        static int the_longest_fam_len; // для красивой таблички
        static int the_longest_name_len;
        static int max_grup_len;

    public:

        Student(string fam_arg, string name_arg, int grup_arg)
        {
            fam  = new char[fam_arg.length()];
            strcpy(fam, fam_arg.c_str());
            the_longest_fam_len = max(the_longest_fam_len, fam_arg.length());

            name = new char[name_arg.length()];
            strcpy(name, name_arg.c_str());
            the_longest_name_len = max(the_longest_name_len, name_arg.length());

            grup = grup_arg;
            max_grup_len = max(max_grup_len, log10(grup)+1);

            count++;
        }


        ~Student()
        {
            delete[] fam;
            delete[] name;
        }


        Student(const Student &p) // конструктор копирования чтобы не было 2х ссылок на 1 область памяти при коп объ
        {
            fam = new char[strlen(p.fam) + 1];
            strcpy(fam, p.fam);

            name = new char[strlen(p.name) + 1];
            strcpy(name, p.name);

            grup = p.grup;
        }


        char* GetFam()
        {
            return fam;
        }


        char* GetName()
        {
            return name;
        }


        static int GetCount()
        {
            return Student::count;
        }


        static void add_student(vector<Student> & arr)
        {

            string  temp_fam;
            string  temp_name;
            int     temp_grup;

            cout << "Введите фамилию студента: ";
            cin  >> temp_fam;

            cout << "Введите имя студента: ";
            cin  >> temp_name;

            cout << "Введите группу студента (число): ";
            cin  >> temp_grup;
            cout << endl;

            arr.push_back(Student(temp_fam, temp_name, temp_grup));


        }


        static void show_database(vector<Student> arr)
        {
            int fam_num_of_char  = the_longest_fam_len + 4;         // кол-во символов в столбце "фамилия"
            int name_num_of_char = the_longest_name_len + 4;        // кол-во символов в столбце "имя"
            int grup_num_of_char = max_grup_len + 4; // кол-во символов в столбце "группа"
            // количество цифер в числе длинной n - log10(n)+1

            cout << endl;
            cout << "База данных «Студенты»" << endl;
            print_line(fam_num_of_char+name_num_of_char+grup_num_of_char);

            cout << "Фамилия";
            print_whitespaces(fam_num_of_char, 7);

            cout << "Имя";
            print_whitespaces(name_num_of_char, 3);

            cout << "Группа" << endl;

            print_line(fam_num_of_char+name_num_of_char+grup_num_of_char);


            for (int i=0; i<count; i++)
            {
                cout << arr[i].GetFam();
                print_whitespaces(fam_num_of_char, strlen(arr[i].GetFam()));

                cout << arr[i].GetName();
                print_whitespaces(name_num_of_char, strlen(arr[i].GetName()));

                cout << arr[i].grup << endl;
            }
            print_line(fam_num_of_char+name_num_of_char+grup_num_of_char);
            cout << "Количество записей в базе: " << count << endl << endl;
        }


        static void halt(vector<Student> unsaved_database)
        {
            ofstream output;
            output.open("data.txt"); // при откр удаляются старые данные

            for (Student  i : unsaved_database)
            {
                output << i.GetFam() << " " << i.GetName() << " " << i.grup << endl;
            }

            exit(0);
        }

};






int Student::count = 0;

int Student::the_longest_fam_len  = 0;
int Student::the_longest_name_len = 0;
int Student::max_grup_len         = 0;



void find_student_by_name(vector<Student> database)
{
    char* fam_arg = (char*)malloc(30*sizeof(char));
    char* name_arg = (char*)malloc(30*sizeof(char));
    cout << "Введите фамилию: ";
    cin >> fam_arg;

    cout << "Введите имя: ";
    cin >> name_arg;

    int falg_if_exist = 0;

    for (Student i : database)
    {
        if (strcmp(i.GetFam(), fam_arg) == 0)
        {
            if (strcmp(i.GetName(), name_arg) == 0)
            {

                if (falg_if_exist == 0)
                {
                    falg_if_exist = 1;
                    cout << "Найденные студенты:" << endl;
                }

                cout << i.GetFam() << " " << i.GetName() << " " << i.grup << endl;
            }
        }
    }

    if (falg_if_exist == 0) { cout << "Подходящие студенты не найдены" << endl;}
}



void find_student_by_grup(vector<Student> database)
{
    int grup_arg;
    cout << "Введите номер группы (число): ";
    cin >> grup_arg;

    int falg_if_exist = 0;

    for (Student i : database)
    {
        if (i.grup == grup_arg)
        {

            if (falg_if_exist == 0)
            {
                falg_if_exist = 1;
                cout << "Найденные студенты в группе " << grup_arg << ":" << endl;
            }

            cout << i.GetFam() << " " << i.GetName() << " " << endl;
        }
    }

    if (falg_if_exist == 0) { cout << "Подходящие студенты не найдены" << endl;}
}



int main()
{

    setlocale(LC_ALL, "rus");
    vector<Student> database;


    fstream file("data.txt", ios::in);

    string fam_temp;
    string name_temp;
    int grup_temp;

    while (file >> fam_temp >> name_temp >> grup_temp)
    {
        database.push_back(Student(fam_temp, name_temp, grup_temp));

        // для пробелов чтобы табличка печаталась красивой
        Student::the_longest_fam_len  = max(Student::the_longest_fam_len, fam_temp.length());
        Student::the_longest_name_len = max(Student::the_longest_name_len, name_temp.length());
        Student::max_grup_len   = max(Student::max_grup_len, log10(grup_temp)+1);
    }

    int input;
    cout << "Добавить студента...................1" << endl;
    cout << "Распечатать базу студентов..........2" << endl;
    cout << "Вывести количество студентов........3" << endl;
    cout << "Найти студента по фамилии и имени...4" << endl;
    cout << "Найти студента по номеру группы.....5" << endl;
    cout << "Выйти из программы..................9" << endl;

    do
    {
        cout << "Выберите действие: ";
        cin >> input;

        switch(input)
        {
            case 1:
                Student::add_student(database);
                break;

            case 2:
                Student::show_database(database);
                break;

            case 3:
                cout << "Количество студентов в базе данных: " << Student::GetCount() << endl;
                break;

            case 4:
                find_student_by_name(database);
                break;

            case 5:
                find_student_by_grup(database);
                break;

            case 9:
                Student::halt(database);

            default:
                return 0;

        }
    } while (1);



}




void print_whitespaces(int num_of_all_char, int num_of_printed)
{
    for (int i=num_of_printed; i<num_of_all_char; i++)
    {
        cout << ' ';
    }

}

void print_line(int num)
{
    for (int i=0; i<num; i++)
    {
        cout << "-";
    }
    cout << endl;
}

int max(int a, int b)
{
    return a>b? a:b;
}

