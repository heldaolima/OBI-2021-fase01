#include <stdio.h>

int main()
{
    int tot = 0;
    char r;
    for (int i = 0; i < 6; i++)
    {
        scanf(" %c", &r);
        if (r == 'V') tot++;
    }
    if (tot == 5 || tot == 6) printf("1\n");
    else if (tot == 3 || tot == 4) printf("2\n");
    else if (tot == 1 || tot == 2) printf("3\n");
    else printf("-1\n");
    return 0;
}