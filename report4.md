1) Student
Name: Канатов Ерхан
Group: ИБ-23-5б
GitHub repo: https://github.com/randikhan/devnet-day1-IB23-kanatov

2) Evidence checklist (files exist)
Все артефакты собраны в папке artifacts/day4/ и соответствуют требованиям.

Docker (6.2.7)
sampleapp_curl.txt: [OK] — Ответ Flask приложения с TOKEN_HASH8.

sampleapp_token_proof.txt: [OK] — Результат grep, подтверждающий наличие хеша.

sampleapp_docker_ps.txt: [OK] — Контейнер запущен и проброшен на порт 8080.

sampleapp_build_log.txt: [OK] — Лог успешной сборки образа.

Jenkins (6.3.6)
jenkins_docker_ps.txt: [OK] — Jenkins запущен в контейнере.

buildapp_console.txt: [OK] — Вывод сборки (BuildAppJob).

testapp_console.txt: [OK] — Вывод тестов (TestAppJob).

pipeline_script.groovy: [OK] — Скрипт пайплайна с 3 стадиями.

pipeline_console.txt: [OK] — Лог выполнения пайплайна (Finished: SUCCESS).

jenkins_url.txt: [OK] — http://localhost:8080/

Ansible (7.4.8)
ansible_ping.txt: [OK] — Успешный пинг хостов.

ansible_hello.txt: [OK] — Проверка выполнения команд через Ansible.

ansible_playbook_install.txt: [OK] — Лог установки Apache.

ports_conf_after.txt: [OK] — Конфиг с измененным портом Listen 8081.

curl_apache_8081.txt: [OK] — Ответ Apache на новом порту.

Security (6.5.10)
signup_v1.txt / login_v1.txt: [OK] — Регистрация и вход (Plain text).

signup_v2.txt / login_v2.txt: [OK] — Регистрация и вход (Hashed).

db_tables.txt: [OK] — Схема БД (USER_PLAIN, USER_HASH).

db_user_hash_sample.txt: [OK] — Пример хешированных паролей в БД.

3) Commands output
Результат финальной проверки скриптом и тестами:
(.venv) devasc@labvm:~/devnet-day1-IB23-kanatov$ python src/day4_summary_builder.py
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-18T16:39:19.513926+00:00",
  "student": {
    "token": "D1-IB-23-5b-08-4B6A",
    "token_hash8": "b00c4a82",
    "name": "Kanatov",
    "group": "IB-23-5B"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "8358bc5d75c6ad26eb70ce9725b95d594a3a692d26288792455daed1ae9a173b",
    "docker_ps": "b4270767a553df66f5b21824be2ddbe3fef3fd21479fd56b296d6a7a7b160bb6",
    "docker_build_log": "a031b461a9985b53e6e12beb7184146a00c5dd77af26b5a6f44d1bcc2bb54afd",
    "docker_token_proof": "58ce0bddf5c8ecb9e964e66366308b3b12e9761ce615badfd5f63ec81d909393",
    "jenkins_docker_ps": "fe9fb44ae9a606a5c15595ce03bca49c32ac6faf4cdef9e3436298a2d6592510",
    "buildapp_console": "4c46e4b1a66a5c72920293c0ddec2fefa866bfaa69fc69efac8a90f68921b460",
    "testapp_console": "cb5182fac0742a2ba1f35d551d28127b51e007da213c80091fa90556600a41b4",
    "pipeline_script": "659ffcab7df8137c32443aa6982688cc802be2519b7821d4d5ab27c8bb5e3293",
    "pipeline_console": "d6bf85f91411ca365a0d89d75822118953b47a000d03cf76cd187a139c2345fb",
    "jenkins_url": "185f195598830dbc315eb3a6741f97eace245e9d9d2a7225c5da77b87f27f3fc",
    "ansible_ping": "67dd2a5d8c584d0b05d2d45171ae6572a01901d893312330060a5fe80b845277",
    "ansible_hello": "6b506fcd95eb0febede6e36542f9524299ecd459f7b11b6743bef44138cbb0fb",
    "ansible_playbook_install": "ccc85cb547c9b689ad36f418df798ece2c81e97877eaedebd83d4c8c8f291537",
    "ports_conf_after": "8ee0ac8272eaa90ca6a9597cb472034768331e543d074cc72141b520ffb6f686",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "2c399e1eabae97d11aa7ad24f33ddc344e245eaeffda029c399a529f66d522a9",
    "login_v1": "4adfad45954901145cf6422b14a1ae546f02190cda2d0a7cdad60533c8259229",
    "signup_v2": "c8a870f95b753cb88eefa18f61d3daef4413d4be990760a8a75ed2396a9edfa0",
    "login_v2": "a78c89bf0278cf19bdb72a153a23110522b61b9c614a5f32387d95e7dab27a61",
    "db_tables": "ad86a4abb22eb668b27efd841c9da481b1681020c8b71ebcfcf570d81ef41ee2",
    "db_user_hash_sample": "8c68d04d8bddadf80ae05ddda4c0fa7d42b9626fb1e63beb0d62b36505bbe3d6"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
(.venv) devasc@labvm:~/devnet-day1-IB23-kanatov$ 

4) Short reflection (5–8 lines)
Hardest part: Самым сложным было подружить Jenkins, запущенный в Docker, с остальными процессами и правильно настроить Pipeline. Также потребовалось время на отладку Ansible-плейбука, чтобы корректно изменить порт Apache в конфигурационном файле.

5) Problems & fixes (at least 1)

