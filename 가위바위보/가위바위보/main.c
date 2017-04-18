//가위바위보 게임
//rand()함수 이용
//조건문 if를 통해 입력한 수에 따라 랜덤으로 생성된 수와 비교

#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main (void){
    srand((unsigned int)time(0));
    int user;
    int gameIsDone = 0;
    printf("<<<<<<가위바위보 게임>>>>>>\n");
    while(gameIsDone == 0){
        printf("가위(1), 바위(2), 보(3)를 입력해라.\n");
        scanf("%d", &user);
        int rand_num = (rand()%3)+1;
        
        if(user == 1 || user == 2 || user == 3){
            if(user == rand_num){
                printf("비겼다. 다시 해라. \n");}
            else if((user == 1 && rand_num == 3) || (user == 2 && rand_num == 1) || (user == 3 && rand_num == 2)){
                printf("이겼다. 다시 할거냐?\n");
                printf("다시 할거면 0, 종료는 1\n");
                scanf("%d", &gameIsDone);}
            else
            {printf("졌다.\n");
                printf("다시 할거면 0, 종료는 1\n");
                scanf("%d", &gameIsDone);}
        }
        
        if(gameIsDone == 1)
            return 0;
    }
}
