package aula_03_02_2026;

public class TiposPrimitivos {
    public static void main (String[] args) {

        int idadePrimitiva = 20;
        System.out.println("idadePrimitiva: " + idadePrimitiva);

        Integer idadeWrapper = null;
        System.out.println("idadeWrapper: " + idadeWrapper);

        // verificar tamanho máximo do Integer
        System.out.println("Max int: " + Integer.MAX_VALUE);
        System.out.println("Min int: " + Integer.MIN_VALUE);

        // int suporta até 2.146.483.647
        // int populacaoMundo = 8000000000; # ERRO

        // se usar long, usa "L" no final do número
        long numero = 30000000000L;
        System.out.println("número: " + numero);

        double d = 10.0;
        System.out.println("d = " + d);
        System.out.println("0.0 / 0.0 = " + (0.0 / 0.0)); // NÃO DÁ ERRO = retorna NaN, por causa do double = casas decimais

        int dez = 10;
        System.out.println("10 / 10 é igual a " + dez / 10); // ERRO: não é possível dividir por 0 = erro lógico = por causa do int
    }
}
