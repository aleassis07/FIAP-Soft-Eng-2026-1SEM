package aula_03_02_2026;

public class MainProduto {
    public static void main(String[] args) {

        System.out.println("MainProduto");

        // Criando objetos
        Produto produto1 = new Produto();
        produto1.codigo = 10;
        produto1.nome = "Fandangos";
        produto1.preco = 4.99;
        produto1.tamanho = 1;
        produto1.peso = 0.50;
        produto1.estoque = 3;
        produto1.aumentarPreco(0.1);
        System.out.println("Preço atual do " + produto1.nome + ": " + "R$ " + produto1.preco);

        Produto produto2 = new Produto();
        produto2.codigo = 23;
        produto2.nome = "Pc Gamer Ryzen 7 32GB RAM 1TB";
        produto2.preco = 10000.00;
        produto2.peso = 1000.0;
        produto2.estoque = 5;
        produto2.diminuirPreco(2000);
        System.out.println("Preço atual do " + produto2.nome + ": " + "R$ " + produto2.preco);

        Produto produto3 = new Produto();
        produto3.codigo = 120;
        produto3.nome = "Playstation 5";
        produto3.preco = 4000;
        produto3.peso = 1000.0;
        produto3.diminuirPreco(2000);
        System.out.println("Preço atual do " + produto3.nome + ": " + "R$ " + produto3.preco);

    }
}
