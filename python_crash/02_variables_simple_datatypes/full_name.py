first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{full_name.title()}")

message=f"Hello,{full_name.title()}"
print(message)

full_name1="{} {}".format(first_name,last_name)
print(full_name1)

'''
f字符串：from python3.6
f'{} {}': 在字符串中插入变量的值，可在前引号前加上字母f,再将要插入的变量放在花括号内。
'''