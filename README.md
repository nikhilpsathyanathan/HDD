# Deep Scan

<img src="https://github.com/nikhilpsathyanathan/HDD/blob/master/screenshots/home.png" width="100%" height="50%">

Deep scan is an ML-based analytic tool that would help you to predict your disk drives before it fails.

#### New Features!
  - intelligent prediction
  - Better analytics 
  - Interactive web App


### Tech 

Deep Scan uses a number of open source projects to work properly:

* [Flask] - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
* [Bulma] - Free, open source, & modern CSS framework based on Flexbox.
* [python] - Python is a programming language that lets you work quickly
and integrate systems more effectively.

And of course Deep Scan itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Deep Scan requires [python] 3.x to run.

Install the dependencies and packages and start the server.

```sh
$ cd HDD
$ pip3 install -r requirement.txt
$ python3 server.py
```

The train.csv should be the root directory and call before server starts

### Test data pre-processing

```sh
python3 train_preprocess.py 
```

### Python packages used
Deep Scan need following packages to star run.

| Package | Description |
| ------ | ------ |
| Numpy | [NumPy is the fundamental package for scientific computing with Python][pk1] |
| Pandas | [Easy-to-use data structures and data analysis tools for the Python][pk2] |
| scikit-learn | [Simple and efficient tools for data mining and data analysis][pk3] |
| Flask | [Flask is a microframework for Python based on Werkzeug][pk4] |




   [dill]: <git@github.com:nikhilpsathyanathan>
   [git-repo-url]: <git@github.com:nikhilpsathyanathan/HDD.git>
   [bulma]: <https://bulma.io/>
   [Flask]: <http://flask.pocoo.org/>
   [python]: <https://www.python.org/>

   [Pk1]: <http://www.numpy.org>
   [pk2]: <https://pandas.pydata.org/>
   [pk3]: <https://scikit-learn.org/stable/>
   [pk4]: <http://flask.pocoo.org/>
