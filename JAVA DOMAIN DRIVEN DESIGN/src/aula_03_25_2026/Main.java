package aula_03_25_2026;

public class Main {
    public static void main(String[] args) {
        FilmeConstrutor titanicSimples = new FilmeConstrutor(1997, 1);
        FilmeConstrutor titanicCompleto = new FilmeConstrutor("James Cameron", "Teste", 1997, 6 );
        System.out.println(titanicCompleto.diretor);
    }
}
