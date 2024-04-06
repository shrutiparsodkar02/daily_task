class Swap{
	/*private int num1;
	private int num2;
	private int temp;
	public void setvalues(int n1,int n2,int temp1){
		this.num1=n1;
		this.num2=n2;
		this.temp=temp1;
	} 
	public int getvalues_n1(){
		return num1;
		}
	public int getvalues_n2(){
		return num2;
		}
	//public int getvalues_temp(){
		//return temp;
		//}*/
	public void swaping_No(int num1,int num2){
		int temp=num1;
		num1=num2;
		num2=temp;
		System.out.println("num1-->"+num1);
		System.out.println("num2-->"+num2);	
	}
}
class swaping{
	public static void main (String args[]){
		int num1=10,num2=20;
		Swap s1=new Swap();
		System.out.println("num1-->"+num1);
		System.out.println("num2-->"+num2);
		s1.swaping_No(10,20);
		
		System.out.println("num1-->"+num1);
		System.out.println("num2-->"+num2);
		//s1.swaping_No();
	
		}
		
		
}
