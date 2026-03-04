package aula_03_04_2026;

public class Filme {

    String nomeFilme;
    int ano;
    double nota;
    String genero;
    int duracao;

    public void exibirInformacoes() {
        System.out.println("=== INFORMAÇÕES DO FILME ===");
        System.out.println("Nome do filme: " + nomeFilme + "\n Ano do filme: " + ano + "\n Nota: " + nota + "\n Gênero: " + genero + "\n Duração total do filme: " + duracao + " horas (aprox.)");
    }



}
