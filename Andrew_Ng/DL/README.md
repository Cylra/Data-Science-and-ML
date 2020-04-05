**这个文件夹下是对吴恩达老师的《深度学习》学习的编程作业**

老师的课程质量确实相当高，由于时间精力有限，不敢保证能快速学完吴老师的课程，而每月支付Coursera $49/月的课程费用对我而言还是有点勉强，故而使用线下模式自学，此处是个人对吴老师课程学习后，对其编程作业的提交，作为对自己所学知识的一个检验。

在我不知道何时学习(争取一年以内)结束后，保证到Coursera上注册课程并支付$49的费用，以示支持。

如果违反了Coursera的规则，请联系我 (287168219@qq.com) 删除。

本来想将编程作业翻译成中文的，但是许多地方翻译成中文意思不能特别准确的表达，想查英文原词以了解更多时，也不方便，而且吴老师作业的英文已经算特别简单了，都读下去也没有许多生僻单词，遂作罢。

### 编程作业中过时的函数调用及bug

编程作业使用Python3完成，但原始作业中部分调用函数已失效，导致运行时报错，需要修改，在我提交的作业本中已进行了修改并顺利运行，下面仅对错误之处进行记录，具体解决办法进入相应的ipynb文件查询:
- L1W2 (2020.03.31)  
作业2中，由于scipy库版本的更新，作业中使用的[imread][5]、[imresize][6]已弃用]
- L1W3 (2020.04.02)  
 plt.scatter的微小改版，给函数传参稍有变化，需要修改planar_utils.py文件和作业中相关函数进行修改，并要重启内核，重新导包，否则修改不生效
- L1W4 (2020.04.02)  
 作业2中，imread、imresize已弃用
 - L2W1 (2020.04.03)  
 作业1、2中，plt.scatter的微小改版
  - L2W2 (2020.04.04)  
 作业中，plt.scatter的微小改版，4 - Adam处第一次出现的公式参数有误，s_corrected的计算应除以${1 - (\beta_2)^t}$
  - L2W3 (2020.04.05)  
 作业中，scipy库的更新


### 参考资料:  

   - [理论作业题目][1]  
      备注：理论作业部分答案貌似有误，还是需要参考[黄博士][2]的答案
   - [编程作业题目][2] ipython notebook空白作业来自于[黄博士][2]
   - [编程作业答案][3]
   - [吴恩达Deeplearning第二课代码bug修正大全][4]


[1]: https://www.kesci.com/home/project/5e20243e2823a10036b542da/code
[2]: https://github.com/fengdu78/deeplearning_ai_books
[3]: https://www.kesci.com/home/project/5de4787aca27f8002c4c3661
[4]: https://blog.csdn.net/skylark0924/article/details/80322165
[5]: https://blog.csdn.net/WUDIxi/article/details/100059943
[6]: https://blog.csdn.net/WUDIxi/article/details/100060055