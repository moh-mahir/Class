#include <stdio.h>
void mmm(char *x)  {
                     while (*x > '\0'){
                     printf("%c", *x);
                     x++;}
    /*for (*x;*x>'\0';x++){
     printf("%c", *x);
    }*/
     }
   int main () {
      char x[] ="Home Work";
      mmm(x); 

 return (0) ;
}