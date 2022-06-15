#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10
#define K 2*N

//this function computes the maximum number between num1 and num2
int max(int num1, int num2){
    return (num1 > num2 ) ? num1 : num2;
}
//this function initializes an  array with random numbers between -100 and 100
int* memory_allocate_function(int n){
	int i;
	int *arr=(int *) malloc(n*sizeof(int));
	if (arr==NULL){
		printf("Can't allocate memory'");//either an error occured or there isn't enough space in the memory
		exit(1);
	}srand(1066581); //I set the seed as my AM
	for(i=0;i<n;i++){
		arr[i]=rand()%201-100; // I create an array whose elements are random numbers between -100 and 100
	}
	return arr;
}
//this function finds the beginning and end of a subarray that contains the elements of the array with the maximum sum and also computes the maximum sum
//the algorithm is order N
int algorithm(int *arr,int *start,int *end,int n){
	int k,l,maxi;
	int current_sum[n+1];
	maxi=0;//current maximum sum is zero
    current_sum[0]=0;//setting the first element of the current sum to zero
    for (k=0;k<n;k++){
    	current_sum[k+1] = max(0, current_sum[k] + arr[k]);//computing the sum of elements of the array k so far and if it's negative we set it to zero
    	if(maxi<current_sum[k+1]){//if the sum of the elements of the subarray is bigger than the current maximum sum then we change the value of the current maximum sum to that of the subarray
    		maxi =current_sum[k+1];//setting the current maximum sum of the array
    		*end=k;//setting the ending of the subarray
		}
	}for(l=*end;l>=0;l--){//computing the beginning of the subarray
		if(current_sum[l]==0){//starting from the end of the subarray and going backwards we find the first element that has the value zero in the current sum and the beginning of the subarray is the element after it
			*start=l;//setting the beginning of the subarray
			break;
		}
	}
	return maxi;
}
//this function runs the algorithm and counts the time it needs to run
int main(int argc, char *argv[]) {
	int max_sum,start=0,end=0,i;
	int *arr;
	arr=memory_allocate_function(N);//makes an array with random numbers between -100 and 100
	clock_t t0=clock();//starts counting the time it takes for the algorithm to run
	max_sum=algorithm(arr,&start,&end,N);//returns the maximum sum of the subarray
	clock_t t1=clock();//finds the time the algorithm ended
	printf("Array with %d elements:\n",N);
	for (i=0;i<N;i++){
		printf("%d ",arr[i]);	
	}printf("\n");
	printf("Maximum sum is %d, the subarray starts from the element in the position %d and ends with the element in the position %d and it took %.3f seconds for the algorithm to run.",max_sum,start+1,end+1,(double)(t1-t0)/CLOCKS_PER_SEC);
	free(arr);//freeing the space needed to store the elements of the array arr
	arr=memory_allocate_function(K);//makes an array with random numbers between -100 and 100
	clock_t t2=clock();//starts counting the time it takes for the algorithm to run
	max_sum=algorithm(arr,&start,&end,K);//returns the maximum sum of the subarray
	clock_t t3=clock();//finds the time the algorithm ended
	printf("\n\nArray with %d elements:\n",K);
	for (i=0;i<K;i++){
		printf("%d ",arr[i]);	
	}printf("\n");
	printf("Maximum sum is %d, the subarray starts from the element in the position %d and ends with the element in the position %d and it took %.3f seconds for the algorithm to run.",max_sum,start+1,end+1,(double)(t3-t2)/CLOCKS_PER_SEC);
	free(arr);//freeing the space needed to store the elements of the array arr
	return 0;
}

