# Известные ошибки Docker

## Описание.
Ошибки на которые я наступил.

## Ошибки.

* error storing credentials - err: exec: "docker-credential-osxkeychain...
Решение: Не установлен компонент docker-credential-helper. В Mac устанавливается командой brew install docker-credential-helper

------------------------------------

* error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH
Решение: Заходим в конфигурациооный файл docker ~/.docker/config.json и удаляем строчку с credsStore. 
