# Detecting COVID-19 in X-ray

<img src="https://docs.google.com/uc?id=1_8T8NAlzpyhk_M_hydFntzc3ajFxrGHO" />

__Quasix__ is a company that had your contracts canceled after the pandemic and decided to turn your attention to fighting the new coronavirus. The company already worked in the medical field with Artificial Intelligence, assisting in the prognosis of lung diseases and various types of pneumonia.

Because of the change in the landscape, the company wants to create a model to detect coronavirus infections, identifying signs of the disease from chest X-rays that will provide savings in the use of test kits and made use of typical resources in hospitals: the machines X-ray.

For the detection of infected patients, the company relies on your team of data scientists to provide a reliable model for early detection in COVID-19 diagnostics.

# Solution steps

    -- C1. Loading and shuffling the data
        -- Sample of X-ray images from pacients tested positive for COVID-19
        -- Sample of X-ray images from healthy patients (normal)
    -- C2. Data wrangling
        -- 1. Normalize to datagen
        -- 2. Transform target into keras binary
        -- 3. Splitting into training and test dataset
        -- 4. Data augmentation in the train set
    -- C3. Configuring transfer learning
    -- C4. Create and training the CNN model
    -- C5. Evaluate the model

# Solution proposal
    -- A ML classification model that provides COVID-19 diagnosis from chest X-ray images
    -- A Streamlit application to make the predictions

# How could COVID-19 be detected in X-ray images?

At the beginning of the pandemic, tests were currently hard to come by — there were not enough of them and couldn't manufacture fast, which was causing panic.

COVID-19 tests, such as RT-PCR, are the most suitable for diagnosis because they confirm whether the patient has the virus or not. However, imaging analysis shows the severity of COVID-19, such as how much it's affecting the lung and how. Being a useful tool to help to differentiate from other diseases that have the same symptom.

# Available on web

The project was deployed using the `Streamlit|Docker` and can be accessed at:

### [__Streamlit App:__ Detecting COVID-19 in X-ray images](https://cutt.ly/quasix-app) *

 * if the application is sleeping, can take a few minutes to go up

# About the data

The datasets that represent the context was obtained from:

* [COVID-19 image data collection](https://github.com/ieee8023/covid-chestxray-dataset)

* [Chest xray pneumonia, ]('https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia')

# References
[[1] Detecting covid 19 in x-ray images, Adrian Rosebrock](https://www.pyimagesearch.com/2020/03/16/detecting-covid-19-in-x-ray-images-with-keras-tensorflow-and-deep-learning/)

[[2] Radiology data collection and preparation for artificial intelligence, Håvard Jenssen](https://medium.com/@hbjenssen/covid-19-radiology-data-collection-and-preparation-for-artificial-intelligence-4ecece97bb5b)

[[3] Detecting covid 19 induced pneumonia from chest-x-rays, Adrian Yijie Xu](https://towardsdatascience.com/detecting-covid-19-induced-pneumonia-from-chest-x-rays-with-transfer-learning-an-implementation-311484e6afc1)