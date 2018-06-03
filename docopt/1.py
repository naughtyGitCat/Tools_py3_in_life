# coding=utf-8
"""1

Usage:
  1.py D_IP init_instance [--configSvr] [--replname=<replSetName>] [-P PORT | --port=PORT] [--disk=data{}]
  1.py init_mongos [-P PORT | --port=PORT] [--instance=<IP>:<PORT>]
  1.py -h | --help

Arguments:
  D_IP  destination IP

Options:
  -P PORT   Self port.
  --disk=DATA_NUMBER    Install in /Data{}.
  --replname=<replSetName> ReplSet`s Name.

"""
from docopt import docopt

def concat_parameters(dict_a):
    opt_str = ''
    for i in dict_a.keys():
        # 如果该选项非false(有值，或True)，且是--parameters，追加拼接到参数字符串中
        if dict_a[i]  and i[0:2] == '--':
            print('key:', i)
            opt_str = opt_str+' {}={}'.format(i,dict_a[i])
    print(opt_str)




if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1.1rc')
    # print(arguments)

    if arguments['init_instance']:
        D_IP = arguments['D_IP']
        concat_parameters(arguments)

    elif arguments['init_mongos']:
        pass






#python 1.py init_instance --port=3304
