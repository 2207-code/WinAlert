# WinAlert
Библиотека для упрощения работы с MessageBox в Python
<h1>Пример кода</h1>
<code>import winalert</code><br>
<code>winalert.alert("Текст окна", "Заголовок окна", icon=winalert.AlertIcon.INFO, buttons=winalert.AlertButtons.OKCANCEL)</code>
<img src="https://cdn.discordapp.com/attachments/881819180922445844/883804923756687370/T81Ob3H5y9VgAAAABJRU5ErkJggg.png">
<h1>Функции</h1>
Функция тут только одна, <code>alert</code>
<h3>Принимает такие аргументы:</h3>
<table>
  <tr>
    <th>Имя</th>
    <th>Описание</th>
    <th>Тип данных</th>
    <th>Обязателен?</th>
    <th>По умолчанию</th>
  </tr>
  <tr><td>text</td><td>Текст внутри окна</td><td>Автоконвертация: <b>str</b></td><td>✅</td><td>нету</td></tr>
  <tr><td>title</td><td>Заголовок окна</td><td>Автоконвертация: <b>str</b></td><td>❌</td><td><code>"WinAlert"</code></td></tr>
  <tr><td>icon</td><td>Иконка в окне</td><td><a href="https://github.com/2207-code/WinAlert#alerticon"><b>AlertIcon</b></a></td><td>❌</td><td><code>AlertIcon.NONE</code></td></tr>
  <tr><td>buttons</td><td>Кнопки в окне</td><td><a href="https://github.com/2207-code/WinAlert#alertbuttons"><b>AlertButtons</b></a></td><td>❌</td><td><code>AlertButtons.OK</code></td></tr>
  <tr><td>keep_on_top</td><td>Удерживать ли окно выше всех?</td><td>Автоконвертация: <b>bool</b></td><td>❌</td><td><code>True</code></td></tr>
  <tr><td>nonblocking</td><td>Является ли вызов неблокирующим</td><td>Автоконвертация: <b>bool</b></td><td>❌</td><td><code>False</code></td></tr>
</table>
<h3>Возвращает:</h3>
<table>
  <tr>
    <th>Тип данных</th>
    <th>Описание</th>
  </tr>
  <tr><td><a href="https://github.com/2207-code/WinAlert#button"><code>Button</code></a> или <code>None</code></td><td>Энумерация нажатой кнопки, <b>или <code>None</code> если вызов неблокирующий</b></td></tr>
</table>
<h1>Классы</h1>
<h2>AlertIcon</h2>
Энумерация иконки для окна. Имеет <b>такие</b> значения:<br>
<table>
  <tr>
    <th>Имя</th>
    <th>Описание</th>
  </tr>
  <tr><td><code>NONE</code></td><td>Иконки нет</td></tr>
  <tr><td><code>ERROR</code></td><td><img src="https://docs.microsoft.com/en-us/windows/win32/api/winuser/images/mb_iconhand.png"></img></td></tr>
  <tr><td><code>QUESTION</code></td><td><img src="https://docs.microsoft.com/en-us/windows/win32/api/winuser/images/mb_iconquestion.png"></img></td></tr>
  <tr><td><code>WARN</code></td><td><img src="https://docs.microsoft.com/en-us/windows/win32/api/winuser/images/mb_iconexclamation.png"></img></td></tr>
  <tr><td><code>INFO</code></td><td><img src="https://docs.microsoft.com/en-us/windows/win32/api/winuser/images/mb_iconasterisk.png"></img></td></tr>
</table>
<i>"Имя" означает аттрибут энумератора. Например <b>INFO</b> означает <code>AlertIcon.INFO</code></i>
<h2>AlertButtons</h2>
Энумерация списка кнопок для окна. Имеет <b>такие</b> значения:<br>
<table>
  <tr>
    <th>Имя</th>
    <th>Описание</th>
  </tr>
  <tr><td><code>OK</code></td><td>Одна кнопка <b>OK</b></td></tr>
  <tr><td><code>OKCANCEL</code></td><td>Кнопки <b>OK</b> и <b>Отмена</b></td></tr>
  <tr><td><code>ABORTRETRYIGNORE</code></td><td>Кнопки <b>Прервать</b>, <b>Повтор</b> и <b>Пропустить</b></td></tr>
  <tr><td><code>YESNOCANCEL</code></td><td>Кнопки <b>Да</b>, <b>Нет</b> и <b>Отмена</b></td></tr>
  <tr><td><code>YESNO</code></td><td>Кнопки <b>Да</b> и <b>Нет</b></td></tr>
  <tr><td><code>RETRYCANCELE</code></td><td>Кнопки <b>Повтор</b> и <b>Отмена</b></td></tr>
  <tr><td><code>CANCELTRYAGAINCONTINUE</code></td><td>Кнопки <b>Отмена</b>, <b>Повторить</b> и <b>Продолжить</b></td></tr>
</table>
<i>"Имя" означает аттрибут энумератора. Например <b>OK</b> означает <code>AlertButtons.OK</code></i>
<h2>Button</h2>
Энумерация ОДНОЙ кнопки, нажатой пользователем. Имеет <b>такие</b> значения:<br>
<table>
  <tr>
    <th>Имя</th>
    <th>Описание</th>
  </tr>
  <tr><td><code>UNKNOWN</code></td><td>Скрипт хз какая кнопка нажата</td></tr>
  <tr><td><code>OK</code></td><td>Кнопка <b>OK</b></td></tr>
  <tr><td><code>CANCEL</code></td><td>Кнопка <b>Отмена</b></td></tr>
  <tr><td><code>ABORT</code></td><td>Кнопка <b>Прервать</b></td></tr>
  <tr><td><code>RETRY</code></td><td>Кнопка <b>Повтор</b></td></tr>
  <tr><td><code>IGNORE</code></td><td>Кнопка <b>Пропустить</b></td></tr>
  <tr><td><code>YES</code></td><td>Кнопка <b>Да</b></td></tr>
  <tr><td><code>NO</code></td><td>Кнопка <b>Нет</b></td></tr>
  <tr><td><code>TRYAGAIN</code></td><td>Кнопка <b>Повторить</b></td></tr>
  <tr><td><code>CONTINUE</code></td><td>Кнопка <b>Продолжить</b></td></tr>
</table>
<i>"Имя" означает аттрибут энумератора. Например <b>OK</b> означает <code>Button.OK</code></i><br>
<i><code>TRYAGAIN</code> и <code>RETRY</code> это разные кнопки!</i>
