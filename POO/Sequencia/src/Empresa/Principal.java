package Empresa;
import java.util.ArrayList;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite a qtd de nomes");
		ArrayList<String> listaNomes = new ArrayList<String>();
		int qtd = teclado.nextInt();
		
		for(int i=0; i<qtd ;i++) {
			String nome = teclado.next();
			listaNomes.add(nome);
		}
		
		for(int i=qtd-1; i>=0; i--) {
			System.out.println(listaNomes.get(i));
		}
		
		
	}

}
