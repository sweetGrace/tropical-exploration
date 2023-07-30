# Tropical代数特性探究

tropical文件夹下包含相关实验执行文件和所使用的工具类。

## 目录

- tropical
	- [algebra](#algebra)
	- [matrix](#matrix)
	- [ov_scheme](#ov_scheme)
  
### algebra

定义了有限域和tropical域两个代数类。

### matrix

探究tropical矩阵下的不动点特性。

>使用说明:

>tropical_matrix.ipynb中包含find_fixed_vector(*args)函数和Analysis_Tropical_Matrix类find_fixed_vector(*args)用于求解给定系数矩阵和列向量的不动点，详细数据会被保存在 data/ProcessDetail 中。Analysis_Tropical_Matrix()类中的analysis_of_given_matrix(*args)函数用于求解给定系数矩阵，遍历范围下的所有列向量的不动点的统计特性，详细数据会被保存在 data/Analysis 中。运行文件中最后两个代码块即可分别运行以上两个功能。

### ov_scheme
探究tropical域上的油醋多变量密码体制特性。

>使用说明:

>ov_scheme.ipynb中定义了油醋签名的验证过程，以及相关参数的生成函数，运行最后两个代码块，分别完全随机的系数矩阵下的统计特性以及对给定的单一系数矩阵的统计特性。
