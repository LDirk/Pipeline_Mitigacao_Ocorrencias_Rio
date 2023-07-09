Para executar a pipeline, siga estas etapas: 

Certifique-se de ter o Python instalado em seu sistema. 

Instale as bibliotecas necessárias para a pipeline. No terminal, navegue até o diretório raiz do projeto e execute o comando: pip install -r requirements.txt.

Execute o comando python run.py , certifique-se de estar no diretório correto. 
Alternativamente, você também pode executar a pipeline em qualquer IDE, abrindo o arquivo e executando-o diretamente.
###################################################################################################

Esta pipeline tem como objetivo consumir dados da API Dados Rio e gerar um relatório de mitigação de ocorrências da cidade, 
a pipeline está configurada para rodar de 20 em 20 minutos por 1 hora , referente a CET-RIO. O resultado final é um arquivo CSV com as seguintes informações:

Data_Consulta_Api : Data e horário em que as ocorrências foram verificadas na API.
Tipo_De_Ocorrencia: Tipo da ocorrência observada.
Status: Status da ocorrência no horário observado.
Quantidade_De_Ocorrencias : Número de ocorrências neste status.
