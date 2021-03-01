import abc


class FilaBase:

    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual = []

    def insere_cliente(self):
        self.fila.append(self.senha_atual)

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    def reseta_fila(self) -> None:
        if self.codigo >= 200:
            self.codigo = 0
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa):
        ...
