package aula_03_02_2026;

public class MainProduto {
    public static void main(String[] args) {

        System.out.println("MainProduto");

        // Objeto
        Produto produto1 = new Produto();

        produto1.codigo = 10;
        produto1.nome = "Fandangos";
        produto1.preco = 4.99;
        produto1.tamanho = 1;
        produto1.peso = 0.50;
        produto1.estoque = 3;

        produto1.aumentoPreco(0.1);

    }

    Produto produto2 = new Produto();

    Produto produto3 = new Produto();
    System.out.println("produto3 - " + produto3.codigo);
}
