package aula_03_18_2026;

import java.util.Scanner;

public class CriarProdutos {
    public static void main(String [] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o nome do produto: ");
        String nome = scanner.nextLine();

        System.out.println("Digite o preço do produto: ");
        double preco = scanner.nextDouble();

        System.out.println("Digite a quantidade do produto: ");
        int quantidade = scanner.nextInt();

        System.out.println("Produto cadastrado com sucesso!");
        System.out.println("Nome: " + nome);
        System.out.println("Preço: " + preco);
        System.out.println("Quantidade: "+ quantidade);

        Produto produto1 = new Produto();
        produto1.exibirInformacoes();
    }

}

