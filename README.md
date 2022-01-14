# infolib
#### _simple and complete PandasDataframe's stat overview_
![PyPI - Status](https://img.shields.io/pypi/status/infolib) ![Build Status](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue) ![PyPI - Downloads](https://img.shields.io/pypi/dm/infolib?color=green)

## Installation

Only through pip at this time
https://test.pypi.org/project/infolib/

```sh
pip install -i https://test.pypi.org/simple/ infolib
```
```sh
from infolib.infolib import inf
```
## How to use

Using infolib is very simple:
```sh
inf(pd.DataFarame)
```
inf() takes 1 positional argument and expects pandas DataFrame object

## Exemple

```sh
# series that will be part of the dataframe
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
i = [1,2,3]
f = [0.123,423.231,0.002]
c = ['A', 'B', 'C']
cn = [1, 2, 3]
b = [False, True, False]
n = [np.nan, np.nan, np.nan]

# import as pandas.Dtaframe
test = pd.DataFrame({"A": s, "B": td, "C": i, "D":f, "E":c, "F":cn, "G":b, "H":n})

# transformation of two features as categories
test['E'] = test_03['E'].astype('category')
test['F'] = test_03['F'].astype('category')
```

```sh
# run infolib
inf(test)
```

![Infolib output](https://raw.githubusercontent.com/AntonelloManenti/infolib/main/tests/output_infolib.PNG)

## Development Status

Read well and don't say you didn't know.

|| Status|
| ------ |------ |
| ✔️| Planning|
| ✔️| Pre-Alpha|
| ✔️| Alpha|
| ❌|Beta
| ❌ |Production/Stable |
|❌|Mature|
|❌|Inactive|

The alpha version was tested in Colab (py 3.7)
and on Jupyter (py 3.10 on Windows)


#### Demo
[Demo on Colab]


## License

[MIT]

## Contacts

[linkedin]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Demo on Colab]: <https://colab.research.google.com/drive/1KTI7CwP_E7IJod_WiD0PT31MaRBdhiki?usp=sharing>
   [MIT]:<https://github.com/AntonelloManenti/infolib/blob/main/LICENSE>
   [linkedin]:<https://www.linkedin.com/in/antonello-manenti/>
