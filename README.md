Para executar a pipeline, siga estas etapas: 

Certifique-se de ter o Python instalado em seu sistema. 

Instale as bibliotecas necessárias para a pipeline. No terminal, navegue até o diretório raiz do projeto e execute o comando: pip install -r requirements.txt.

Execute o comando python run.py , certifique-se de estar no diretório correto. 
Alternativamente, você também pode executar a pipeline em qualquer IDE, abrindo o arquivo e executando-o diretamente.

###################################################################################################

Esta pipeline tem como objetivo consumir dados da API Dados Rio e gerar um relatório de mitigação de ocorrências da cidade, 
a pipeline está configurada para rodar de 20 em 20 minutos por 1 hora (3 requisições) , referente a CET-RIO. O resultado final é um arquivo CSV com as seguintes informações:

Data_Consulta_Api : Data e horário em que as ocorrências foram verificadas na API.

Tipo_De_Ocorrencia: Tipo da ocorrência observada.

Status: Status da ocorrência no horário observado.

Quantidade_De_Ocorrencias : Número de ocorrências neste status.

###################################################################################################

Funcionalidades de cada Script 

utils.py

  Importa o módulo prefect.
  
  Define a função log(message) que registra uma mensagem de log usando o logger do contexto do Prefect.

tasks.py:

  Importa os módulos e pacotes necessários, como StringIO, pandas, prefect, requests, datetime, timedelta, pytz, os.path e csv.
  
  Importa a função log do arquivo utils.

  Define a tarefa SCRIPT_ETL(), que realiza as seguintes etapas:
  
  Extração, verificando catch e log de erros. 
    
  Tratamento dos dados. 
    
  Carregamento dos dados em um arquivo Csv.
  
flows.py

  Importa os módulos Flow, datetime, timedelta e SCRIPT_ETL do arquivo tasks.
  
  Importa a classe IntervalSchedule do módulo prefect.schedules.
  
  Cria um objeto IntervalSchedule para agendar a execução do fluxo.
  
  Define um fluxo chamado 'Ocorrencias' com o agendamento definido anteriormente.
  
  Adiciona a tarefa SCRIPT_ETL() ao fluxo
