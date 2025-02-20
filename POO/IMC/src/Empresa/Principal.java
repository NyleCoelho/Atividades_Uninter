package Empresa;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		System.out.println("Bem vindo a calculadora de IMC!");
		
		System.out.println("Digite seu peso");
		Scanner teclado = new Scanner(System.in);
		int peso = teclado.nextInt();
		
		System.out.println("Digite sua altura");
		Scanner teclado1 = new Scanner(System.in);
		double altura = teclado1.nextDouble();
		
		double imc = peso / (altura * altura);
		System.out.printf("Seu imc: %.2f", imc);
	}
	

}
