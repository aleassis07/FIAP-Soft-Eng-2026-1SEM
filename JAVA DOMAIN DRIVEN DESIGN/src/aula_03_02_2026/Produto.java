package aula_03_02_2026;

public class Produto {

    // Atributos
    String nome;
    double preco;
    int codigo;
    int tamanho;
    int estoque;
    double peso;

    // Métodos
    public void aumentoPreco(double preco) {
        this.preco += preco;

        System.out.println("Preço aumentado com sucesso! " + this.preco);
    }

    public void diminuirPreco(double preco) {
        this.preco -= preco;

        System.out.println("Preço diminuído com sucesso! " + this.preco);
    }
}
