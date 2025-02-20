package Empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		int idade = 10;
		idade = idade + 2;
		String nome = "Linda";
		
		double peso = 72.5;

		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Digite sua idade");
		idade = teclado.nextInt();
		
		System.out.println("Digite seu peso");
		peso = teclado.nextDouble();
		
		System.out.println("Digite seu nome");
		nome = teclado.next();
		
		System.out.println("idade:" + idade);
		System.out.printf("peso:%.2f\n",peso);
		System.out.printf("nome " + nome);
		
		if(idade <18) {
			System.out.println("Acesso bloqueado");
		}
		else if(idade <65) {
			System.out.println("Adulto");
		}
		else {
			System.out.println("idoso");
		}
		
		for(int i=0; i<10; i++) {
			System.out.println("Valor: " + i);
		}
		
		//array
		int megaSena[] = {11, 34, 64, 65, 34, 43, 67};
		megaSena[0] = 43; 
		
		int numeros[] = new int[200];
		numeros[60] = 50;
		
		

	}

}
