#include <stdio.h>
   int main () {
char name [50] ;
int i=0 ;
int ans , rod;
char nmb1 , nmb2 , c ;

    printf("Hello . Welcome to the calculator system \nPleas enter your username\n");
    fgets(name , sizeof(name) , stdin) ;
         for (i=0;i<50;i++){
    if (name[i]==' ') {
         printf("Error wrong data type \nThe username can consst of CAPITAL_LITER and small_liter and nubers and sidns(!,@,_...) \nPlease try agein with a username that consists without space .");
         break ;
         }}

    if (i == 50){
      printf("Hello %senter the calculationas it consists of one integar number as A+B without space\n",name);


      scanf("%c",&nmb1) ;
      scanf("%c",&c) ;
      scanf("%c",&nmb2) ;
if (nmb1>47 && nmb1<58 && nmb2>47 && nmb2<58)       {
            if (c=='+'){
              ans=nmb1-48+nmb2-48;     
              printf("The answer is : %d\n",ans);                        
                }
            else if (c=='-'){
              ans=(nmb1-48)-(nmb2-48);     
              printf("The answer is : %d\n",ans);                        
                }
            else if (c=='*'){
              ans=(nmb1-48)*(nmb2-48);     
              printf("The answer is : %d\n",ans);                        
                }
            else if (c=='/'){
                  if (nmb2-48==0){
                    printf("Cannot be divided by zero");
                 }
                 else {
              ans=(nmb1-48)/(nmb2-48);
              rod=(nmb1-48)%(nmb2-48);     
              printf("The answer of the division is : %d\nAnd the remainder is : %d",ans,rod); } }                      
                           
                
                else{
                   printf("Error\nPlease check the calculation.");  }      }                

              
              else if (c==32){
              printf("Error\nPlease enter the calculation as A+B without space.");}
              else{
              printf("Error wrong data type \nPlease check the calculation that consists of one integer numbers only."); 
              }

    }
 return (0) ;
}