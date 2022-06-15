#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10
#define K 2*N

//this function computes the maximum number among num1, num2 and num3
int max3(int num1, int num2, int num3){
    if(num1>=num2 && num1>=num3) return num1;
    if(num2>=num1 && num2>=num3) return num2;
    if(num3>=num1 && num3>=num2) return num3;
}
//this function computes the maximum number between num1 and num2
int max2(int num1, int num2){
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
//the algorithm is order NlogN
int algorithm(int *arr,int lo,int hi,int *start,int *end, int *help_sum){
	int mid,left_max,right_max,i,j,sum,sta,en;
	sum=0;//current sum of the left side
	if(lo==hi){//if the array consists of only 1 element and if it's positive then it's the max if not the max is 0
		return max2(0,arr[lo]);
	}mid=(lo+hi)/2;//I divide the array in half so I can work each half array with less recursions
	left_max=0;//current max sum of the left half of the array
	for(i=mid;i>lo-1;i--){
		sum+=arr[i];//current sum of the left side up to the i element going backwards
		if (sum>left_max){//if the current sum is bigger than the current max then we replace the current max with the current sum
    		left_max=sum;//the maximum sum of the left half of the array
    		sta=i;//start of the subarray with the maximum sum of the left half of the array
    	}
	}
	right_max=0;//current max sum of the right half of the array
	sum=0;//current sum of the right side
	for(i=mid+1;i<hi+1;i++){
		sum+=arr[i];//current sum of the right side up to the i element going forward
		if (sum>right_max){//if the current sum is bigger than the current max then we replace the current max with the current sum
    		right_max=sum;//the maximum sum of the right half of the array
    		en=i;//end of the subarray with the maximum sum of the right half of the array
    	}
    }
    //help_sum holds the best possible sum so far, so in the end I can decide where is the beginning and ending of the subarray with the maximum sum
    if(left_max>=right_max && left_max>=(left_max+right_max)&&left_max>=*help_sum){//if the left part of the array has the maximum sum
    	*help_sum=left_max;
    	*start=sta;
    	*end=mid;
	}if(right_max>=left_max && right_max>=(left_max+right_max)&&right_max>=*help_sum){//if the right part of the array has the maximum sum
		*help_sum=right_max;
    	*start=mid+1;
    	*end=en;
	}if((left_max+right_max)>=right_max && (left_max+right_max)>=left_max&&(left_max+right_max)>=*help_sum){//if the combination of the left and right part of the array has the maximum sum
		*help_sum=left_max+right_max;
    	*start=sta;
    	*end=en;
	}
	return max3(left_max+right_max,algorithm(arr,lo,mid,start,end,help_sum),algorithm(arr,mid+1,hi,start,end,help_sum));//recursive algorithm
}//this function runs the algorithm and counts the time it needs to run
int main(int argc, char *argv[]) {
	int max_sum,help_sum=0,start=0,end=0,i;
	int *arr;
	arr=memory_allocate_function(N);//makes an array with random numbers between -100 and 100
	clock_t t0=clock();//starts counting the time it takes for the algorithm to run
	max_sum=algorithm(arr,0,N-1,&start,&end,&help_sum);//returns the maximum sum of the subarray
	clock_t t1=clock();//finds the time the algorithm ended
	printf("Array with %d elements:\n",N);
	for (i=0;i<N;i++){
		printf("%d ",arr[i]);	
	}printf("\n");
	printf("Maximum sum is %d, the subarray starts from the element in the position %d and ends with the element in the position %d and it took %.3f seconds for the algorithm to run.",max_sum,start+1,end+1,(double)(t1-t0)/CLOCKS_PER_SEC);
	free(arr);//freeing the space needed to store the elements of the array arr
	arr=memory_allocate_function(K);//makes an array with random numbers between -100 and 100
	clock_t t2=clock();//starts counting the time it takes for the algorithm to run
	max_sum=algorithm(arr,0,K-1,&start,&end,&help_sum);//returns the maximum sum of the subarray
	clock_t t3=clock();//finds the time the algorithm ended
	printf("\n\nArray with %d elements:\n",K);
	for (i=0;i<K;i++){
		printf("%d ",arr[i]);	
	}printf("\n");
	printf("Maximum sum is %d, the subarray starts from the element in the position %d and ends with the element in the position %d and it took %.3f seconds for the algorithm to run.",max_sum,start+1,end+1,(double)(t3-t2)/CLOCKS_PER_SEC);
	free(arr);//freeing the space needed to store the elements of the array arr
	return 0;
}
