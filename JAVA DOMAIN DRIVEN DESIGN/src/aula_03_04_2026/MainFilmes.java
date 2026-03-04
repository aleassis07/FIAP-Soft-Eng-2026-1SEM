package aula_03_04_2026;

public class MainFilmes {
    public static void main(String [] args) {

        Filme filme1 = new Filme();
        filme1.nomeFilme = "Titanic";
        filme1.ano = 1997;
        filme1.nota = 10;
        filme1.duracao = 3;
        filme1.genero = "Drama";
        filme1.exibirInformacoes();
        System.out.println("\n");
        Filme filme2 = new Filme();
        filme2.nomeFilme = "Equilibrium";
        filme2.ano = 2002;
        filme2.nota = 8;
        filme2.duracao = 2;
        filme2.genero = "Ação, Suspense";
        filme2.exibirInformacoes();
    }
}
