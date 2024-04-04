import locale
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        ativo_1 = float(''.join(filter(str.isdigit, request.form['valor_casa']))) / 100
        ativo_2 = float(''.join(filter(str.isdigit, request.form['valor_imovel']))) / 100
        ativo_3 = float(''.join(filter(str.isdigit, request.form['valor_veiculos']))) / 100
        ativo_4 = float(''.join(filter(str.isdigit, request.form['valor_investimentos']))) / 100
        ativo_5 = float(''.join(filter(str.isdigit, request.form['outros_ativos']))) / 100

        passivo_1 = float(''.join(filter(str.isdigit, request.form['valor_hipoteca']))) / 100
        passivo_2 = float(''.join(filter(str.isdigit, request.form['valor_carro']))) / 100
        passivo_3 = float(''.join(filter(str.isdigit, request.form['valor_estudante']))) / 100
        passivo_4 = float(''.join(filter(str.isdigit, request.form['valor_dividas']))) / 100
        
        total_ativos = ativo_1 + ativo_2 + ativo_3 + ativo_4 + ativo_5
        total_passivos = passivo_1 + passivo_2 + passivo_3 + passivo_4

        patrimonio_liquido = total_ativos - total_passivos
        res = 'positivo' if patrimonio_liquido > 0 else 'negativo'        
        
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        patrimonio_formatado = locale.currency(patrimonio_liquido, grouping=True, symbol=None)
        
        return render_template('resultado.html', patrimonio=patrimonio_formatado, res=res)

if __name__ == '__main__':
    app.run(debug=True)