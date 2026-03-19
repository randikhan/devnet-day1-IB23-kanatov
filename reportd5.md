1) Student
Name: Канатов Ерхан
Group: ИБ-23-5б
GitHub repo: https://github.com/randikhan/devnet-day1-IB23-kanatov

2) YANG (8.3.5)

Файлы-доказательства:

artifacts/day5/yang/ietf-interfaces.yang

artifacts/day5/yang/pyang_version.txt

artifacts/day5/yang/pyang_tree.txt

Скриншот (необязательно): вывод pyang -f tree

Результат:
YANG-модель успешно скачана и проанализирована с помощью pyang.
В выводе присутствует требуемая структура, включая interfaces и параметр enabled? boolean.

3) Webex (8.6.7)

Название комнаты содержит token_hash8: Да

Текст сообщения содержит token_hash8: Да

Файлы-доказательства:

artifacts/day5/webex/me.json

artifacts/day5/webex/rooms_list.json

artifacts/day5/webex/room_create.json

artifacts/day5/webex/message_post.json

artifacts/day5/webex/messages_list.json

Результат:
Через Webex API (с использованием Python) выполнены следующие действия:

Получена информация о текущем пользователе (me)

Получен список комнат

Создана новая комната с уникальным token_hash8

Отправлено сообщение с token_hash8

Получен список сообщений

4) Packet Tracer Controller REST (8.8.3)

external_access_check содержит “empty ticket”: Да

serviceTicket сохранён: Да

Файлы-доказательства:

artifacts/day5/pt/external_access_check.json

artifacts/day5/pt/network_devices.json

artifacts/day5/pt/hosts.json

artifacts/day5/pt/postman_collection.json

artifacts/day5/pt/postman_environment.json

artifacts/day5/pt/pt_internal_output.txt

Результат:
Работа с REST API контроллера Packet Tracer выполнена успешно:

Проверен внешний доступ (получен ответ с “empty ticket”)

Получен и сохранён service ticket

Выполнены авторизованные GET-запросы с заголовком X-Auth-Token

Получены данные об устройствах сети и хостах

Экспортированы коллекция и окружение Postman

Выполнен Python-код внутри Packet Tracer

5) Вывод команд (вставить как есть)
python src/day5_summary_builder.py
pytest -q