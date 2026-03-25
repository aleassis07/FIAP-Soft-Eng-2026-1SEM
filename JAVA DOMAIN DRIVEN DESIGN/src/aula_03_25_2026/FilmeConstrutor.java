package aula_03_25_2026;

public class FilmeConstrutor {
    String titulo;
    String diretor;
    int anoLancamento;
    int duracao;

    public FilmeConstrutor(String titulo, String diretor, int anoLancamento, int duracao) {
        if (titulo == null || titulo.isBlank()) {
            throw new IllegalArgumentException(
                    "O título não pode ser vazio!"
            );
        }

        if (anoLancamento <= 1888) {
            throw new IllegalArgumentException(
                    "O ano de lançamento deve ser maior do 1888"
            );
        }

        if (duracao < 0) {
            throw new IllegalArgumentException();
        }

        this.titulo = titulo;
        this.diretor = diretor;
        this.anoLancamento = anoLancamento;
        this.duracao = duracao;
    }

    public FilmeConstrutor(int anoLancamento, int duracao) {
        if (anoLancamento <= 1888) {
            throw new IllegalArgumentException(
                    "O ano de lançamento deve ser maior do 1888!"
            );
        }

        if (duracao < 0) {
            throw new IllegalArgumentException(
                    "A duração do filme deve ser positiva!"
            );
        }

        this.anoLancamento = anoLancamento;
        this.duracao = duracao;
    }

}
