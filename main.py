#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from user_reg_login import reg_main, login_main, user_center


def main():
    print("操作提示：")
    print("1：登录")
    print("2：注册")
    print("0：退出")

    while True:
        op = input("\n>：")

        if op == "0":
            print("感谢你的使用，下次再见！")
            sys.exit(2)
        elif op == "1":
            user_name = login_main()
            if user_name:
                print("登录成功！")
                user_center(user_name)
            else:
                print("密码错误，登录失败！")
        elif op == "2":
            reg_main()
        else:
            print("输入错误，请重新输入！")

if __name__ == "__main__":
    main()


    










