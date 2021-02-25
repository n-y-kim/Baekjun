#include <stdio.h>
#include <stdlib.h>

void push(int);
void pop();
void size();
void empty();
void top();

int main() {

int N;
char* function;
int insertNum;

scanf("%d", &N);
getchar();

while (N > 0) {
    scanf("%[^\n]", function);
    getchar();
    printf("%s\n", function);
    printf("%c\n", *(function+5));
    //printf("%d\n", insertNum);
    //getchar();
    //printf("%c\n", input[0]);
    //printf("%c\n", input[1]);
    N--;
}

}

