<img src="https://static01.nyt.com/images/2019/12/17/books/review/17fatbooks/17fatbooks-mobileMasterAt3x.jpg" width="1000" height="325"></img>

# Coletando e estruturando dados para um sistema de recomendação de livros

A __Book Club__ é uma startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários, cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele não queira oferecer outro livro em troca.

A empresa deseja construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários, já que uma das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir o sistema de recomendação, é necessário coletar e armazenar os dados do site. Portanto, o objetivo será coletar e armazenar os seguintes dados:

- O nome do livro.
- A categoria do livro.
- O número de estrelas que o livro recebeu.
- O preço do livro.
- Se o livro está em Estoque ou não, e a quantidade

---
## Da arquitetura do fluxo

<img src="https://0rtj3q.dm.files.1drv.com/y4mqa46_aDV-8InnRTXdmUsSmAYhePXgduHby2WHwpg3Zxxk0_nyWzF7zJXLTfuJ02gfpPlWDSq59Xn7FsBAlwrLZxNVnlXMq15v-NwrG7IvEuyrrM4c_nxnwX_H_KndEVZ3DHXYyDqhesr5fCtX3YxFTzogd0B_AZ_Ctdpk68qWtG3w6ObGT1sJDz8sS4Q4blf0kKCpeumBiQmN7ojHFQeMg?width=3225&height=1013&cropmode=none"></img>

---

## Para executar esse código

Para a execução do código, basta clonar este repositório para dentro da pasta Home do Airflow (especificamente a pasta `dags`).

Para instalação do __Apache Airflow__:

> pip install apache-airflow

Além disso, será necessário uma instância do MongoDB (o [MongoAtlas](https://www.mongodb.com/cloud/atlas) oferece uma suite gratuita na nuvem).

Considerando que você já tem o Airflow instalado e configurado, acesse a pasta:

> dags > bookstoscrape 

e crie um arquivo `.env` com a URI e o nome do banco de dados do MongoDB, conforme arquivo `.env-example` de exemplo.

Depois de configurado o arquivo `.env`, basta iniciar o Airflow e o serviço de agendamento.

Após a primeira execução, ao verificar o banco de dados, terá algo semelhante ao `schema` abaixo:

<img src="https://0rtp3q.dm.files.1drv.com/y4meR6UO4QU50ZRTlaDAr5F4NKwb_NtatYskZwjHqDwCvVIT_XSJTnyZEPEG5HcVmX_htimzCPeN6h_Wuubik_hclc9_P0QGzXIMxGHH6tQxYPBXTROX3O6Vj-Ur4iQhD8-j0T5HvfIO4LSo8J1YRcSnYvOqdSvEp4xJufAymAMQE1c5MtBRcr9-fdmk01yiZuSKABzd_8IrswiKHvpT5flxA?width=1666&height=569&cropmode=none"></img>

<img src="https://0rto3q.dm.files.1drv.com/y4mYULsWmD1f0ByH_mq5BBvIVdD4eixST0S7B7YlNJoBMRezHdeilStqevBMb_rDiSW_e_jNsLT2dGflzaXrX62Ka80vacpu5NJr8nV5WPnCRnSY22zUSoPLF9uMvLAYuqvk42wvypTGnaemG7p_RDdfNg06CmzbVMJ7pEvK4kc1xi68aMagFaKID8FP1vW7sDvV8MNultat2INQcamZ_RqZA?width=1667&height=971&cropmode=none"></img>

---

## _Sobre os dados_

Os dados para serem coletados e armazenados estão disponíveis no site [books.toscrape.com](http://books.toscrape.com)

_Disclaimer: o contexto apresentado e a empresa são ficticios e existem somente para a elaboração de um problema._

_Nota: Este projeto foi sugerido por [Meigarom Lopes](https://www.linkedin.com/in/meigarom) em seu blog [sejaumdatascientist.com](https://sejaumdatascientist.com)_