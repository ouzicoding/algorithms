
def test(param):
    """
    函数说明
    :param param:
    :return:
    """
    msg = input('请输入：')
    print(param, msg)
    return


def test1():
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
    for key in a  == for key in a.keys()
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

