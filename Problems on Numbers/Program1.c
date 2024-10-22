#include<stdio.h>

float CalculatePercentage(int iMakrs , int iTotal)
{
    float percentage = 0.0f;

    if(iMakrs > iTotal)
    {
        printf("Invalid Input\n");
        return percentage;
    }
    percentage = (((float)iMakrs /(float)iTotal) * 100);
    return percentage;

}
int main()
{
    int iValue1 = 0;
    int iValue2= 0;
    float fRet = 0.0f;

    printf("Enter the marks : \n");
    scanf("%d",&iValue1);

    printf("Enter the Total marks : \n");
    scanf("%d",&iValue2);

    fRet = CalculatePercentage(iValue1,iValue2);

    printf("Your percentage is: %f\n",fRet);

    return 0;
}