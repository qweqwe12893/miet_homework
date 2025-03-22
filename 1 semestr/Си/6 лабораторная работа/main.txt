#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>




struct parcel
{
    char* sender_lastname;
    char* sender_firstname;
    char* sender_address;
    char* reciver_lastname;
    char* reciver_firstname;
    char* reciver_address;
    double weight;
};




void add_parcel(struct parcel** list, int* n) {
    *list = (struct parcel*)realloc(*list, sizeof(struct parcel) * (*n + 1));
    struct parcel* ptr = &(*list)[*n]; 
    char buff[30];

    printf("Введите фамилию отправителя: ");
    scanf("%29s", buff);
    ptr->sender_lastname = (char*)malloc(strlen(buff) + 1);
    strcpy(ptr->sender_lastname, buff);

    printf("Введите имя отправителя: ");
    scanf("%29s", buff);
    ptr->sender_firstname = (char*)malloc(strlen(buff) + 1);
    strcpy(ptr->sender_firstname, buff);

    printf("Введите адрес отправителя: ");
    scanf("%29s", buff);
    ptr->sender_address = (char*)malloc(strlen(buff) + 1);
    strcpy(ptr->sender_address, buff);

    printf("Введите фамилию получателя: ");
    scanf("%29s", buff);
    ptr->reciver_lastname = (char*)malloc(strlen(buff) + 1);
    strcpy(ptr->reciver_lastname, buff);

    printf("Введите имя получателя: ");
    scanf("%29s", buff);
    ptr->reciver_firstname = (char*)malloc(strlen(buff) + 1);
    strcpy(ptr->reciver_firstname, buff);

    printf("Введите адрес получателя: ");
    scanf("%29s", buff);
    ptr->reciver_address = (char*)malloc(strlen(buff) + 1);
    strcpy(ptr->reciver_address, buff);

    printf("Введите вес посылки: ");
    scanf("%lf", &ptr->weight);
    
    (*n)++; // Увеличиваем размер массива
}




void display_info(struct parcel* list, int n) {
    if (n == 0) {
        printf("Нет посылок для отображения.\n");
        return; // выход из функции, если нет посылок
    }

    printf("Информация о посылках:\n");
    printf("------------------------------------------------------------------------------------------------------------------\n");
    printf("| %s | %s | %s | %s | %s | %s | %s | %s |\n", 
           "Номер      ", "Фамилия    ", "Имя        ", "Адрес      ", 
           "Фамилия    ", "Имя        ", "Адрес      ", "Вес         ");
    printf("| %s | %s | %s | %s | %s | %s | %s | %s |\n", 
           "посылки    ", "отправителя", "отправителя", "отправителя", 
           "получателя ", "получателя ", "получателя ", "            ");
    printf("------------------------------------------------------------------------------------------------------------------\n");

    for (int i = 0; i < n; i++) {
        printf("| %12d|", i + 1); // номер посылки
        printf(" %12s|", list[i].sender_lastname);
        printf(" %12s|", list[i].sender_firstname);
        printf(" %12s|", list[i].sender_address);
        printf(" %12s|", list[i].reciver_lastname);
        printf(" %12s|", list[i].reciver_firstname);
        printf(" %12s|", list[i].reciver_address);
        printf(" %13.2lf|", list[i].weight); // выводим вес с двумя знаками после запятой
        printf("\n------------------------------------------------------------------------------------------------------------------\n");
    }
}




void find_parcels_to_recipient(struct parcel* list, int n, char* lastname, char* firstname) {
    int found = 0;

    for (int i = 0; i < n; i++) {
        // srvnen strcmp 0 - одинк
        if (strcmp(list[i].reciver_lastname, lastname) == 0 && strcmp(list[i].reciver_firstname, firstname) == 0) {
            // Если совпадение найдено, выводим информацию о посылке
            if (!found) {
                printf("Найденные посылки для получателя %s %s:\n", lastname, firstname);
                printf("------------------------------------------------------------------------------------------------------------------\n");
                printf("| %s | %s | %s | %s | %s | %s | %s | %s |\n", "Номер      ", "Фамилия    ", "Имя        ", "Адрес      ", "Фамилия    ", "Имя        ", "Адрес      ", "Вес         ");
                printf("| %s | %s | %s | %s | %s | %s | %s | %s |\n", "посылки    ", "отправителя", "отправителя", "отправителя", "получателя ", "получателя ", "получателя ", "            ");
                printf("------------------------------------------------------------------------------------------------------------------\n");
                found = 1; 
            }

            printf("| %12d|", i + 1);
            printf(" %12s|", list[i].sender_lastname);
            printf(" %12s|", list[i].sender_firstname);
            printf(" %12s|", list[i].sender_address);
            printf(" %12s|", list[i].reciver_lastname);
            printf(" %12s|", list[i].reciver_firstname);
            printf(" %12s|", list[i].reciver_address);
            printf(" %13.2lf|", list[i].weight);
            printf("\n------------------------------------------------------------------------------------------------------------------\n");
        }
    }

    if (!found) {
        printf("Не найдено ни одной посылки для получателя %s %s.\n", lastname, firstname);
    }
}




