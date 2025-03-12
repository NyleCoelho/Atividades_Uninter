public class Livro {
    public String autores;
    public float custoProducao;
    public float precoVenda;
    public String titulo;
    public int paginas;

    public float lucro() {
        return precoVenda - custoProducao;
    }

    public void imprimirTitulo() {
        System.out.println("O titulo: " + titulo);
    }

    public float imposto() {
        return 0.2f * lucro();
    }

}
