import os
#目录内容,自动递归,无需改动
Dirinfo={}
#(子)文件夹递归
Pathx=''
y=0
def analysis(Path=None):
    global Dirinfo
    Dirinfo={}
    if Path==None:
        print('[Err]在分析时出现错误:未传入文件夹路径')
    if not os.path.exists(Path):
        print('[Err]在分析'+Path+'时出现错误:文件(夹)不存在或无法访问')
        return
    Dirinfo[Path]={}
    try:
        TempDir=os.listdir(Path)
    except:
        print('Access Denied.')
    Dirinfo[Path]={}
    Dirinfo[Path]['Dir']=[]
    Dirinfo[Path]['File']=[]
    #先定义Dirinfo,预防在空文件(夹)时报错 
    for x in TempDir:
        TempPath=os.path.join(Path,x)   
        if os.path.isdir(TempPath):
            Dirinfo[Path]['Dir'].append(x)
        elif os.path.isfile(TempPath):
            Dirinfo[Path]['File'].append(x)
        #文件分类
    #print('在'+Path+'中发现'+str(len(Dirinfo[Path]['Dir']))+'个目录,'+str(len(Dirinfo[Path]['File']))+'个文件')
        #对于找到的子目录,进行同样的操作(也就是说 对于找到的子目录的子目录也会递归 子目录的子目录的子目录......)
#加载文件夹
#主程序
Unchanged=False
def explore():
    global y
    global Pathx
    global Dirinfo
    global Unchanged
    global Root
    if Unchanged==False:
        Root=Pathx
    Pathx=str(input('>'))
    if Pathx=='.':
        Pathx,tmp=os.path.split(Root)
        print(Pathx)
        analysis(Pathx)
        show()
    try:
        if int(Pathx)>y:
            os.popen(os.path.join(Root,Dirinfo[Root]['File'][int(Pathx)-1-y]))
            Unchanged=True
            Pathx=Root
            show()
        else:
            Pathx=os.path.join(Root,Dirinfo[Root]['Dir'][int(Pathx)-1])
    except:
        print('Error Occured.')
    if Unchanged==False:
        analysis(Pathx)
        show()
    Unchanged=False
def show():
    global Dirinfo
    global Pathx
    global y
    os.system('cls')
    print('SuExplorer:'+Pathx)
    #print(Dirinfo)
    for x in range(len(Dirinfo[Pathx]['Dir'])):
        print(str(x+1)+':'+Dirinfo[Pathx]['Dir'][x]+'\\')
        y=x+1
    for x in range(len(Dirinfo[Pathx]['File'])):
        print(str(x+1+y)+':'+Dirinfo[Pathx]['File'][x])
    explore()
Pathx=str(input('Enter your root folder >'))
if not os.path.exists(Pathx):
    print('[Err]Location Not Found.')
else:
    analysis(Pathx)
    print('SuExplorer:'+Pathx)
    print(Dirinfo)
    for x in range(len(Dirinfo[Pathx]['Dir'])):
        print(str(x+1)+':'+Dirinfo[Pathx]['Dir'][x]+'\\')
        y=x+1
    for x in range(len(Dirinfo[Pathx]['File'])):
        print(str(x+1+y)+':'+Dirinfo[Pathx]['File'][x])
    explore()
os.system('pause')
