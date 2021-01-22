#include <stdio.h>

#define DIAG(r, c) (r+c)
#define ANTIDIAG(r, c) (8+c-r-1)

int combination_is_solution(int combination[]);
void swap(int *a, int *b);
void check_hit(int r, int c, char arr[8]);
void permutation(int *arr, int start, int end);
int *solve();

int results[92][8];
int counter = 0;

int main()
{
    solve();
    int i;
    for (i=0; i<8; i++)
    {
        printf("%d", results[1][i]);
    }
    return 0;
}

int *solve()
{
    int size=7;
    int arr[8] = {0, 1, 2, 3, 4, 5, 6, 7};
    permutation(arr, 0, size);

    return *results;
}


int combination_is_solution(int combination[8]) 
{
    int c=0;
    int r;
    int diags = 0;
    int antidiags = 0;
    int diag;
    int antidiag;

    for (c=0; c<8; c++)
    {
        r=combination[c];
        diag = DIAG(r,c);
        antidiag = ANTIDIAG(r,c);
        
        if (diags & (1<<diag)){
            return 0;
        }
        else {
            diags |= (1<<diag);
        }

        if (antidiags & (1<<antidiag)){
            return 0;
        }
        else {
            antidiags |= (1<<antidiag);
        }
    }

    return 1;
}

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}


void permutation(int *arr, int start, int end)
{
    if(start==end)
    {
        if (combination_is_solution(arr) == 1) {
            int z;
            for (z=0; z<8; z++) 
            {
                results[counter][z] = arr[z];
            }
            counter++;
        }

        return;
    }
    int i;
    for(i=start;i<=end;i++)
        {
            swap((arr+i), (arr+start));
            permutation(arr, start+1, end);
            swap((arr+i), (arr+start));
        }
}
