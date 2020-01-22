本repo从https://github.com/deepmind/rc-data fork而来。

deepmind提供了一份数据集,且提供了生成这份数据集的脚本。使用该脚本不一定能顺利地生成这份数据集,原因1:waybackmachine不稳定;原因2:需要翻墙.

因此https://cs.nyu.edu/~kcho/DMQA/ 提供了生成后的数据集。

https://cs.stanford.edu/~danqi/data/cnn.tar.gz在https://cs.nyu.edu/~kcho/DMQA/的基础上做了小小的处理。


mkdir ~/data/rc-data
cd ~/data/rc-data
wget https://github.com/deepmind/rc-data/raw/master/generate_questions.py
wget https://storage.googleapis.com/deepmind-data/20150824/data.tar.gz -O - | tar -xz --strip-components=1

会生成目录
~/data/rc-data/cnn
~/data/rc-data/cnn/downloads
~/data/rc-data/cnn/entities
~/data/rc-data/cnn/questions  //qa任务主要使用这个目录
~/data/rc-data/cnn/stories
~/data/rc-data/cnn/tokens

`~/data/rc-data/dailymail`与`~/data/rc-data/cnn`类似

// conda remove -n rc-data --all
~/anaconda3/bin/conda create -n rc_data python=2.7 # 避免与旧的环境rc-data重名
source ~/anaconda3/bin/activate
conda activate rc_data

wget https://github.com/deepmind/rc-data/raw/master/requirements.txt
pip install -r requirements.txt # lxml3.3.3报错了
pip install lxml
//Successfully installed lxml-4.4.2;--mode=generate 不需要用到lxml 
pip uninstall lxml
// install lxml 3.3.3
// conda install -c anaconda gcc
// pip install -r requirements.txt
// 这两行解决不了install lxml 3.3.3
// sudo apt-get install libxml2-dev libxslt-dev # 这需要root 权限

// conda install -c anaconda lxml=3.3.3 # 找不到


// conda install -c anaconda lxml
// lxml-4.4.2
// https://anaconda.org/search?q=lxml
// 找个最接近的3.3.5
// https://anaconda.org/chuongdo/lxml
conda install -c chuongdo lxml

//Traceback (most recent call last):
//  File "generate_questions.py", line 32, in <module>
//    from lxml import html
//  File "/home/dff/anaconda3/envs/rc_data/lib/python2.7/site-packages/lxml/html/__init__.py", line 42, in <module>
//    from lxml import etree
#ImportError: libxslt.so.1: cannot open shared object file: No such file or directory

// 还是有问题。
conda uninstall lxml
conda install -c anaconda lxml
// conda install lxml 有问题...................

pip install lxml
// lxml-4.4.2 貌似可以正常使用
// 在requirements.txt里注释掉lxml所在的行
pip install -r requirements.txt
python generate_questions.py --corpus=cnn --mode=download
// 大概有9w+url下载失败,可以重新执行上一行命令再次尝试下载.不过这个数据集目前来说是不如natural questions的，不值得花太多时间去深究。
// 实际上url的总共数目就是9w+,所有的url都需要翻墙。
#http://web.archive.org/web/20100329110846id_/http://www.cnn.com:80/2010/WORLD/meast/01/17/iraq.aziz.hospitalized/index.html
// wget http://web.archive.org/web/20100329110846id_/http://www.cnn.com:80/2010/WORLD/meast/01/17/iraq.aziz.hospitalized/index.html ;无法成功
//pip install shadowsocks
python generate_questions.py --corpus=dailymail --mode=download

python generate_questions.py --corpus=cnn --mode=generate
wget https://github.com/deepmind/rc-data/raw/master/expected_cnn_test.txt
comm -3 <(cat expected_cnn_test.txt) <(ls cnn/questions/test/)


python generate_questions.py --corpus=dailymail --mode=generate
#comm -3 <(cat expected_[cnn/dailymail]_test.txt) <(ls [cnn/dailymail]/questions/test/)

不打算在dailymail上复现

####update

从https://cs.nyu.edu/~kcho/DMQA/上下载生成后的数据集
解压缩后目录结构如下
cnn/questions/training/*.question
cnn/questions/validation/*.question
cnn/questions/test/*.question
cnn/wayback_test_urls
cnn/wayback_training_urls
cnn/wayback_validation_urls
把这些目录/文件覆盖掉
~/data/rc-data/cnn/questions/training
~/data/rc-data/cnn/questions/validation
~/data/rc-data/cnn/questions/test
~/data/rc-data/cnn/wayback_test_urls
~/data/rc-data/cnn/wayback_training_urls
~/data/rc-data/cnn/wayback_validation_urls

dailymail数据集与cnn的操作类似,同样覆盖一遍。

生成cdq所用的数据集可参考如下脚本:
https://blog.csdn.net/ChenS27/article/details/99673661
或
https://github.com/theblackcat102/rc-cnn-dailymail/blob/master/README.md
https://github.com/theblackcat102/rc-cnn-dailymail/blob/master/code/utils.py#L12


整理为post_process.py

`python post_process.py`
