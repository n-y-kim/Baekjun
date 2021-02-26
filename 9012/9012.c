#include <stdio.h>
#include <stdlib.h>

void calculate(char*, int);
void result(char*);

int main() {
    int input, i = 0;

    scanf("%d", &input);
    getchar();

    while(input > 0){
        char vps[50];
        scanf("%s", vps);
        char* pointVps = vps;
        calculate(pointVps, 0);
        result(pointVps);
        input--;
    }
}

void calculate(char* vps, int start){
    int i = 0, j = 0;

    if (vps[start] == '\0' || vps[start] == ')') return;
    else if (vps[start] == '0') { calculate(vps, start+1); }
    else {
        i= start;
        while(vps[i] != ')'){
            i++;
            if (vps[i] == '\0') break;
            else if (vps[i] == ')') {

                vps[start] = '0';
                vps[i] = '0';

                break;
            } 
        }
        calculate(vps, start+1); 
    }
}

void result(char* vps){
    int i = 0, result = 0;
    while(vps[i] != '\0'){
        if (vps[i] == '(' || vps[i] == ')') { 
            printf("NO\n"); 
            return;
        }
        i++;
    }
    printf("YES\n");
    return;
}