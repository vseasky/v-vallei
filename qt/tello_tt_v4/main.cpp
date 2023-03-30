#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    a.setWindowIcon(QIcon(":/icon/image/bitbug_favicon.ico"));
    MainWindow w;
    w.show();
    return a.exec();
}
