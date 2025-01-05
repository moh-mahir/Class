#include <stdio.h>
int main () {
    int x=1;
   int i=1;
  
    for(i;i<=5;i++){    
        for(x;x<=10;x++){
              if ( (i>1 && i<5)&&(x>1 && x<10) ) {
                     printf("* "); }
              else {
                    printf("# ");}
         if (x == 10) {       
            printf("\n");}
        } x=1;
    }
    

 return (0) ;
}