#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int a[n];

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    for (int i = 0; i < n; i++)
    {
        if (a[i] == 0)
        {
            int j = i-1;
            if (a[j] != 0) a[j] = 0;
            else 
            {
                while (a[j] == 0) j -= 1;
                a[j] = 0;
            }
        }
    }

    int soma = 0;

    for (int i = 0; i < n; i++) soma += a[i];

    printf("%d\n", soma);

    return 0;
}