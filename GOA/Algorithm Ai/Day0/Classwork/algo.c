
#include <stdio.h>

int main ()
{
    int a[] = {1, 3, 2};
    int n = 3;
    int i = 0;
    i = n - 1;
    int MAX = a [ i ] ;
    int INDEX = i ;
    
    for ( i = n - 2; i >= 0 ;i--)
    {
        if ( MAX < a [ i ] )
        {
            MAX = a [ i ] ;
            INDEX = i ;
        }
    }
    printf("\nMAX is %d, and INDEX is %d\n\n", MAX, INDEX);
    
    return 0 ;
    
}

//operations:1=, 2-, 3 if, 4.return, 5.printf

//კოდშია 11 მინიჭება

//how many times opperations have done?
//if 3, return 1, printf 1, minus 4, equals 10,

//f return(a, n) = 1 ყოველთვის პასუხი ერთია 

//f = (a, n) {
    //7
    //98 = 7+2
    //10 = 7+ 4
//}

//i = 2 i = 1 i = 0 i =-1
//a = list n = 3

//fგამოცვლა (a, n) {
    //0
    //1
    //2
    //n-1
//}


//best case = min
//worst case = max

