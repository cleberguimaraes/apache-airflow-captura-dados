 Airflow Captura Dados

Este repositório contém um exemplo de código usando o Apache Airflow para capturar dados de uma API e processá-los de acordo com condições específicas. O fluxo de trabalho é definido usando a linguagem Python e utiliza operadores do Airflow para realizar tarefas e controlar o fluxo de execução.

Pré-requisitos

Antes de executar o código, certifique-se de ter instalado em seu ambiente:

- Apache Airflow
- Python 3.x
- Bibliotecas: pandas, requests, json

 Funcionalidade

O código realiza as seguintes etapas:

1. Captura de dados: Uma solicitação HTTP é feita para a URL "https://data.ny.gov/resource/kwxv-fwze.json" para obter os dados. Os dados JSON são convertidos em um DataFrame do Pandas e a quantidade de linhas é calculada.

2. Validação de dados: A quantidade de linhas obtida na etapa anterior é validada. Se a quantidade for maior que 100, o fluxo continua para a próxima etapa ("valido"). Caso contrário, o fluxo é desviado para a etapa "nvalido".

3. Tarefas "valido" e "nvalido": Essas tarefas simplesmente imprimem mensagens indicando se a quantidade de dados é considerada válida ou inválida.

4. Geração de arquivo CSV: Os dados obtidos na etapa de captura são novamente convertidos em um DataFrame do Pandas e salvos como um arquivo CSV no caminho "/home/dataset/dados.csv".

 Configuração do Airflow

O código utiliza o Airflow para agendar e executar as tarefas. Um fluxo de trabalho é definido usando a classe `DAG` do Airflow, com o nome "airflow_captura_dados". O fluxo é agendado para iniciar em 17 de julho de 2023, com um intervalo de agendamento de 30 minutos. O fluxo de trabalho não recupera tarefas atrasadas, pois `catchup` está definido como `False`.

 Executando o Código

Certifique-se de ter o Airflow configurado corretamente em seu ambiente antes de executar o código. Além disso, as bibliotecas Python mencionadas acima devem estar instaladas.

Para executar o código, siga as etapas abaixo:

1. Clone este repositório em seu sistema.

2. No diretório do projeto, instale as dependências executando o seguinte comando: `pip install -r requirements.txt`.

3. Inicie o Airflow e inicie o webserver e o scheduler.

4. Verifique se a configuração do Airflow está correta e os fluxos de trabalho estão sendo exibidos no painel do Airflow.

5. O código será executado de acordo com o agendamento definido no fluxo de trabalho. As mensagens de saída indicando o status da quantidade de dados serão exibidas no console do Airflow.

 Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou novos recursos para este projeto.

 Licença

Este projeto está licenciado sob a licença...