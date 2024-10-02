# RAD-Python
Repositório para o projeto da matéria de Desenvolvimento Rápido de Aplicações em Python

# Sobre o projeto
Estou desenvolvendo um sistema de gerenciamento de proponentes para a associação em que eu trabalho. Proponentes são possíveis associados que estão no "radar" da associação, eles já tiveram contato de alguma forma com os divulgadores da associação e demonstraram interesse em se associar. Eles fazem um pré cadastro com todos os dados e valor da contribuição associativa, nesse caso eles ficam no sistema de prospecção e serão contatados para fechar o contrato.

# Como rodar o projeto
Esse projeto utiliza o streamlit como interface gráfica, então a biblioteca dele precisa ser instalada no seu computador. É simples, só utilizar esse comando no terminal do visual studio code: pip install streamlit. Após tudo ser instalado é só abrir o prompt de comando, utilizar o comando cd seguido pelo diretório onde a pasta do projeto está localizada e em seguida rodar o comando: streamlit run main.py. Também é necessário importar o arquivo do banco de dados para o seu gerenciador de databases, ele fica na pasta services com o nome "crud_python.d"
