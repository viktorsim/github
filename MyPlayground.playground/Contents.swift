#include <stdio.h>

int main (void){
    
    char name[20];
    char gender[6];
    int birthday, period;
    char destination[20];
    
    printf("<<<<< Interview for Travel Plan >>>>>>\n");
    printf("Input your name : ");
    scanf("%s", name);
    printf("Gender : ");
    scanf("%s", gender);
    printf("Day of birth(ex. 19930310)");
    scanf("%d", &birthday);
    printf("Destination : ");
    scanf("%s", destination);
    printf("Period of trip(ex. 5) : ");
    scanf("%d", &period);
    
    printf("NAME : %s\nGENDER : %s\nDAY OF BIRTH : %d\nDESTINATION : %s\nPERIOD OF TRIP : %d", name, gender, birthday, destination, period);
    
    return 0;
}