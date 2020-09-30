<img src="https://docs.google.com/uc?id=1oXlPBfpw1ZXhCX123o6PdshP02L0if9T"/>

# Collecting and structuring data for a book recommendation system

__Book Club__ is a book exchange startup. The business model works based on the exchange of books by users, each book registered, gives the right to exchange, however, the user can also buy the book, in case that does not want to offer another in exchange.

The company is still building your customer base and would like to improve the Recommendation System with data outside of your base so that it boosts the volume of exchanges and sales among users, as one of the most important mechanisms for this business monetize is the recommendation. An excellent recommendation improves the volume of trades and sales on the website.

To get the data it's needed, the company believes that a trusted website for extracting the information is `Bookstoscrape`, a website maintained by the community where readers make the recommendation through a rating, representing how much users liked and disliked the book.

After obtaining authorization for scraping, the company would like to collect and store the following data:

- The book name
- The category
- The number of stars the book received
- The book price

## Solution steps
    -- C1. Build the data collection process flow
    -- C2. Develop the web scraping script
    -- C3. Build the Airflow dags
    -- C4. Turn data available through an API

## Solution proposal
    -- 1. Data collection and storage by Airflow
    -- 2. An API to query the data
        -- by book name
        -- by category
        -- by range rating

---

## _Airflow architecture_

<img src="https://0rtj3q.dm.files.1drv.com/y4mqa46_aDV-8InnRTXdmUsSmAYhePXgduHby2WHwpg3Zxxk0_nyWzF7zJXLTfuJ02gfpPlWDSq59Xn7FsBAlwrLZxNVnlXMq15v-NwrG7IvEuyrrM4c_nxnwX_H_KndEVZ3DHXYyDqhesr5fCtX3YxFTzogd0B_AZ_Ctdpk68qWtG3w6ObGT1sJDz8sS4Q4blf0kKCpeumBiQmN7ojHFQeMg?width=3225&height=1013&cropmode=none"></img>

---

## To run this code
To run this code you'll need the Apache Airflow to schedule the scripts to collect and store the data in MongoDB and, Flask to make API requests.

The packages needed to Airflow are inside the `dags` folder (`Pipfile-Airflow`).
The packages needed to FlaskAPI are inside the `api` folder (`Pipfile`).

To install __Apache Airflow__:

> pip install apache-airflow

Besides, that will be necessary for a MongoDB instance (you can use [Mongodb Atlas](https://www.mongodb.com/cloud/atlas) that provides a free tier in the cloud).

Considering that you have Airflow installed and configured, go to the folder `dags > bookstoscrape` and create a file `.env` with MongoDB credentials, the example file is `.env-example`.

After that, just run Airflow and start the scheduled service.

In the first run, it expected that you have something like this in your MongoDB instance:

<img src="https://0rtp3q.dm.files.1drv.com/y4meR6UO4QU50ZRTlaDAr5F4NKwb_NtatYskZwjHqDwCvVIT_XSJTnyZEPEG5HcVmX_htimzCPeN6h_Wuubik_hclc9_P0QGzXIMxGHH6tQxYPBXTROX3O6Vj-Ur4iQhD8-j0T5HvfIO4LSo8J1YRcSnYvOqdSvEp4xJufAymAMQE1c5MtBRcr9-fdmk01yiZuSKABzd_8IrswiKHvpT5flxA?width=1666&height=569&cropmode=none"></img>

<img src="https://0rto3q.dm.files.1drv.com/y4mYULsWmD1f0ByH_mq5BBvIVdD4eixST0S7B7YlNJoBMRezHdeilStqevBMb_rDiSW_e_jNsLT2dGflzaXrX62Ka80vacpu5NJr8nV5WPnCRnSY22zUSoPLF9uMvLAYuqvk42wvypTGnaemG7p_RDdfNg06CmzbVMJ7pEvK4kc1xi68aMagFaKID8FP1vW7sDvV8MNultat2INQcamZ_RqZA?width=1667&height=971&cropmode=none"></img>

## Sending API Requests

To sending requests through API, install the API `pipenv` packages and run the file `server.py`. The authentication token it's provided from the route: `/token`

Although that, you can access the data through my API deployed in a free dyno in Heroku:

__root url__: 

    bookscrape.api.pedro-costa.wtf

__routes__:
    
    /token
    return an Authorization Token to send in the request header

    /books
    return a book list with query parameters informed
    Query Parameters: 
        title: Book title
        category: Book category

    /bookstars
    return a book list between a <min> and <max> value of star rating
    Query Parameters: 
        min: Minimum value for star rating
        max: Maximum value for star rating

---

## _About the data_

The data collected and stored is available on the website [books.toscrape.com](http://books.toscrape.com)

_Disclaimer: the context presented, the company, the CEO, and the business questions are fictitious and exist only for the elaboration of a problem. The website was developed and made available on purpose for web scraping._

_* This project was suggested by [Meigarom Lopes](https://www.linkedin.com/in/meigarom) in your blog [sejaumdatascientist.com](https://sejaumdatascientist.com)_