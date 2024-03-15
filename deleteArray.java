class DeleteArray{
	int[] delete(int arr[],int n, int x){
		//n as the size of element
		//x the number which we want to delete
		//i will work as index
		int i=0;
		for(i=0;i<n;i++){
			if(arr[i]==x){
			break;
			}
			else if(i==(n-1)){
			System.out.println(exit) ;
			}
		}
		for(int j=i;j<(n-1);j++){
			arr[j]=arr[j+1];
			return n-1;
		}
		return arr;
	}
	
	
	public static void main(String args[]){
		DeleteArray d= new DeleteArray();
		int arr[]={10,20,30,40,50};
		int res=d.delete(arr,5,30);
		System.out.println(res);
		int arr1[]=d.delete(arr,5,30);
		System.out.println(arr1);
	}

}



