<img src="https://dm2302files.storage.live.com/y4mjoWpKezUd7ykYnOn2t6DRjIbYWcBHM85Ytuw7XSxiRSUEwiSvjuPRw7Me4ioJwJCbghN1JQuDwXuiCM0uV4m_KiIyj9LcX5rm_HwC460BlCQ03mfCqauISbZxpasUFIpxBafTRyPGfzznlUkoiZgARXGoEn7nbhmRUVd6kz94VRNTJ5JDej-kMzBZLaTk4RvAuTGb169kTLgN0TLsYe68w/cidades-coloridas_bo-kaap.png?psid=1&width=1024&height=418"></img>

# Finding opportunities to make better deals in the housing market


The CEO of House Rocket would like to maximize the company's revenue by finding better deals in the housing market.

The company's strategy is to buy houses in great locations with low prices and resell them later at higher prices. The higher the difference between buying and selling, the greater the company's profit and therefore increase your revenue.

QHowever, houses have many attributes that make them more or less attractive to buy and sell, and the location and period of the year can also influence prices.

To maximize revenue, the CEO believes that the following questions should be answered:

- Which houses the company should be purchase?

- With the house in company possession, what is the best moment to be sold, and for which price?

- The company should do a restoration to increase the price sale? What are the recommendations? For each restoration recommendation, how the price increases?


## _About the data_

The dataset that represents the context is available on the [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction). And contains house sale prices in King County, one of the 39 counties in Washington state.

_Disclaimer: the context presented, the company, the CEO, and the business questions are fictitious and exist only for the elaboration of a problem._

_* This project was suggested by [Meigarom Lopes](https://www.linkedin.com/in/meigarom) in your blog [sejaumdatascientist.com](https://sejaumdatascientist.com)_

## Solution steps
    -- C1. Understanding data (Finding data inconsistency and cleaning)
    -- C2. Feature engineering (New features that can be useful to data model)
    -- C3. Hypotheses
    -- C4. Exploratory Data Analysis
        -- Hypotheses validation
        -- Multivariate Analysis
    -- C6. Model Pipeline (Data obtaining until model training)

## Solution proposal
    -- 1. Table (House | Recommendation score)
    -- 2. Table (House | Sale date | Sale price) --> ML Model
    -- 3. Table (House | Improvements Features | Sale price correlation)

## To better visualization, look at:
- [__Exploratory Data Analysis__](https://nbviewer.jupyter.org/github/pcesar-costa/portfolio/blob/master/finding-opportunities-to-make-better-deals-in-the-housing-market/Exploratory%20Data%20Analysis.ipynb)
- [__Model pipeline__](https://nbviewer.jupyter.org/github/pcesar-costa/portfolio/blob/master/finding-opportunities-to-make-better-deals-in-the-housing-market/Model%20Pipeline.ipynb)
- [__Report__](https://datastudio.google.com/reporting/41facf33-e9c3-4b2f-8451-bcb136745a4a/page/IIchB)

## Summary of the conclusion by the analysis
<img src="https://0rtu3q.dm.files.1drv.com/y4mQ-GVlbNI1NFxNPuOE3kO8zLKhNs7wnbDnQYep8zKhBacdEXAKlh0-brIes4yPKJ7phoOKAQof3twEdLVv7lBTmO0zgzOAQEHW5951XsiWEhZIz8MKddAjrqXZGDfSskDGqOVjh8iFHGbRpMCvjZn5YB8bApHgitHkNRjeWhJcoGuqO4v6GfltV3Wj8PtlWJCBFnNbLYIA8m662wA9P63qg/Tomada-de-Decis%C3%B5es.png?psid=1"></img>

<br>

- __Which houses the company should be purchase?__

Among the issues raised for the purchase of property, the location, future market valuation, and other conditions of the property were taken into consideration, besides the time difference between the purchase and sale being as short as possible to reduce the effects of a property degradation.

Based on the analysis, it is possible to stipulate the cheapest and most expensive m² per region, with the Bellevue region showing benefit indications of purchase since it has one of the cheapest m² about the land space (which can build) and it has one of the most expensive living space, even though it is a place with a high standard (houses above 1M on average) the purchase with a future market valuation or a renovate has indications of profit.

About sectors that have an annual appreciation, Seattle is one of the highest. In this case, the purchase recommendation occurs for the South Zone, which has an appreciation close to the North sector, but with cheaper houses (indicating that there is inflation in the North sector). Besides these sectors, the next one is Bellevue, reinforcing the above argument about buying for return through an improvement. In the less valued zone per year (Preston), purchases are not recommended to annual appreciation, since it has a high price average. The difference in valuation between the South Seattle sector, with cheaper houses, may present a better deal since it is possible to achieve the same average values considering the valuation market, but with a much smaller investment.

In terms of the conditions of the property, the ones that present better deals to purchase are those with conditions 2 and 3, higher than this, the increase in price sale is not significant. In condition 3 are high price variance, so it is possible to sell houses in these conditions for an extended kind of customers. And condition 2 shows a significant drop in price sale and can offer a better deal to improvements since it has a concentration of price, therefore improving the condition will cover more customer profiles.

Besides, the view of houses can be relevant for customers, since views with waterfront are mostly overvaluing the house.

<br>

- __With the house in company possession, what is the best moment to be sold, and for which price?__

The data show us that the best selling period occurs in spring and winter, where there is also an increase in demand. In this period, houses can be sold on average for an amount above 3% per m². About a period in which demand is low,  the difference between these two periods can be on average 6% per m².

<br>

- __The company should do a restoration to increase the price sale? What are the recommendations? For each restoration recommendation, how the price increases?__

The improvement is interesting to increase the sale price, especially in houses that can be purchased with waterfront, since in these cases there is an overvaluation. In our analysis, it was possible to verify that in front of rivers and lakes, some houses were sold for relatively low prices, even though they have a quality of view 4 and are in sectors that are valued, such as Seattle. Among the attributes that can be classified for a restoration, such as the number of bathrooms, bedrooms, improvement in the condition, and the grade, the attribute that contributes the most is the grade, followed by the condition.