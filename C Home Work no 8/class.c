#include <stdio.h>
   int main () {
char name [50] ;
int i=0 ;
int nmb1 , nmb2 , ans , rod;
char c ;

    printf("Hello . Welcome to the calculator system \nPleas enter your username\n");
    fgets(name , sizeof(name) , stdin) ;
         for (i=0;i<50;i++){
    if (name[i]==' ') {
         printf("Error wrong data type \nThe username can consst of CAPITAL_LITER and small_liter and sidns(!,@,_...) \nPlease try agein with a username that consists without space .");
         break ;
         }}

    if (i == 50){
      printf("Hello %senter the calculationas as A+B without space\n",name);


      scanf("%d",&nmb1) ;
      scanf("%c",&c) ;
      scanf("%d",&nmb2) ;
            if (c=='+'){
              ans=nmb1+nmb2;     
              printf("The answer is : %d\n",ans);                        
                }
            else if (c=='-'){
              ans=nmb1-nmb2;     
              printf("The answer is : %d\n",ans);                        
                }
            else if (c=='*'){
              ans=nmb1*nmb2;     
              printf("The answer is : %d\n",ans);                        
                }
            else if (c=='/'){
                  if (nmb2==0){
                    printf("Cannot be divided by zero");
                 }
                 else {
              ans=nmb1/nmb2;
              rod=nmb1%nmb2;     
              printf("The answer of the division is : %d\nAnd the remainder is : %d",ans,rod); }                       
                }
            else if (c==' '){
              printf("Error\nPlease enter the calculation as A+B without space.");                        
                }
              else{
              printf("Error wrong data type \nPlease try agein with a calculation that consists of integer numbers only."); 
              }
     

    }
 return (0) ;
}