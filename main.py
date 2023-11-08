from flask import Flask, render_template
import cx_Oracle
from itertools import groupby

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
    query = "SELECT razaosocial, descrcencus, nomefunc, descrfuncao, email, telefone FROM ad_plvsiramal"
    cursor.execute(query)
    data = cursor.fetchall()

    # Criar uma lista de dicionários com os dados extraídos
    result = []
    for row in data:
        result.append({
            'empresa': row[0],
            'departamento': row[1],
            'nome_funcionario': row[2],
            'cargo': row[3],
            'email': row[4],
            'telefone': row[5]
        })
        
    # Feche a conexão com o banco de dados 
    cursor.close()
    connection.close()
    
    # Agrupar os dados por empresa e departamento
    dados_agrupados = []
    dados_ordenados = sorted(result, key=lambda x: (x['empresa'], x['departamento']))

    current_empresa = None
    current_departamento = None
    empresa_departamento = None

    for data in dados_ordenados:
        empresa = data['empresa']
        departamento = data['departamento']

        if empresa != current_empresa:
            if empresa_departamento is not None:
                dados_agrupados.append(empresa_departamento)
            
            current_empresa = empresa
            empresa_departamento = {
                "empresa": empresa,
                "departamentos": []
            }

        if departamento != current_departamento:
            current_departamento = departamento
            empresa_departamento['departamentos'].append({
                "departamento": departamento,
                "funcionarios": [data]
            })
        else:
            empresa_departamento['departamentos'][-1]['funcionarios'].append(data)

    if empresa_departamento is not None:
        dados_agrupados.append(empresa_departamento)
        
    return render_template('index.html', dados=dados_agrupados)

if __name__ == '__main__':
    app.run()
