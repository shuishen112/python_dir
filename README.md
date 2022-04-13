<!--
 * @Author: your name
 * @Date: 2022-04-13 10:01:02
 * @LastEditTime: 2022-04-13 10:06:39
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: /python_dir/README.md
-->

## python dir problems

```
.
├── README.md
├── dir_one
│   ├── __init__.py
│   └── module1.py
├── dir_two
│   ├── __init__.py
│   └── module2.py
└── module_test.py
```

As shown above. The module2 whats use the function in module1.py

There are two method to implement it. 

1. add sys.path in module2.py

```
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dir_one.module1 import my_print

```

2. use the python -m . Note that if we want to use python -m, we should add __init__.py file in each dir so that the python can make this dir a module. 

```
python -m dir_two.module2
```

Note that there is not .py 