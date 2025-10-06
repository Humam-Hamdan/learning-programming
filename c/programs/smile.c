#include <stdio.h>    
#include <unistd.h>    
#include <stddef.h>    
#include <time.h>    
     
void delay_sec(float sec) {    
    struct timespec sleep = {    
     
        .tv_sec = sec / 1,    
        .tv_nsec = (sec - (int) sec) * 1000000000    
    };    
    nanosleep(&sleep, NULL);    
}    
     
int main() {    
    char dummybuf[4096];    
    size_t inputSize = read(0, dummybuf, 4096);    
    printf("\033[1A");    
    printf("\033[%dC", (int) inputSize);    
    for (int i = 0; i < inputSize; i++) {    
        delay_sec(0.1);    
        printf("\b \b");    
        fflush(stdout);    
    }    
    delay_sec(0.8);    
    putc(':', stdout);    
    fflush(stdout);    
    delay_sec(0.2);    
    putc(')', stdout);    
    fflush(stdout);    
    delay_sec(0.5);    
    printf("\b \b");    
    fflush(stdout);    
    delay_sec(0.2);    
    printf("\b \b");    
    fflush(stdout);    
    delay_sec(0.8);    
}
