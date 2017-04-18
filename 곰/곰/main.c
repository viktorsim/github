//곰게임

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (void){
    
    srand((unsigned int)time(0));
    int runNumber = rand()%2 ;
    int chooseNumber;
    int bear = 100;
    int attack = 1;
    
    printf("<<<< 곰 등 판 >>>>\n");
    printf("싸울거야?\n싸움 : 0, 도망 : 1\n");
    scanf("%d", &chooseNumber);
    if(chooseNumber == 1){
        if(runNumber == 0){
            printf("도망갔당ㅎ\n");
            return 0;}
        else{
            printf("안돼. 싸워야 한다.\n");
            chooseNumber = 0 ;
        }
    }
    if(chooseNumber == 0){
        printf("싸운다.\n6번 안에 곰을 물리쳐야 한다.\n공격시작.\n");
        while(attack != 7){
            int pihae = rand()%30 ;
            printf("%d번째 공격입니다.\n", attack);
            printf("당신은 %d만큼의 피해를 입혔읍니다.\n", pihae);
            bear = bear - pihae;
            printf("곰의 체력은 %d입니다.\n", bear);
            attack ++ ;
            
            if(bear <= 0){
                printf("이겼읍니다.^^\n");
                return 0;
            }
        }
        printf("죽었다.\n");
    }
}
