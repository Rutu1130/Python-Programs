#include<stdio.h>

void Display(int iNo)
{
    int iDigit = 0;

    iDigit = iNo % 10;
    printf("%d\n",iDigit);  // 1
    iNo = iNo / 10;     // 72

    iDigit = iNo % 10;
    printf("%d\n",iDigit);  // 2
    iNo = iNo / 10;     // 7

    iDigit = iNo % 10;
    printf("%d\n",iDigit);  // 7
    iNo = iNo / 10;     // 0

}

int main()
{
    int iValue = 721;

  
    Display(iValue);

    return 0;
}