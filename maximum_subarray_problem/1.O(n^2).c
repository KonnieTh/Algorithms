#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10
#define K 2*N

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
//the algorithm is order N^2
int algorithm(int *arr,int *start,int *end, int n){
	int help_arr[n+1],j,k,l,subarray_sum,maxi;
	help_arr[0]=0;//setting the first element of the "helping" array to zero
	for(l=1;l<n+1;l++){
		help_arr[l]=help_arr[l-1]+arr[l-1];//setting each element of the "helping" array as the sum of the elements of the arr up to this element
	}
	maxi=0;//current maximum sum is zero
	for(j=0;j<n;j++){
		for(k=j;k<n;k++){
			subarray_sum=help_arr[k+1]-help_arr[j];//computing the subarray sum of elements by subtracting the element in the position k+1 of the "helping" array with the element in the position j of the "helping" array
			if(subarray_sum>maxi){//if the sum of the elements of the subarray is bigger than the current maximum sum then we change the value of the current maximum sum to that of the subarray
				maxi=subarray_sum;//setting the current maximum sum of the array
				*start=j;//setting the beginning of the subarray
				*end=k;//setting the ending of the subarray
			}
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

