package aula_03_18_2026;

import java.util.Scanner;

public class CriarProdutos {
    public static void main(String [] args) {

        Scanner scanner = new Scanner(System.in);

        // cadastro Produto1
        Produto produto1 =new Produto();

        System.out.println("Digite o nome do produto: ");
        produto1.nome = scanner.nextLine();

        System.out.println("Digite o preço do produto: ");
        produto1.preco = scanner.nextDouble();

        System.out.println("Digite a quantidade do produto: ");
        produto1.quantidade = scanner.nextInt();

        produto1.exibirInformacoes();
    }

}

