#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    QAction* actAbout;
    QAction* actHelp;

    void led_cfg_clear(void);
    QString dirpath;

private:
    Ui::MainWindow *ui;

private slots:
    void doHelp();//帮助文档
    void doAbout();//关于
};
#endif // MAINWINDOW_H
