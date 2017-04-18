#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    char name[10] ;
    
    printf("Hello world!\n");
    printf("What is your name?\n");
    scanf("%s", name);
    
    printf("It is good to meet you, %s\n", name);
    system("PAUSE");
    return 0;
}
