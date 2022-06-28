from src.model.DAO.Connection import Connection


class ServicoDAO(Connection):
    def __init__(self):
        Connection.__init__(self)

    # Método para inserir posto no banco de dados
    def insert(self, *args):
        try:
            sql = "INSERT INTO servico (tipo, quantidade, valor, observacao, id_cliente, id_posto) VALUES (%s, %s, %s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro Inserido com Sucesso")
        except Exception as e:
            print("Erro ao inserir:", e)

    # Método para deletar posto do banco de dados por id
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM servico WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para remoção"

            sql_d = f"DELETE FROM servico WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro foi deletado com sucesso"
        except Exception as e:
            print("Erro ao deletar:", e)

    # Método para atualizar posto no banco de dados
    def update(self, id, *args):
        try:
            sql = f"UPDATE servico SET tipo = %s, quantidade = %s, valor = %s, observacao = %s, id_cliente = %s, id_posto = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro Atualizado")
        except Exception as e:
            print("Erro ao atualizar:", e)

    # Método para selecionar todos os posto do banco de dados
    def select_all(self):
        return self.query("SELECT * FROM servico")

    # Método para procurar um posto no banco de dados
    def search(self, *args, type_s="id"):
        try:
            sql = "SELECT * FROM servico WHERE id = %s"
            if type_s == "id_cliente":
                sql = "SELECT * FROM servico WHERE id_cliente = %s"

            elif type_s == "id_posto":
                sql = "SELECT * FROM servico WHERE id_posto = %s"

            data = self.query(sql, args)
            if data:
                return data

            return "Registro não encontrado"
        except Exception as e:
            print("Erro ao encontrar o registro:", e)

    # Método para retornar todas as informações necessárias para venda usando as tabelas relacionadas do banco
    def select_tabelas_relacionadas(self):
        try:
            sql = '''SELECT s.tipo, s.quantidade, s.valor, s.observacao, c.nome AS cliente_nome, c.cpf AS cliente_cpf, c.data_nascimento AS cliente_data_nascimento, c.endereco AS cliente_endereco, c.placa AS cliente_placa, p.nome AS posto_nome, comb.descricao AS combustivel_descricao, comb.quantidade AS combustivel_quantidade, comb.valor AS combustivel_valor, comb.observacao AS combustivel_observacao
                    FROM servico s
                    INNER JOIN cliente c ON c.id = s.id_cliente
                    INNER JOIN posto p ON p.id = s.id_posto
                    INNER JOIN combustivel comb ON comb.id = p.id_combustivel'''

            return self.query(sql)

        except Exception as e:
            return "Erro ao encontrar:", e


if __name__ == "__main__":
    pass
