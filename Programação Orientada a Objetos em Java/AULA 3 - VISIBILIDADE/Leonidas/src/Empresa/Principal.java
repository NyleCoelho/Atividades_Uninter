package Empresa;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {

		int valorCorreto = 10000;
		
		System.out.println("Digite seu palpite: ");
		Scanner teclado = new Scanner(System.in);
		int palpite = teclado.nextInt();
		
		while(palpite != valorCorreto) {
			if(palpite > valorCorreto) {
				System.out.println("Um pouco menos...");
			}
			else {
				System.out.println("Um pouco mais...");
			}
			
			System.out.println("Digite outro palpite");
			palpite = teclado.nextInt();
		}
		
		System.out.println("Parabens! vc acertou.");
		
	}

}
