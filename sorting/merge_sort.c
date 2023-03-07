// https://www.programiz.com/dsa/merge-sort
// psuedocode: CLRS 4e

#include<stdio.h>

void merge(int A[], int p, int q, int r);
void merge_sort(int A[], int p, int r);
void print_array(int A[], int n);

int main()
{
    int arr[] = {43, 5, 39, 33, 90, 22, 30, 32, 44, 53};
    int n = sizeof(arr) / sizeof(arr[0]);

    merge_sort(arr, 0, n-1);
    print_array(arr, n);

    return 0;
}

void merge_sort(int A[], int p, int r)
{

    if (p>=r)
    {
        return ;
    }
    int q = p + (r-p) / 2;          // midpoint

    merge_sort(A, p, q);
    merge_sort(A, q+1, r);

    merge(A, p, q, r);
}

void merge(int A[], int p, int q, int r)
{
    // length for new arrays
    int n_L = q-p+1;        // length of A[p: q]
    int n_R = r-q;          // length of A[q+1: r]

    // new arrays
    int L[n_L];             // L[0: n_L-1]
    int R[n_R];             // R[0: n_R-1]

    // copying elements of A[p:q] into L
    for (int i = 0; i < n_L; i++)
    {
        L[i] = A[p+i];
    }
    // copying elements of A[q+1:p] into R
    for (int j = 0; j < n_R; j++)
    {
        R[j] = A[q+j+1];
    }

    // indexes
    int i=0;    // i index the smallest remaining element in L
    int j=0;    // j index the smallest remaining element in R
    int k=p;    // k index the location in A to fill

    // As long as each of the arrays L and R contains an unmerged element,
    // copy the smallest unmerged element back into A[p:r].
    while (i < n_L && j < n_R)
    {
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            i++;
        }
        else
        {
            A[k] = R[j];
            j++;
        }
        k++;
        
    }
    
    // Having gone through one of L and R entirely, copy the
    // remainder of the other to the end of A[p:r].
    while (i < n_L) 
    {
        A[k] = L[i];
        i++;
        k++;
    }

    while (j < n_R) 
    {
        A[k] = R[j];
        j++;
        k++;
    }
}

void print_array(int A[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d  ", A[i]);
    }
    printf("\n");
}
