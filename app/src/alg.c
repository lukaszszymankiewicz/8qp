# include <stdio.h>
# include <string.h>

#define DIAG(r, c) (r+c)
#define ANTIDIAG(r, c) (8+c-r-1)

int *solve();
void next_perm(int * ap, int len);
void swap_elements(int * ap, int a, int b);
int combination_is_solution(int combination[]);
int factorial(int n);

int results[92][8] = { 0 };

int *solve()
{
    memset(results, 0, sizeof(results[0][0]) * 8 * 92);

    int counter = 0;
    int n = 8;
    int perm[] = {0, 1, 2, 3, 4, 5, 6, 7};

    for (int i=0; i<factorial(n)-1; i++){
        next_perm(&perm[0], n);

        if (combination_is_solution(perm) == 1){
            for (int z=0; z<8; z++) {
                results[counter][z] = perm[z];
            }
            counter++;
        }
    }
    return *results;
}

void next_perm(int * ap, int len) {
    int k = 0;
    int l = 0;

    // Find the largest index k such that a[k] < a[k + 1].
    for (int i=0; i<len-1; i++){
        if ( *(ap+i) < *(ap+i+1) ){
            k = i;
        }
    }

    // Find the largest index l greater than k such that a[k] < a[l].
    for (int j=k; j<len; j++){
        if ( *(ap+k) < *(ap+j) ){
            l = j;
        }
    }

    // Swap the value of a[k] with that of a[l].
    swap_elements(ap, k, l);

    // Reverse the sequence from a[k + 1] up to and including the final element a[n].
    for (int z=0; k+1+z < len-1-z; z++){
        swap_elements(ap, (k+1)+z, (len-1)-z);
    }
}

int combination_is_solution(int combination[8]) 
{
    int c=0;
    int r;
    int antidiags = 0;
    int diags = 0;
    int diag, antidiag;

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

void swap_elements(int * ap, int a, int b){
    int temp = *(ap + a);
    *(ap + a) = *(ap + b);
    *(ap + b) = temp;
}

int factorial(int n){
    int res = 1;

    for (int i=2; i<n+1; i++){
        res *= i;
    }
    return res;
}

