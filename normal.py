from filabase import FilaBase


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'NM{self.codigo}'


    def chama_cliente(self, caixa):
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, digija-se ao caixa: {caixa}"