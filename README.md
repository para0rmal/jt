[![version](https://img.shields.io/badge/Version-1.0-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/para0rmal/jt.svg?branch=master)](https://travis-ci.com/para0rmal/jt)


# jt

jt is a command line utility which allows you to visualise JSON schemas as text trees. It may be used as a complement to `jq`, to facilitate the interpretation of a JSON schema, prior to defining filters.

Note: At this point it assumes consistency across data contained in arrays and only evaluates the schema of the first element.

Installation
---


Clone the repository:
```
$ git clone https://github.com/para0rmal/jt.git
```

Enter directory:
```
$ cd jt/
```

#### A) Virtual Environment Installation

You may use the `pipenv` virtual environment manager from PyPy. 

Install `pipenv`:
```
$ pip3 install pipenv
```

Install `jt` within a virtual environment using `pipenv`:
```
$ pipenv --python 3.6 install -e .
```

Activate the virtualenv (deactivate with `exit`):
```
$ pipenv shell
```


#### B) Local Installation

Install locally:
```
$ python3 setup.py install
```

Examples
---

#### View help:
![image](https://user-images.githubusercontent.com/15225347/76718203-def4dd00-672d-11ea-88ac-1a240d62883d.png)

#### Read JSON from stream:
![jt-json](https://user-images.githubusercontent.com/15225347/76711660-c5419e80-6709-11ea-8b03-0795f107a9c1.png)

#### Read YAML from stream:
![jt-yaml](https://user-images.githubusercontent.com/15225347/76711659-c4a90800-6709-11ea-908f-5699c0b17308.png)

