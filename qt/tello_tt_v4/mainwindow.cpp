#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QFileDialog"

#include <QScreen>
#include <QPixmap>
#include <QDesktopWidget>
#include <QDateTime>
#include <QMessageBox>

#include <QTextStream>

//#include "QDebug"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
  ui->setupUi(this);

  /*初始化按键id、方便统一管理*/
  ui->pushButton1->set_id(1);
  ui->pushButton2->set_id(2);
  ui->pushButton3->set_id(3);
  ui->pushButton4->set_id(4);
  ui->pushButton5->set_id(5);
  ui->pushButton6->set_id(6);
  ui->pushButton7->set_id(7);
  ui->pushButton8->set_id(8);
  ui->pushButton9->set_id(9);
  ui->pushButton10->set_id(10);
  ui->pushButton11->set_id(11);
  ui->pushButton12->set_id(12);
  ui->pushButton13->set_id(13);
  ui->pushButton14->set_id(14);
  ui->pushButton15->set_id(15);
  ui->pushButton16->set_id(16);
  ui->pushButton17->set_id(17);
  ui->pushButton18->set_id(18);
  ui->pushButton19->set_id(19);
  ui->pushButton20->set_id(20);
  ui->pushButton21->set_id(21);
  ui->pushButton22->set_id(22);
  ui->pushButton23->set_id(23);
  ui->pushButton24->set_id(24);
  ui->pushButton25->set_id(25);
  ui->pushButton26->set_id(26);
  ui->pushButton27->set_id(27);
  ui->pushButton28->set_id(28);
  ui->pushButton29->set_id(29);
  ui->pushButton30->set_id(30);
  ui->pushButton31->set_id(31);
  ui->pushButton32->set_id(32);
  ui->pushButton33->set_id(33);
  ui->pushButton34->set_id(34);
  ui->pushButton35->set_id(35);
  ui->pushButton36->set_id(36);
  ui->pushButton37->set_id(37);
  ui->pushButton38->set_id(38);
  ui->pushButton39->set_id(39);
  ui->pushButton40->set_id(40);
  ui->pushButton41->set_id(41);
  ui->pushButton42->set_id(42);
  ui->pushButton43->set_id(43);
  ui->pushButton44->set_id(44);
  ui->pushButton45->set_id(45);
  ui->pushButton46->set_id(46);
  ui->pushButton47->set_id(47);
  ui->pushButton48->set_id(48);
  ui->pushButton49->set_id(49);
  ui->pushButton50->set_id(50);
  ui->pushButton51->set_id(51);
  ui->pushButton52->set_id(52);
  ui->pushButton53->set_id(53);
  ui->pushButton54->set_id(54);
  ui->pushButton55->set_id(55);
  ui->pushButton56->set_id(56);
  ui->pushButton57->set_id(57);
  ui->pushButton58->set_id(58);
  ui->pushButton59->set_id(59);
  ui->pushButton60->set_id(60);
  ui->pushButton61->set_id(61);
  ui->pushButton62->set_id(62);
  ui->pushButton63->set_id(63);
  ui->pushButton64->set_id(64);
  ui->pushButton65->set_id(65);
  ui->pushButton66->set_id(66);
  ui->pushButton67->set_id(67);
  ui->pushButton68->set_id(68);
  ui->pushButton69->set_id(69);
  ui->pushButton70->set_id(70);

  /*添加关于、帮助标题栏*/
  actAbout = ui->menu_about->addAction("关于", this, SLOT(doAbout()));
  actHelp = ui->menu_help->addAction("帮助", this, SLOT(doHelp()));

  /*信号和槽*/
  connect(ui->pushButton65, &QPushButton::released,
          [this]() {
            //因为pushButton本身结构里面无法修改其他pushButton里面的内容，因此必须使用此方式
            ui->pushButton65->rgb_border_show();
            ui->pushButton66->rgb_border_show();
            ui->pushButton67->rgb_border_show();
          });

  connect(ui->pushButton66, &QPushButton::released,
          [this]() {
            //因为pushButton本身结构里面无法修改其他pushButton里面的内容，因此必须使用此方式
            ui->pushButton65->rgb_border_show();
            ui->pushButton66->rgb_border_show();
            ui->pushButton67->rgb_border_show();
          });

  connect(ui->pushButton67, &QPushButton::released,
          [this]() {
            //因为pushButton本身结构里面无法修改其他pushButton里面的内容，因此必须使用此方式
            ui->pushButton65->rgb_border_show();
            ui->pushButton66->rgb_border_show();
            ui->pushButton67->rgb_border_show();
          });

  connect(ui->pushButton68, &QPushButton::released,
          [this]() {
            dirpath = QFileDialog::getExistingDirectory(this, "选择目录", "./", QFileDialog::ShowDirsOnly);
            //            ui->textBrowser->setText("你选择的目录为：\n"+dirpath);
            ui->textBrowser->insertPlainText("你选择的目录为：\n" + dirpath + "\n");
            //         qDebug()<<dirpath;
          });

  connect(ui->pushButton69, &QPushButton::released,
          //=:把外部所有局部变量，类中成员以值传递
          //this：类中所有成员以值传递
          //&：把外部所有局部变量，引用符号-----容易出错
          [this]() {
            //        qDebug() << "我是69"<<tello_cfg_set;
            QPixmap pixmap = ui->frame_1->grab(QRect(QPoint(0, 0), QSize(-1, -1)));
            if (dirpath != NULL)
            {
              QString jpg_name = QDateTime::currentDateTime().toString("yy_MM_dd_hh_mm_ss.jpg");
              /*保存对应图片信息*/
              pixmap.save(dirpath + '/' + jpg_name);
              /*点阵转换导出到.txt*/
              QFile file(dirpath + "/text.txt");
              //方式：Append为追加，WriteOnly，ReadOnly
              if (!file.open(QIODevice::Append | QIODevice::Text))
              {
                QMessageBox::critical(NULL, "提示", "无法创建文件");
                return -1;
              }
              QTextStream out(&file);
              out << QString("%1").arg(tello_cfg_set) + ",#" + jpg_name << endl;
              out.flush();
              file.close();
              //            ui->textBrowser->setText("本次转换:\r\n\r\n"+QString("%1").arg(tello_cfg_set)+"\r\n\r\n"+"导出文件:"+"\r\n\r\n"+
              //                                     jpg_name+"\r\n"+"点阵导出结果添加到text.txt"
              //                                     +"\r\n\r\n\r\n\r\n\r\n\r\n"
              //                                     +QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd"));
              //            ui->textBrowser->insertPlainText("本次转换:\n"+QString("%1").arg(tello_cfg_set)+"\n"+"导出文件:"+"\n"+
              //                                     jpg_name+"\n"+"点阵导出结果添加到text.txt"
              //                                     +"\n"
              //                                     +QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd\n"));

              //            ui->textBrowser->setText(tr("<h1><font color = green>%1</font>的人品指数：<font color = orange>%2</font>"
              //                                        "<h4>点评：奸雄，实实在在的奸雄，宁可我负人人，不可人人负我，"
              //                                        "你的人品不及格，小心哦。"
              //                                        "<h2><font color = gray>代表人物：曹操</font>"
              //                                        "<img src=\":/images/CC.jpg\">"
              //                                        ));
            }
            else
            {
              //            ui->textBrowser->setText("本次转换:\r\n\r\n"+QString("%1").arg(tello_cfg_set)+"\r\n\r\n"+"提示:未选择导出文件,相关文件（.jpg ,.txt文件将无法导出"
              //                                       +"\r\n\r\n\r\n\r\n\r\n\r\n"
              //                                     +QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd")
              //                                     );
              ui->textBrowser->insertPlainText("本次转换:\n" + QString("%1").arg(tello_cfg_set) + "\n" + "提示:未选择导出文件,相关文件（.jpg ,.txt文件将无法导出" + "\n" + QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss dddd") + "\n");
            }
          });

  connect(ui->pushButton70, &QPushButton::released,
          //=:把外部所有局部变量，类中成员以值传递
          //this：类中所有成员以值传递
          //&：把外部所有局部变量，引用符号-----容易出错
          [this]() {
            led_cfg_clear();
            ui->textBrowser->setText(" ");
          });
}

