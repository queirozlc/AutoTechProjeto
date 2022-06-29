from src.model.DAO.Connection import Connection


class CombustivelDAO(Connection):
    def __init__(self):
        Connection.__init__(self)

    # Método para inserir combustivel no banco de dados
    def insert(self, *args):
        try:
            sql = "INSERT INTO combustivel (descricao, quantidade, valor, observacao) VALUES (%s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro Inserido com Sucesso")
        except Exception as e:
            print("Erro ao inserir:", e)

    # Método para deletar combustivel do banco de dados por id
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM combustivel WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para remoção"

            sql_d = f"DELETE FROM combustivel WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro foi deletado com sucesso"
        except Exception as e:
            print("Erro ao deletar:", e)

    # Método para atualizar combustivel no banco de dados
    def update(self, id, *args):
        try:
            sql = f"UPDATE combustivel SET descricao = %s, quantidade = %s, valor = %s, observacao = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro Atualizado")
        except Exception as e:
            print("Erro ao atualizar:", e)

    # Método para selecionar todos os combustivel do banco de dados
    def select_all(self):
        return self.query("SELECT * FROM combustivel")

    # Método para procurar um combustivel no banco de dados
    def search(self, *args, type_s="id"):
        try:
            sql = "SELECT * FROM combustivel WHERE id = %s"
            if type_s == "descricao":
                sql = "SELECT * FROM combustivel WHERE descricao LIKE %s"

            data = self.query(sql, args)
            if data:
                return data

            return None
        except Exception as e:
            print("Erro ao encontrar o registro:", e)


if __name__ == "__main__":
    combustivel = CombustivelDAO()

    print(combustivel.select_all())