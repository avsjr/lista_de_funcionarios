from flask import Flask, render_template, request
import cx_Oracle

app = Flask(__name__)

# Configurações do banco de dados Oracle
username = 'sankhya'
password = 'q4l8s5m4'
tns_name = '(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=oraclesrv.platinacsc.com.br)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=orcl)))'

@app.route('/')
def index():
    # Conecta ao banco de dados Oracle
    connection = cx_Oracle.connect(username, password, tns_name)
    cursor = connection.cursor()

    # Execute a consulta SQL na sua view de funcionários
    query = "SELECT razaosocial, nomefunc, descrcencus, descrfuncao, email, telefone FROM ad_plvsiramal;"
    cursor.execute(query)

    # Recupere os dados e organize-os de acordo com a estrutura desejada
    data = []
    for row in cursor:
        razaosocial, descrcencus, nomefunc, descrfuncao, email, telefone = row
        # Crie um dicionário com os campos desejados
        record = {
            'Nome_Empresa': razaosocial,
            'departamento': descrcencus,
            'Nome_Funcionario': nomefunc,
            'Cargo': descrfuncao,
            'Email': email,
            'Telefone': telefone
        }
        data.append(record)

    # Feche a conexão com o banco de dados
    cursor.close()
    connection.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
