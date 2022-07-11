
favorite_language="python "
print(favorite_language)
print(favorite_language.rstrip())

print(favorite_language)

favorite_language=favorite_language.rstrip()
print(favorite_language)
'''
rstrip():
这种删除只是暂时的，要永久删除这个字符串中的空白，必须将删除操作的结果关联到变量

>>> favorite_language='python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '
>>> favorite_language=favorite_language.rstrip()
>>> favorite_language
'python'
>>>
'''