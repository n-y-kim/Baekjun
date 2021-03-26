#include <stdio.h>
#include <stdlib.h>

int main(){
    char n_m[];
    scanf("%[^\n]", n_m);
    printf("%c %c\n",n_m[0], n_m[1]);
    int n = n_m[0];
    int m = n_m[1];

    printf("%d %d\n", n, m);
}