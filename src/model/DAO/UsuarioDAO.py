from src.model.DAO.Connection import Connection


class UsuarioDAO(Connection):
    def __init__(self):
        Connection.__init__(self)

    # Método para inserir usuario no banco de dados
    def insert(self, *args):
        try:
            sql = "INSERT INTO usuario (nome, cpf, senha, data_nascimento, endereco, nivel_acesso) VALUES (%s, %s, %s, %s, %s, %s)"
            self.execute(sql, args)
            self.commit()
            print("Registro Inserido com Sucesso")
        except Exception as e:
            print("Erro ao inserir:", e)

    # Método para deletar usuario do banco de dados por id
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM usuario WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para remoção"

            sql_d = f"DELETE FROM usuario WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro foi deletado com sucesso"
        except Exception as e:
            print("Erro ao deletar:", e)

    # Método para atualizar usuario no banco de dados
    def update(self, id, *args):
        try:
            sql = f"UPDATE usuario SET nome = %s, cpf = %s, senha = %s, data_nascimento = %s, endereco = %s, nivel_acesso = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro Atualizado")
        except Exception as e:
            print("Erro ao atualizar:", e)

    # Método para selecionar todos os usuarios do banco de dados
    def select_all(self):
        return self.query("SELECT * FROM usuario")

    # Método para procurar um usuario no banco de dados
    def search(self, *args, type_s="cpf"):
        sql = "SELECT * FROM usuario WHERE cpf LIKE %s"
        if type_s == "id":
            sql = "SELECT * FROM usuario WHERE id = %s"
        elif type_s == "nome":
            sql = "SELECT * FROM usuario WHERE nome LIKE %s"
        elif type_s == "nivel_acesso":
            sql = "SELECT * FROM usuario WHERE nivel_acesso LIKE %s"
        elif type_s == "senha":
            sql = "SELECT * FROM usuario WHERE senha LIKE %s"

        data = self.query(sql, args)
        if data:
            return data

        return None


if __name__ == "__main__":
    usuario = UsuarioDAO()
