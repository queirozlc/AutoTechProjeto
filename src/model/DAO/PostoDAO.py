from src.model.DAO.Connection import Connection


class PostoDAO(Connection):
    def __init__(self):
        Connection.__init__(self)

    # Método para inserir posto no banco de dados
    def insert(self, *args):
        try:
            sql = "INSERT INTO posto (nome, id_combustivel) VALUES (%s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro Inserido com Sucesso")
        except Exception as e:
            print("Erro ao inserir:", e)

    # Método para deletar posto do banco de dados por id
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM posto WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para remoção"

            sql_d = f"DELETE FROM posto WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro foi deletado com sucesso"
        except Exception as e:
            print("Erro ao deletar:", e)

    # Método para atualizar posto no banco de dados
    def update(self, id, *args):
        try:
            sql = f"UPDATE posto SET nome = %s, id_combustivel = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro Atualizado")
        except Exception as e:
            print("Erro ao atualizar:", e)

    # Método para selecionar todos os posto do banco de dados
    def select_all(self):
        return self.query("SELECT * FROM posto")

    # Método para procurar um posto no banco de dados
    def search(self, *args, type_s="id"):
        try:
            sql = "SELECT * FROM posto WHERE id = %s"
            if type_s == "nome":
                sql = "SELECT * FROM posto WHERE nome LIKE %s"

            data = self.query(sql, args)
            if data:
                return data

            return "Registro não encontrado"
        except Exception as e:
            print("Erro ao encontrar o registro:", e)

    # Método para retornar todas as informações necessárias para venda usando as tabelas relacionadas do banco
    def select_tabelas_relacionadas(self):
        try:
            sql = '''SELECT p.nome, c.descricao AS combustivel_descricao, c.quantidade AS combustivel_quantidade, c.valor AS combustivel_valor, c.observacao AS combustivel_observacao
                    FROM posto p
                    INNER JOIN combustivel c ON c.id = p.id_combustivel'''

            return self.query(sql)

        except Exception as e:
            return "Erro ao encontrar:", e


if __name__ == "__main__":
    pass
