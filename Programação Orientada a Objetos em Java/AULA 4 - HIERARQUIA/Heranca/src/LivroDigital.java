public class LivroDigital extends Livro {
    public String linkDownload;
    public int tamanhoMB;

    public float imposto() {
        return 0.2f * lucro() + 2;
    }

    public float tamanhoPorPagina() {
        return tamanhoMB/(float)paginas;
    }
}
