### 面向饼服的ONGEKI b45查分器

小孩子不懂事写着玩的，不包含r10的计算因为我不知道咋写而且很粗糙，凑合看吧

#### 查分步骤

找一个有控制台的浏览器(Chrome, Edge)等，访问u.otogame.net并登录

以Chrome为例，按F12打开控制台，选择“网络”，在筛选器中选择"Fetch/XHR"

![](.\assets\1.png)

在饼服面板中点击“音击-乐曲信息”，注意到浏览器控制台中出现"playlog"请求

![](.\assets\2.png)

单击playlog，在“标头”中向下滚动找到"请求标头"中的"Authorization"字段，复制该字段内容

![](.\assets\3.png)

在查分器所在文件夹中新建"Authorization.txt"文件(注意大小写)，将复制的内容粘贴进去，保存并关闭文件

在终端中运行"python ONGEKIprobe.py"，等待至输出"Finish"则成绩记录已获取并保存在"ongeki.csv"中

输出"Error:token is invalid"：Authorization会不定时刷新，刷新网页并重新复制一次可解决

#### b45计算与可视化

定数信息位于"ongeki_music.csv"文件，需要更新时可在终端中运行"python ONGEKILevelProbe.py"

在终端中运行"python ONGEKIb45Calculator.py"，可进行rating的计算，计算结果将分别保存在各个csv文件中

输入"python -m http.server:8080"并运行，然后在浏览器中访问"localhost:8080"即可查看b45表格
