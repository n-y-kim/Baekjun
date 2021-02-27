// # push X: 정수 X를 큐에 넣는 연산이다.
// # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// # size: 큐에 들어있는 정수의 개수를 출력한다.
// # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
// # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void push(int);
void pop();
int size();
void empty();
void front();
void back();

typedef struct QueueNode {
    int num;
    struct QueueNode* frontLink;
    struct QueueNode* backLink;
} QueueNode;

QueueNode *front_;
QueueNode *rear;

int main() {
    front_ = NULL;
    rear = front_;
    int inputNum;
    int insertNum = 0;
    int printSize;

    scanf("%d", &inputNum);
    getchar();

    while(inputNum>0){
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
                printSize = size();
                printf("%d\n", printSize);
                break;
            case 'e':
                empty();
                break;
            case 'f':
                front();
                break;
            case 'b':
                back();
                break;

           }
        }
        inputNum--;
        insertNum = 0;
    }
}

void push(int num){
    QueueNode* temp = (QueueNode*)malloc(sizeof(QueueNode));
    temp->num = num;
    if (front_ == NULL && rear == NULL) { //빈 queue에 push할 때
        temp->backLink = NULL;
        temp->frontLink = NULL;
        front_ = temp;
        rear = temp;
    }
    else { 
        temp->frontLink = rear;
        rear->backLink = temp;
        temp->backLink = NULL;
        rear = temp;
    }
}

void pop() {
    QueueNode* temp = front_;
    if (front_ == NULL && rear == NULL) {
        printf("-1\n");
        return;
    } 
    else if (front_ == rear){
        printf("%d\n", temp->num);
        front_ = NULL;
        rear = NULL;
        free(temp);
    }
    else { //하나 있을때랑 여러개 있을때 나눠줘야 하나?
        printf("%d\n", temp->num);
        front_ = front_->backLink;
        front_->frontLink = NULL;
        free(temp);
    }
}

int size() {
    QueueNode* temp = front_;

    int size = 0;
    while(temp != NULL){
        temp = temp->backLink;
        size++;
    }

    //printf("%d\n", size);
    return size;
}

void empty() {
    int getSize = size();

    if (getSize == 0) {
        printf("1\n");
    } else {
        printf("0\n");
    }
}

void front() {
    if (front_ == NULL && rear == NULL) {
        printf("-1\n");
    } else {
        printf("%d\n",front_->num);
    }
}

void back() {
    if (front_ == NULL && rear == NULL) {
        printf("-1\n");
    } else {
        printf("%d\n",rear->num);
    }
}