MainWindow::~MainWindow()
{
  delete ui;
}
void MainWindow::led_cfg_clear(void)
{
  //    qDebug()<<"daole1";
  ui->pushButton1->reset();
  ui->pushButton2->reset();
  ui->pushButton3->reset();
  ui->pushButton4->reset();
  ui->pushButton5->reset();
  ui->pushButton6->reset();
  ui->pushButton7->reset();
  ui->pushButton8->reset();
  ui->pushButton9->reset();
  ui->pushButton10->reset();
  ui->pushButton11->reset();
  ui->pushButton12->reset();
  ui->pushButton13->reset();
  ui->pushButton14->reset();
  ui->pushButton15->reset();
  ui->pushButton16->reset();
  ui->pushButton17->reset();
  ui->pushButton18->reset();
  ui->pushButton19->reset();
  ui->pushButton20->reset();
  ui->pushButton21->reset();
  ui->pushButton22->reset();
  ui->pushButton23->reset();
  ui->pushButton24->reset();
  ui->pushButton25->reset();
  ui->pushButton26->reset();
  ui->pushButton27->reset();
  ui->pushButton28->reset();
  ui->pushButton29->reset();
  ui->pushButton30->reset();
  ui->pushButton31->reset();
  ui->pushButton32->reset();
  ui->pushButton33->reset();
  ui->pushButton34->reset();
  ui->pushButton35->reset();
  ui->pushButton36->reset();
  ui->pushButton37->reset();
  ui->pushButton38->reset();
  ui->pushButton39->reset();
  ui->pushButton40->reset();
  ui->pushButton41->reset();
  ui->pushButton42->reset();
  ui->pushButton43->reset();
  ui->pushButton44->reset();
  ui->pushButton45->reset();
  ui->pushButton46->reset();
  ui->pushButton47->reset();
  ui->pushButton48->reset();
  ui->pushButton49->reset();
  ui->pushButton50->reset();
  ui->pushButton51->reset();
  ui->pushButton52->reset();
  ui->pushButton53->reset();
  ui->pushButton54->reset();
  ui->pushButton55->reset();
  ui->pushButton56->reset();
  ui->pushButton57->reset();
  ui->pushButton58->reset();
  ui->pushButton59->reset();
  ui->pushButton60->reset();
  ui->pushButton61->reset();
  ui->pushButton62->reset();
  ui->pushButton63->reset();
  ui->pushButton64->reset();
}
void MainWindow::doHelp()
{
  QMessageBox::information(this, "帮助", "设置点阵画面:\r\n"
                                         "param display_graph: string: 长度最大为64，点阵屏显示图案的编码字符串，每个字符解读为二进制后对应位置的led点的状态，"
                                         "'0'为关闭该位置led，'r'为点亮红色，'b'为点亮蓝色，'p' 为点亮紫色，输入的长度不足64，后面对应的led点默认都是'0'熄灭状态\r\n"
                                         "该软件适用于大疆Tello_TT教育机器人，基于官方SDK开发版本，对需要设计的图片进行点阵取模，最后输出图片，并将string写入.txt文件，写入文本会对应图片，方便记忆。\r\n");
}
void MainWindow::doAbout()
{
  QMessageBox::about(this, "关于", "作者：SEASKY-刘威\n"
                                   "邮箱：liuwei_seasky@163.com\n"
                                   "版本号：v0.00.01\n"
                                   "相关：http:xxx.com\n"
                                   "更新日期：2020/10/30");
}
