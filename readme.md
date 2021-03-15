# 文本识别

1. 安装python环境
    ```shell script
    conda create -n ocr python=3.7
2. 安装paddlehub
    ```shell script
    
    #需要将PaddleHub和PaddlePaddle统一升级到2.0版本
    !pip install paddlehub==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple 
    !pip install paddlepaddle==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple 
    
    #该Module依赖于第三方库shapely、pyclipper，使用该Module之前，请先安装shapely、pyclipper
    !pip install shapely -i https://pypi.tuna.tsinghua.edu.cn/simple 
    !pip install pyclipper -i https://pypi.tuna.tsinghua.edu.cn/simple 
  
3. 样例
    ```
   https://aistudio.baidu.com/aistudio/projectdetail/507159
   ```