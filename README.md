# Comparación de crypto monedas

## Introducción

Este proyecto realiza un análisis de los precios históricos de todas las crypto monedas disponibles en https://coinmarketcap.com/ con el objetivo de encontrar las que tienen un comportamiento similar al Bitcoin.
En primer lugar se consiguen mediante web scraping toda la información histórica disponible en coinmarketcap para todas las cryptomonedas, luego, se realiza un agrupamiento utilizando k-means.

## Motivación

Noté hace algún tiempo que las curvas del precio de Bitcoin y de Ethereum tenían una tendencia muy similar, como se ve en el gráfico. Esto me generó la inquietud de si había otras cryptomonedas en las que pase lo mismo, revisé manualmente algunas y vi varias coincidencias. En ese momento comencé a buscar la forma de poder detectar estas similitudes de forma automática para la mayor cantidad de monedas posibles. El objetivo en primer lugar era detectar si existía un desfase temporal entre las curvas con el fin de determinar si el resto de las monedas "seguían" al Bitcoin (o a otra moneda en particular) y de esta forma tener información de cómo se va a comportar el precio del resto en el futuro observando el comportamiento de esta moneda "testigo". Rapidamente encontré que al menos en la ventana temporal que tenía disponible, no existía tal moneda testigo. Sin embargo seguí con el análisis dado que creo que tener agrupadas las monedas de acuerdo a su comportamiento puede ser útil. Por el momento se me ocurren dos posibilidades: 1 - Aumentar el dataset disponible para predictores basados en redes neuronales. 2 - Si se logra predecir el comportamiento mediante cualquier técnica de alguna de las monedas se sabe que se puede esperar un comportamiento similar del resto.

## Herramientas utilizadas
Para la obtención de los precios históricos se utilizó Selenium. Para el modelo de k-means se utilizó tslearn, una librería basada en sklearn pero con herramientas agregadas para facilitar su implementación en series temporales. Para el análisis estadístico se utilizó la librería scipy. Para los gráficos, matplotlib y seaborn. Para el manejo del dataset Pandas.
