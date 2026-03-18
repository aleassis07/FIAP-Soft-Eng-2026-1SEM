package aula_03_18_2026;

import java.util.Scanner;

public class ExemploScanner {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.println("Digite sua idade: ");
        int idade = scanner.nextInt();

        System.out.println("Ola, " + nome + " você tem " + idade + " anos.");
    }
}


