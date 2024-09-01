
def test(param):
    """
    函数说明
    :param param:
    :return: void
    """
    msg = input('请输入：')
    print(param, msg)
    return


def test1():
    """
    for else  List（列表）
    """
    sites = ["1", "2", "3", "4"]
    for site in sites:
        if site == "3":
            print("截断条件成立")
            break
        print("循环数据 " + site)
    else:
        print("没了!")
    print("完成循环!")
    return


def test2():
    """
    for key in a  == for key in a.keys()  字典(dictionary)
    """
    mp = {'a': '1', 'b': '2', 'c': '3'}
    for key in mp:
        print(key, mp[key])
    return


def test3():
    mp = {'a': '1', 'b': '2', 'c': '3'}
    for value in mp.values():
        print(value)
    return


def test4():
    # 输出元组
    mp = {'a': '1', 'b': '2', 'c': '3'}
    for item in mp.items():
        print(item)
    return


def test5():
    """
    key,value == (key,value)
    :return:
    """
    mp = {'a': '1', 'b': '2', 'c': '3'}
    for key, value in mp.items():
        print(key, value)
    return

def test6():
    """
    元组  类似于只读的 List（列表）不能二次赋值
    """
    tuple = ( '1', 2 , 3.33, '4', 5.5 )
    tinytuple = (6, '7.7')
     
    print (tuple)                      # 输出完整元组
    print (tuple[0])                   # 输出元组的第一个元素
    print (tuple[1:3])                 # 输出第二个至第四个（不包含）的元素 
    print (tuple[2:])                  # 输出从第三个开始至列表末尾的所有元素
    print (tinytuple * 3)              # 输出元组两次
    print (tuple + tinytuple)          # 打印组合的元组
    return

