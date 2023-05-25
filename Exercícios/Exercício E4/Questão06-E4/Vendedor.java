public class Vendedor extends Pessoa {
    private String cpf;
    private double percentualComissao;

    // Construtor
    public Vendedor(String nome, String telefone, String cpf, double percentualComissao) {
        super(nome, telefone);
        this.cpf = cpf;
        this.percentualComissao = percentualComissao;
    }

    // Getters e Setters para os atributos específicos
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public double getPercentualComissao() {
        return percentualComissao;
    }

    public void setPercentualComissao(double percentualComissao) {
        this.percentualComissao = percentualComissao;
    }
}
