命令：

搜索：
pybabel extract -F static/i18n/babel.cfg -k gettext -o static/i18n/messages.pot .

初始化语言：
pybabel init -i static/i18n/messages.pot -d static/i18n -l en
pybabel init -i static/i18n/messages.pot -d static/i18n -l zh

更新翻译：
pybabel update -i static/i18n/messages.pot -d static/i18n

生成翻译：
pybabel compile -d static/i18n
