from PyQt6.QtWidgets import QApplication, QWidget, QLabel

import sys # Только для доступа к аргументам командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = QWidget()

textLabel = QLabel(window)
textLabel.setText("Hello World!")
textLabel.move(110, 85)

window.show()  # Важно: окно по умолчанию скрыто.
window.setGeometry(50, 50, 320, 200)
window.setWindowTitle("PyQt6 Example")

# Запускаем цикл событий.
app.exec()


# Приложение не доберётся сюда, пока вы не выйдете и цикл
# событий не остановится.