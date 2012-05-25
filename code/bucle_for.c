#include <stdio.h>

void main(int argc, char *argv[]) {
    char * l[] = {"hola", "mundo", "cruel"};
    int i, n = sizeof(l)/sizeof(char *);
    for (i=0; i<n; i++) {
        puts(l[i]);
        }
    }