void find_and_sort_parcels_above_weight(struct parcel* list, int n, double weight_threshold) {
    // буф
    struct parcel* filtered_parcels = (struct parcel*)malloc(sizeof(struct parcel) * n);
    int count = 0;

    // фильтр вес
    for (int i = 0; i < n; i++) {
        if (list[i].weight > weight_threshold) {
            filtered_parcels[count++] = list[i]; // Копируем посылку в новый массив
        }
    }

    // сорт в алф
    for (int i = 0; i < count - 1; i++) {
        for (int j = i + 1; j < count; j++) {
            if (strcmp(filtered_parcels[i].reciver_lastname, filtered_parcels[j].reciver_lastname) > 0) {
                struct parcel temp = filtered_parcels[i];
                filtered_parcels[i] = filtered_parcels[j];
                filtered_parcels[j] = temp;
            }
        }
    }


    if (count > 0) {
        printf("Посылки с весом больше %.2lf:\n", weight_threshold);
        printf("------------------------------------------------------------------------------------------------------------------\n");
        printf("| %s | %s | %s | %s | %s | %s | %s | %s |\n", "Номер      ", "Фамилия    ", "Имя        ", "Адрес      ", "Фамилия    ", "Имя        ", "Адрес      ", "Вес         ");
        printf("| %s | %s | %s | %s | %s | %s | %s | %s |\n", "посылки    ", "отправителя", "отправителя", "отправителя", "получателя ", "получателя ", "получателя ", "            ");
        printf("------------------------------------------------------------------------------------------------------------------\n");
        
        for (int i = 0; i < count; i++) {
            printf("| %12d|", i + 1);
            printf(" %12s|", filtered_parcels[i].sender_lastname);
            printf(" %12s|", filtered_parcels[i].sender_firstname);
            printf(" %12s|", filtered_parcels[i].sender_address);
            printf(" %12s|", filtered_parcels[i].reciver_lastname);
            printf(" %12s|", filtered_parcels[i].reciver_firstname);
            printf(" %12s|", filtered_parcels[i].reciver_address);
            printf(" %13.2lf|", filtered_parcels[i].weight);
            printf("\n------------------------------------------------------------------------------------------------------------------\n");
        }
    } else {
        printf("Нет посылок с весом больше %.2lf.\n", weight_threshold);
    }

    // Освобождение временной памяти
    free(filtered_parcels);
}




int main()
{
    setlocale(LC_ALL, "Rus");

    int n = 0; 
    struct parcel *all_parcels = NULL; 
    int ans = -1; 
    char buffer_lastname[30]; 
    char buffer_firstname[30]; 
    double buffer_weight; 

    while (1) 
    { 
        printf("\nКаталог действий:\n"); 
        printf("    добавить посылку.............................1\n"); 
        printf("    распечатать информацию о посылках............2\n"); 
        printf("    найти посылки для заданного получателя.......3\n"); 
        printf("    найти все посылки с весом больше заданного...4\n");
        printf("    выйти........................................0\n"); // Добавляем возможность выхода
        printf("Выберите действие: ");
        scanf("%d", &ans); 

        switch (ans) 
        { 
        case 1: 
            add_parcel(&all_parcels, &n); 
            break; 
        case 2: 
            display_info(all_parcels, n); 
            break; 
        case 3: 
            printf("Введите фамилию получателя: "); 
            scanf("%s", buffer_lastname); 
            printf("Введите имя: "); 
            scanf("%s", buffer_firstname); 
            find_parcels_to_recipient(all_parcels, n, buffer_lastname, buffer_firstname); 
            break; 

        case 4: 
            printf("Введите вес: "); 
            scanf("%lf", &buffer_weight);
            find_and_sort_parcels_above_weight(all_parcels, n, buffer_weight); 
            break;

        case 0:
            printf("Выход из программы.\n");
            return 0; 

        default: 
            printf("По номеру нет зарегистрированных действий\n"); 
        } 
    } 
}

/*
    • добавить новую посылку;
    • распечатать информацию о посылках в табличном виде;
    • найти все посылки для заданного получателя (получатель – это фамилия + имя) результат вывести на экран;
    • найти все посылки с весом больше заданного, результат сортировать по алфавиту (по получателю), запомнить в массиве и вывести на экран.
*/
