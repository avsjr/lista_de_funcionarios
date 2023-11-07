from flask import Flask, render_template, jsonify
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
    query = "SELECT razaosocial, nomefunc, descrcencus, descrfuncao, email, telefone FROM ad_plvsiramal"
    cursor.execute(query)

    data = {}  # Usamos um dicionário para representar as empresas
    for row in cursor:
        razaosocial, descrcencus, nomefunc, descrfuncao, email, telefone = row
        empresa = razaosocial
        departamento = descrcencus
        funcionario = {
            'Nome_Funcionario': nomefunc,
            'Cargo': descrfuncao,
            'Email': email,
            'Telefone': telefone
        }

        # Verificamos se a empresa já existe no dicionário
        if empresa not in data:
            data[empresa] = {}

        # Verificamos se o departamento já existe na empresa
        if departamento not in data[empresa]:
            data[empresa][departamento] = []

        # Adicionamos o funcionário ao departamento da empresa
        data[empresa][departamento].append(funcionario)

    # Feche a conexão com o banco de dados (deve estar fora do loop)
    cursor.close()
    connection.close()

    return render_template('index.html', data=data)
    #return jsonify(data)

if __name__ == '__main__':
    app.run()
