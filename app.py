from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# BANCO DE DADOS EM PYTHON (Estrutura profissional de metadados)
CONTEUDO_CURSOS = {
    "tecnologia": [
        {
            "id": 101,
            "nome": "CS50: Introduction to Computer Science",
            "plataforma": "Harvard University (edX)",
            "duracao": "12 semanas (6-18h/sem)",
            "idioma": "Inglês (Legendas PT-BR)",
            "certificado": "Gratuito / Pago (Opcional)",
            "link": "https://edx.org",
            "descricao": "O maior e mais famoso curso de fundamentos de programação, algoritmos, C, Python e SQL do mundo."
        },
        {
            "id": 102,
            "nome": "Python for Everybody Specialization",
            "plataforma": "University of Michigan (Coursera)",
            "duracao": "Aproximadamente 2 meses",
            "idioma": "Inglês (Legendas PT-BR)",
            "certificado": "Grátis via Auxílio Financeiro",
            "link": "https://coursera.org",
            "descricao": "Do absoluto zero às estruturas de dados e tratamento de arquivos web utilizando a linguagem Python."
        }
    ],
    "negocios": [
        {
            "id": 201,
            "nome": "Google Digital Marketing & E-commerce",
            "plataforma": "Google Career Certificates",
            "duracao": "Aproximadamente 3 meses",
            "idioma": "Inglês / Português",
            "certificado": "Grátis via Auxílio Coursera",
            "link": "https://coursera.org",
            "descricao": "Aprenda SEO, anúncios digitais, e-mail marketing e métricas avançadas com os especialistas do Google."
        },
        {
            "id": 202,
            "nome": "Financial Markets",
            "plataforma": "Yale University (Coursera)",
            "duracao": "33 horas",
            "idioma": "Inglês (Legendas PT-BR)",
            "certificado": "Grátis via Auxílio Financeiro",
            "link": "https://coursera.org",
            "descricao": "Visão geral das ideias, métodos e instituições que permitem à sociedade humana gerenciar riscos e promover empreendimentos."
        }
    ],
    "design": [
        {
            "id": 301,
            "nome": "Google UX Design Professional Certificate",
            "plataforma": "Google (Coursera)",
            "duracao": "Aproximadamente 6 meses",
            "idioma": "Inglês (Legendas PT-BR)",
            "certificado": "Grátis via Auxílio Coursera",
            "link": "https://coursera.org",
            "descricao": "Fundamentos de pesquisa de usuário, wireframes, protótipos de alta fidelidade e testes de usabilidade no Figma."
        }
    ]
}

# ROTAS DA API REST
@app.route('/')
def home():
    # Renderiza o arquivo HTML separado que ficará na pasta templates
    return render_template('index.html')

@app.route('/api/cursos', methods=['GET'])
def obter_cursos():
    categoria = request.args.get('categoria', 'tecnologia')
    dados_categoria = CONTEUDO_CURSOS.get(categoria, [])
    return jsonify(dados_categoria)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
