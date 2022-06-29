from src.model.Cliente import Cliente
from src.model.DAO.Connection import Connection


class ClienteDAO(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO cliente (nome, cpf, data_nascimento, endereco, placa) VALUES (%s, %s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro Inserido com Sucesso")
        except Exception as e:
            print("Erro ao inserir:", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM cliente WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para remoção"

            sql_d = f"DELETE FROM cliente WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro foi deletado com sucesso"
        except Exception as e:
            print("Erro ao deletar:", e)

    def select_all(self):
        return self.query("SELECT * FROM cliente")

    def update(self, id, *args):
        try:
            sql = f"UPDATE cliente SET nome = %s, cpf = %s, data_nascimento = %s, endereco = %s, placa = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro Atualizado")
        except Exception as e:
            print("Erro ao atualizar:", e)

    def search(self, *args, type_s="cpf"):
        sql = "SELECT * FROM cliente WHERE cpf LIKE %s"
        if type_s == "id":
            sql = "SELECT * FROM cliente WHERE id = %s"
        elif type_s == "placa":
            sql = "SELECT * FROM cliente WHERE placa LIKE %s"

        elif type_s == "nome":
            sql = "SELECT * FROM cliente WHERE nome LIKE %s"

        data = self.query(sql, args)
        if data:
            return data

        return None


if __name__ == "__main__":
    cliente = ClienteDAO()

    cliente.delete(9)