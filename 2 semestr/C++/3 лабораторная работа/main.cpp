#include "Student.h"
#include "Date.h"
#include <string>

int main() {
    setlocale(LC_ALL, "rus");
    vector<Student> database;

    fstream file("data.txt", ios::in);
    string fam_temp, name_temp;
    int grup_temp;

    int day_temp, month_temp, year_temp;

    while (file >> fam_temp >> name_temp >> grup_temp >> day_temp >> month_temp >> year_temp) {

        database.push_back(Student(fam_temp, name_temp, grup_temp, day_temp, month_temp, year_temp));
    }

    int input;
    cout << "1. Добавить студента\n"
         << "2. Распечатать базу студентов\n"
         << "3. Вывести количество студентов\n"
         << "4. Найти студента по фамилии и имени\n"
         << "5. Найти студента по номеру группы\n"
         << "6. Найти студента по Дню рождения\n"
         << "9. Выйти из программы\n";

    do {
        cout << "Выберите действие: ";
        cin >> input;

        switch (input) {
            case 1:
                Student::add_student(database);
                break;

            case 2:
                Student::show_database(database, "База данных «Студенты»");
                break;

            case 3:
                cout << "Количество студентов: " << Student::GetCount() << endl;
                break;

            case 4:
                find_student_by_name(database);
                break;

            case 5:
                find_student_by_grup(database);
                break;

            case 6:
                find_student_by_birthday(database);
                break;

            case 9:
                Student::halt(database);
                break;
            default:
                return 0;
        }
    } while (true);
}








