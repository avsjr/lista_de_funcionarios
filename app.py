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
    query = "SELECT razaosocial, descrcencus, nomefunc, descrfuncao, email, telefone FROM ad_plvsiramal"
    cursor.execute(query)

    
    # Usamos uma lista para representar a árvore de empresas, departamentos e funcionários
    tree = []

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

        # Verificamos se a empresa já existe na árvore
        try:
            empresa_index = int(empresa)
        except ValueError:
            continue
    
        # Verificamos se a empresa já existe na árvore
        empresa_index = int(empresa)
        empresa_node = tree[empresa_index]
        
        # Verificamos se o departamento já existe na empresa
        departamento_node = next((node for node in empresa_node['departamentos'] if node['departamento'] == departamento), None)

        if departamento_node is None:
            # Se o departamento não existe, adicionamos o departamento à empresa
            departamento_node = {'departamento': departamento, 'funcionarios': []}
            empresa_node['departamentos'].append(departamento_node)

        # Adicionamos o funcionário ao departamento
        departamento_node['funcionarios'].append(funcionario)

    # Feche a conexão com o banco de dados
    cursor.close()
    connection.close()

    return render_template('index.html', tree=dict(tree))

if __name__ == '__main__':
    app.run()
