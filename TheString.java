/counts words ands consonants

import java.util.Scanner;

public class TheString {
	String str;
	int len,wordcount,cons,vow;
	TheString(){
		 str = "";
		 len = 0;
		 wordcount = 0;
		 cons= 0;
	}
	TheString(String ds){
		str = ds;
	}
	 void count() {
		char ch;
		str=str+' ';
		len = str.length();
		for(int i =1;i<len;i++) {
			ch = str.charAt(i);
			if (ch == ' ') {
				wordcount++;
			}
			else if("AEIOUaeiou".indexOf(ch)>=0) {
				vow++;
				//continue;
			}
			else {
				cons++;
			}
		}
	}
	 void display() {
		System.out.println(wordcount);
		System.out.println(cons);
		System.out.println(vow);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		TheString ob = new TheString(s);
		ob.count();
		ob.display();
		
	}

}
