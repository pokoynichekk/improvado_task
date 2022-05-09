# Запуск скрипта
Скрипт запускается из терминала:

    python main.py [ACCESS_TOKEN] [USER_ID] [OPTIONS]
  
Для более подробной информации можно воспользоваться командой:

    python main.py --help
  
После выполнения в терминал выведется сообщение:

  Usage: main.py [OPTIONS] ACCESS_TOKEN USER_ID
  
  Options:
  
   -f, --format_file [csv|tsv|json] 
                                     Output file format.
                                     
   -p, --path TEXT                   Path to file.
    
   --help                            Show this message and exit.
    
# Получение токена доступа
Для работы скрипта необходимо получить токен доступа. Сделать это можно на сайте https://vkhost.github.io/

После перехода на сайт необходимо выбрать приложение vk.com и предоставить этому приложению доступ к странице.

Токен будет предоставлен в адресной строке в качестве параметра access_token.
