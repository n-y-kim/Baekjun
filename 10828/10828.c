#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void push(int);
void pop();
void size();
void empty();
void top();

typedef struct stackNode {
    int number;
    struct stackNode* link;
} stackNode;

stackNode* top_;

int main() {

    int N, count = 0;
    int insertNum;
    top_ = NULL;

    scanf("%d", &N);
    getchar();


    while (N > 0) {
        char function[15] = {0};
        scanf("%[^\n]", function);
        getchar();
        
        if (function[5] >= 48 && function[5] <= 57){
            //push + number -> special case. 문자열 분할 해줘야함
            
            int i = 5, j=0;

            //숫자 시작부분부터 엔터 친 부분까지 훑기
            while (function[i] != '\0'){
                j++;
                i++;
            }

            i = 5;

            //insertNum에 숫자 저장
            while (j>0) {
                insertNum += (int)(function[i]-48) * pow(10,j-1);
                i++;
                j--;
            }

            push(insertNum);
        } 
        
        else {
            
           switch (function[0]){
               case 'p':
                    pop();
                    break;
               case 's':
                    size();
                    break;
               case 'e':
                    empty();
                    break;
               case 't':
                    top();
                    break;

           }
        }
        
        N--;
        insertNum = 0;
    }

}

void push(int insertNum){
    stackNode* temp = (stackNode*)malloc(sizeof(stackNode));

    temp->number = insertNum;
    temp->link = top_;

    top_ = temp;
}

void pop() {
    stackNode* temp = top_;

    if (top_ == NULL) {
        printf("-1\n");
        return;
    } else {
        printf("%d\n", temp->number);
        top_ = temp->link;
        free(temp);
    }
}

void size() {
    stackNode* temp = top_;
    int size = 0;
    if (temp != NULL){
        while(temp != NULL){
        
            temp = temp->link;
            size++;
        }
    }
    

    printf("%d\n", size);
}

void empty() {
    if (top_ == NULL){
        printf("1\n");
    } else {
        printf("0\n");
    }
    
}

void top() {
    stackNode* temp = top_;

    if (top_ == NULL){
        printf("-1\n");
    } else {
        printf("%d\n", temp->number);
    }
}