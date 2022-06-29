from src.model.DAO.Connection import Connection


class PostoCombustivelDAO(Connection):
    def __init__(self):
        Connection.__init__(self)

    # Método para inserir posto no banco de dados
    def insert(self, *args):
        try:
            sql = "INSERT INTO posto_combustivel (id_posto, id_combustivel) VALUES (%s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro Inserido com Sucesso")
        except Exception as e:
            print("Erro ao inserir:", e)

    # Método para deletar posto do banco de dados por id
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM posto_combustivel WHERE id = {id}"
            if not self.query(sql_s):
                return None

            sql_d = f"DELETE FROM posto_combustivel WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro foi deletado com sucesso"
        except Exception as e:
            print("Erro ao deletar:", e)

    # Método para atualizar posto no banco de dados
    def update(self, id, *args):
        try:
            sql = f"UPDATE posto_combustivel SET id_posto = %s, id_combustivel = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro Atualizado")
        except Exception as e:
            print("Erro ao atualizar:", e)

    # Método para selecionar todos os posto do banco de dados
    def select_all(self):
        return self.query("SELECT * FROM posto_combustivel")

    # Método para procurar um posto no banco de dados
    def search(self, *args, type_s="id"):
        try:
            sql = "SELECT * FROM posto_combustivel WHERE id = %s"
            if type_s == "id_posto":
                sql = "SELECT * FROM posto_combustivel WHERE id_posto = %s"

            elif type_s == 'nome_combustivel':
                sql = '''SELECT p.id as posto_id, p.nome as posto_nome, c.id, c.descricao as combustivel_nome, c.quantidade as combustivel_quantidade, c.valor as combustivel_valor
                         FROM posto_combustivel pc
                         INNER JOIN posto p
                         ON p.id = pc.id_posto
                         INNER JOIN combustivel c 
                         ON c.id = pc.id_combustivel 
                         WHERE p.nome LIKE %s and c.descricao LIKE %s'''

            elif type_s == 'id_posto_combustivel':
                sql = ''' SELECT pc.id, p.nome, c.id, c.descricao as combustivel_nome, c.quantidade as combustivel_quantidade, c.valor as combustivel_valor
                          FROM posto_combustivel pc
                          INNER JOIN posto p
                          ON p.id = pc.id_posto
                          INNER JOIN combustivel c
                          ON c.id = pc.id_combustivel
                          WHERE pc.id_posto = %s and pc.id_combustivel = %s'''

            data = self.query(sql, args)
            if data:
                return data

            return None
        except Exception as e:
            print("Erro ao encontrar o registro:", e)

    # Método para retornar todas as informações necessárias para venda usando as tabelas relacionadas do banco
    def select_tabelas_relacionadas(self):
        try:
            sql = '''SELECT p.nome AS nome_posto, c.descricao AS combustivel_descricao, c.quantidade AS combustivel_quantidade, c.valor AS combustivel_valor, c.observacao AS combustivel_observacao
                    FROM posto_combustivel pc
                    INNER JOIN posto p 
                    ON p.id = pc.id_posto
                    INNER JOIN combustivel c
                    ON c.id = pc.id_combustivel'''

            return self.query(sql)

        except Exception as e:
            return "Erro ao encontrar:", e

    def buscar_combustivel_por_nome(self, *args, type_s="nome"):
        try:
            sql = '''SELECT c.descricao AS combustivel_nome, c.quantidade AS combustivel_quantidade, c.valor AS combustivel_valor
                     FROM posto_combustivel pc
                     INNER JOIN combustivel c
                     ON c.id = pc.id_combustivel
                     INNER JOIN posto p
                     ON p.id = pc.id_posto
                     WHERE p.nome = %s'''
            data = self.query(sql, args)

            if data:
                return data

            return None

        except Exception as e:
            return "Erro:", e


if __name__ == "__main__":
    posto = PostoCombustivelDAO()

    print(posto.buscar_combustivel_por_nome('Posto Ipiranga'))
